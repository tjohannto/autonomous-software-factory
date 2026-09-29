# LLM-Model Proxy & Cost-Quality Router

Der **LLM-Model Proxy** ist das wirtschaftliche und qualitative Kontrollzentrum der Software Factory. 
Er sorgt dafür, dass jede Aufgabe an das **kostenoptimalste Modell** verteilt wird, das die geforderte Qualität zuverlässig liefert. 
Über ein kontinuierliches Feedback-Logging (Quality & Cost Flywheel) bewertet das System Modelle nach realen Erfolgsraten.

---

## 🎯 Die 3 Modell-Tiers (Aufgabenverteilung)

| Tier | Modell-Beispiele | Kosten / 1M Tokens (Richtwert) | Ideale Aufgaben |
| :--- | :--- | :--- | :--- |
| **Tier 1: Heavyweight** *(High Reasoning)* | Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro | \$3.00 – \$15.00 | • Epic-Zerlegung & Architektur<br>• Komplexe Refactorings über viele Dateien<br>• Eskalations-Stufe bei hartnäckigen QA-Fails |
| **Tier 2: Workhorse** *(Mid / Efficient Code)* | GPT-4o-mini, Gemini 1.5 Flash, Claude 3.5 Haiku | \$0.15 – \$1.00 | • Standard User-Story Implementierung<br>• Test-Suite Generierung (SDET)<br>• Review-Feedback Auswertung |
| **Tier 3: Utility / Fast** *(Low-Cost / Local)* | DeepSeek Coder, Llama 3 8B, Gemini Flash-Lite | \$0.05 – \$0.10 (oder lokal \$0) | • Regex-Fixes & Syntax-Korrekturen<br>• Git Commit Messages & PR-Formatierung<br>• Diktat-/Voice-Bereinigung im Interview |

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
