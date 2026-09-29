# Domain Overlay: Web App (MVP1)

Dieses Overlay erweitert die generische `software-factory` (MVP0) um WebApp-spezifische Rollen und das **Contract-First Handshake-Muster**.

---

## 🏗️ Das Contract-First Muster

Um Kollisionen und Missverständnisse zwischen Frontend und Backend zu vermeiden, coden die Agenten niemals blind los. 
Stattdessen gilt:

```text
               [ spec.md ]
                    │
                    ▼
          [ api-contract.yaml ] (OpenAPI 3.0 / REST Contract)
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
[ Frontend Agent ]        [ Backend Agent ]
(Baut UI mit Mocks)       (Baut Endpunkte & DB)
       │                         │
       └────────────┬────────────┘
                    ▼
          [ QA / Integration ]
      (Prüft Contract-Compliance)
```

---

## 👥 Spezialisierte Rollen (Overlays)

* **[frontend-agent.md](prompts/frontend-agent.md):** Fokussiert auf User Experience, Komponentenarchitektur, Barrierefreiheit und Mock-APIs.
* **[backend-agent.md](prompts/backend-agent.md):** Fokussiert auf Schnittstellenkonformität, Validierung, Business-Logik und Datenbank-Migrationen.

---

## 🔄 Vererbung von der Basis

Beide Agenten erben automatisch alle Governance- und Qualitätsregeln aus dem übergeordneten Verzeichnis:
* Git-Workflow & Branching: `../../prompts/git-governance.md`
* Basis-Coding-Standards: `../../prompts/coding-agent.md`
* PR-Template: `../../templates/pr-template.md`
