# Autonomous Software Factory (Core & WebApp Overlay)

Eine modulare, evolvierbare Software-Entwicklungsfabrik, die Software-Entwicklern ermöglicht, standardisierte Agenten-Teams aufzusetzen. Endanwender und Domänenexperten ("Vibecoder") steuern die Entwicklung über **Spec-Driven Development (SDD)**, Sprach- oder Texteingaben und deterministische Quality Gates – gehärtet durch **agile Story-Zerlegung (Scrum-Style)**, **doppelt abgesicherte Code-Wiederverwendung (Reuse First im Coder & QA)** und die Governance-Prinzipien moderner Multi-Agent-Systeme (inspiriert durch **NovaSmart Enterprise AI Governance**).

---

## 🎯 Vision & Kernprinzipien

1. **Scrum & Story-Slicing statt Monster-Specs:**
   * Niemals Epics am Stück implementieren. Der Interview Agent schneidet große Ideen automatisch in mundgerechte User Stories (max. 1–3 REQs).
2. **Reuse First (Doppelt geprüft gegen Greenfield-Spam):**
   * **Im Coder:** Prüfpflicht vor dem Schreiben neuer Zeilen.
   * **Im QA Gatekeeper:** Diff-Inspektion auf unnötige Duplikate. Erfindet der Coder das Rad neu, wird der PR abgelehnt!
3. **Vier-Augen-Prinzip:**
   * Rollentrennung: Der Coding Agent schreibt ausschließlich Produktivcode. Der unabhängige **Test Engineer Agent (SDET)** schreibt die Test-Suite gegen die Akzeptanzkriterien.
4. **Deterministische QA & NovaSmart Governance:**
   * QA Gatekeeper führt Tests in der Shell aus (Exit Code 0), scannt nach Secrets und erzwingt saubere Pull Requests nach `dev` via Squash & Merge.

---

## 🏛️ Der agile Fabrik-Workflow

```text
               [ Vibecoder (Voice/Text) ]
                            │
                            ▼
                    [ Interview Agent ]  ◄── (Epic Decomposer: Schneidet Stories)
                            │
                            ▼ erzeugt
                    [ specs/01-story.md ] ◄── (Scope, Code-Reuse, 1-3 REQs, ACs)
                            │
            ┌───────────────┴───────────────┐ (Parallele Ausführung auf feat/01-story)
            ▼                               ▼
    [ Coding Agent ]             [ Test Engineer Agent ]
    (Prüft Bestandscode,         (Schreibt Test-Suite & Edge Cases
     schreibt Produktivcode)      unabhängig vom Coder)
            │                               │
            └───────────────┬───────────────┘
                            ▼ Handoff an Sandbox
                 [ QA Gatekeeper Agent ] ◄── (1. Tests ausführen, 2. Anti-Duplication Check)
                            │
       ┌────────────────────┴────────────────────────┐
       ▼ [FAIL: Tests rot ODER Duplikate]            ▼ [PASS: Tests grün & Reuse OK]
  [ review_feedback.md ]                     [ Auditierter Pull Request ]
  (Retry Loop an Coder, max. 3x)             (PR-Template nach dev Branch)
                                                     │
                                                     ▼ Squash & Merge
                                              [ dev / Staging ]
                                                     │
                                                     ▼ Release PR
                                             [ main / Production ]
```

---

## 📁 Projektstruktur

```text
.
├── README.md                                          # Diese Systemdokumentation
├── specs/                                             # Historisierte User Stories (specs/01-xyz.md)
└── .agents/
    └── skills/
        └── software-factory/
            ├── SKILL.md                               # Base Skill-Definition
            ├── templates/
            │   ├── spec-template.md                   # Schlankes Spec-Template mit "Code Reuse First"
            │   └── pr-template.md                     # Auditierter PR inkl. Reuse-Nachweis
            ├── prompts/
            │   ├── interview-agent.md                 # PO, Scrum Master & Epic Decomposer
            │   ├── coding-agent.md                    # Implementer (App-Code mit Reuse-First-Pflicht)
            │   ├── test-engineer-agent.md             # Unabhängiger SDET (Test-Suite)
            │   ├── qa-agent.md                        # QA Gatekeeper (Runner & Anti-Duplication Guard)
            │   └── git-governance.md                  # Branching-, Commit- & Release-Regeln
            │
            └── extensions/                            # 🚀 MODULARE DOMAIN OVERLAYS
                └── domain-webapp/
                    ├── EXTENSION.md                   # WebApp Architektur & Contract-First Doku
                    ├── templates/
                    │   └── api-contract.yaml          # OpenAPI 3.0 Contract Standard
                    └── prompts/
                        ├── frontend-agent.md          # UI, a11y, State, Mock-APIs
                        └── backend-agent.md           # API Compliance, Security, DB Migrations
```

---

## 🚦 Rollen & Zuständigkeiten

| Rolle | Primäre Verantwortung | Wichtigste Regel |
| :--- | :--- | :--- |
| **Interview Agent** | Product Owner, Scrum-Splitting, Spec-Erstellung | Erkennt Epics, schneidet max. 1–3 REQs pro Story; benennt wiederverwendbare Module. |
| **Coding Agent** | Implementierung des Produktivcodes | **Reuse First:** Vorhandene Komponenten suchen und nutzen; keine eigenen Tests. |
| **Test Engineer Agent** | Test-Suite, AC-Abdeckung, bösartige Edge Cases | Schreibt keinen Produktivcode; testet unabhängig gegen die Spec. |
| **QA Gatekeeper** | Testausführung, Anti-Duplication Guard, Secret-Scan | **Prüft Diff auf Code-Duplikate;** lehnt PR ab, wenn Rad neu erfunden wurde. |

---

## 🗺️ Roadmap

- [x] **Core & Governance (MVP0)**
  - [x] Agile Story-Slicing (Scrum-Style, max. 1–3 REQs pro Story).
  - [x] "Code Reuse First"-Mechanismus (im Coder UND als QA-Prüfschranke).
  - [x] Vier-Augen-Trennung: Coding Agent vs. Test Engineer Agent.
  - [x] QA Gatekeeper Agent (Shell-Runner & Compliance).
  - [x] Git-Governance, Branch Protection & PR-Template (NovaSmart Standard).
- [x] **Domain Overlay: Web App (MVP1)**
  - [x] Overlay-Konzept ohne Copy-Paste Redundanz (Vererbung der Base-Regeln).
  - [x] Spezialisierte Rollen: Frontend Engineer & Backend Engineer.
  - [x] Contract-First Handshake-Muster (`api-contract.yaml`).
- [ ] **Tech-Stack Profile (MVP2)**
  - [ ] Konkrete Profile (z. B. Angular Frontend + NestJS/Go Backend).
  - [ ] Integrierte Linter-/Test-Runner-Templates.
