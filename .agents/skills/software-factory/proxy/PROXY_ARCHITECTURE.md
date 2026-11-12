# LLM-Model Proxy & Cost-Quality Router

Der **LLM-Model Proxy** ist das wirtschaftliche und qualitative Kontrollzentrum der Software Factory. 
Er sorgt dafür, dass jede Aufgabe an das **kostenoptimalste Modell** verteilt wird, das die geforderte Qualität zuverlässig liefert. 
Über ein kontinuierliches Feedback-Logging (Quality & Cost Flywheel) bewertet das System Modelle nach realen Erfolgsraten.

---

## 🎯 Die Modell-Tiers (Aufgabenverteilung)

Drei Cloud-Tiers (1–3) plus die optionale lokale Stufe **Tier L**, die in der Reihenfolge vor Tier 3 steht.

| Tier | Modell-Beispiele | Kosten / 1M Tokens (Richtwert) | Ideale Aufgaben |
| :--- | :--- | :--- | :--- |
| **Tier 1: Heavyweight** *(High Reasoning)* | Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro | \$3.00 – \$15.00 | • Epic-Zerlegung & Architektur<br>• Komplexe Refactorings über viele Dateien<br>• Eskalations-Stufe bei hartnäckigen QA-Fails |
| **Tier 2: Workhorse** *(Mid / Efficient Code)* | GPT-4o-mini, Gemini 1.5 Flash, Claude 3.5 Haiku | \$0.15 – \$1.00 | • Standard User-Story Implementierung<br>• Test-Suite Generierung (SDET)<br>• Review-Feedback Auswertung |
| **Tier L: Local** *(optional, kostenfrei)* | Ollama, z. B. `qwen3-coder:30b` | \$0 (lokal) | • Siehe Abschnitt „Tier L (Local)“<br>• Nur risikoarme, leicht prüfbare Aufgaben |
| **Tier 3: Utility / Fast** *(Low-Cost / Local)* | DeepSeek Coder, Llama 3 8B, Gemini Flash-Lite | \$0.05 – \$0.10 (oder lokal \$0) | • Regex-Fixes & Syntax-Korrekturen<br>• Git Commit Messages & PR-Formatierung<br>• Diktat-/Voice-Bereinigung im Interview |

---

## 🏠 Tier L (Local) – optionale, kostenfreie Stufe

Tier L ist ein lokal betriebenes Modell (Referenz: Ollama auf `127.0.0.1:11434`, Modell `qwen3-coder:30b`; Messwerte und
Einschränkungen: lokale Benchmark-Notiz E2, Qualitätsbewertung dort noch offen). Es ist **optional** und ändert die
Architektur nicht: Ohne Tier L gilt das Routing oben unverändert. Konfiguration: [`templates/routing-local.example.yaml`](templates/routing-local.example.yaml).

### Eignung
Aufgaben mit **geringem Risiko** und **leicht prüfbarem Ergebnis**:
* Commit-Message-Entwurf (Prüfung: Conventional-Commits-Format)
* Zusammenfassung von Log- und Testausgaben
* Formatierung von Specs und PR-Texten
* Boilerplate und Testgerüste (Prüfung: Tests/Lint laufen)
* Kontext-Verdichtung für den Scrum Master (Ergebnis wird gegen das Quell-Material gegengelesen)

### Ausschluss (harte Regel)
Tier L trifft **nie** ein Qualitäts- oder Sicherheitsurteil. Ausgeschlossen sind:
* QA-Gatekeeper-Verdikt (`VERIFIED` / `QA_FAILED`)
* Secret-Prüfung und Duplikat-Prüfung
* Red/Green-Zertifizierung
* Security-Review (jedes Ergebnis eines lokalen Modells wäre allenfalls ein Hinweis, keine Prüfung)

Diese Prüfungen bleiben deterministisch (Tests, Tools, Linter) oder laufen auf höheren Tiers; verbindlich entscheidet der Mensch.

### Eskalation
```text
[ Aufgabe, Tier L zugeordnet ] ──▶ [ lokaler Versuch (max. 1) ] ──▶ [ Prüfung: Schema / Tests / Lint ]
                                                                     ├── [OK]   ──▶ fertig
                                                                     └── [FAIL oder offensichtliches Scheitern]
                                                                              (Timeout, leere/abgeschnittene Antwort)
                                                                              ▼ automatisch
                                                                      Tier 3 (oder Tier 2)
```
* **Maximal ein lokaler Versuch pro Aufgabe**, kein Retry-Loop auf Tier L.
* Die Eskalation wird geloggt (`escalated_from_local: true`); danach gelten die normalen Regeln für Tier 3 / 2.
* Ist der lokale Endpoint nicht erreichbar, wird die Aufgabe ohne Versuch wie ohne Tier L geroutet.
* Endpoint nur `localhost`; vertraulicher Code verlässt den Rechner nicht.

### Zusätzliche Logfelder (optional, abwärtskompatibel)
`tier` darf `"L"` sein; `runtime` (`local`/`cloud`), `local_latency_ms`, `escalated_from_local`, `estimated_tokens_saved`.
Siehe `templates/model-eval-schema.json`. Bestehende Pflichtfelder sind unverändert.

---

## 🔄 Dynamic Escalation Routing (Selbstheilender Loop)

Statt standardmäßig das teuerste Modell zu nutzen, startet der Proxy immer mit dem **günstigsten qualifizierten Modell**:

```text
               [ Task vom Scrum Master ]
                           │
                           ▼
                 [ Proxy: Wähle Tier 2 ] (z.B. Flash / Mini)
                           │
                           ▼
                  [ QA Gatekeeper ]
                   ├── [PASS] ──▶ Fertig! (Kosten minimal gehalten)
                   └── [FAIL] ──▶ Retry 1 mit Tier 2 (Hint vom Scrum Master)
                                         │
                                         ▼ [Erneuter FAIL]
                                [ Automatische Eskalation auf Tier 1! ]
                                (Heavyweight löst den schwierigen Edge Case)
```

---

## 📊 Observability & Flywheel (Das Evaluations-Schema)

Jeder API-Call wird in `logs/model-eval.jsonl` erfasst:

```json
{
  "timestamp": "2026-09-29T12:20:00Z",
  "task_id": "01-task-extractor-cli",
  "task_type": "CODE_IMPLEMENTATION",
  "model_used": "gemini-1.5-flash",
  "tier": 2,
  "tokens": {
    "prompt_tokens": 1250,
    "completion_tokens": 340,
    "total_cost_usd": 0.00032
  },
  "qa_result": {
    "first_time_pass": false,
    "attempts_needed": 2,
    "final_status": "VERIFIED"
  },
  "efficiency_score": 0.85
}
```

### Der Efficiency Score
$$\text{Efficiency Score} = \frac{\text{Erfolgsquote (\%)}}{\text{Kosten pro gelöster Story (\$) \times 1000}}$$

Das System kann automatisch Berichte erstellen, welches Modell für welchen Aufgabentyp die beste Rendite (höchste Pass-Rate bei geringsten Token-Kosten) bietet.
