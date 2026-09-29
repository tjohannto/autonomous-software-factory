# Domain Overlay: Web App (MVP1)

This overlay extends the core `software-factory` (MVP0) with web application roles and the **Contract-First Handshake Pattern**.

---

## 🏗️ The Contract-First Pattern

To prevent frontend and backend agents from drifting or hallucinating divergent interfaces, agents never code blindly.
Instead:

```text
               [ spec.md ]
                    │
                    ▼
          [ api-contract.yaml ] (OpenAPI 3.0 / REST Contract)
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
[ Frontend Agent ]        [ Backend Agent ]
(Builds UI with mocks)    (Builds endpoints & DB)
       │                         │
       └────────────┬────────────┘
                    ▼
          [ QA / Integration ]
      (Verifies contract compliance)
```

---

## 👥 Specialized Roles (Overlays)

* **[frontend-agent.md](prompts/frontend-agent.md):** Focuses on user experience, component architecture, accessibility (a11y), responsive design, and mock APIs.
* **[backend-agent.md](prompts/backend-agent.md):** Focuses on schema compliance, validation, business logic, security, and database migrations.

---

## 🔄 Inheritance from Core

Both agents automatically inherit all governance and quality guidelines from the core directory:
* Git Workflow & Branching: `../../prompts/git-governance.md`
* Coding Standards: `../../prompts/coding-agent.md`
* PR Template: `../../templates/pr-template.md`
