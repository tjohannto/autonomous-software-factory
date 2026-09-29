---
name: software-factory
description: Domain-agnostic Software Factory based on Spec-Driven Development (SDD) & NovaSmart AI Governance.
---

# Software Factory (Core)

Dieses Skill definiert das wiederverwendbare Fundament für eine autonome Software-Entwicklungsfabrik nach dem **Spec-Driven Development (SDD)**-Prinzip und **Vier-Augen-Qualitätssicherung**.

## Rollen & Prompts

1. **[Interview Agent (Spec Lead)](prompts/interview-agent.md):** Führt das Gespräch mit dem Vibecoder (auch Voice-to-Text), stellt max. 1-2 Fragen pro Interaktion und erstellt die Spezifikation basierend auf [spec-template.md](templates/spec-template.md).
2. **[Coding Agent (Implementer)](prompts/coding-agent.md):** Schreibt den Produktivcode exakt nach `spec.md`. Schreibt selbst keine Tests, um Confirmation Bias zu vermeiden.
3. **[Test Engineer Agent (SDET)](prompts/test-engineer-agent.md):** Schreibt unabhängig die automatisierte Test-Suite (Happy Paths + Edge Cases) streng nach den Akzeptanzkriterien.
4. **[QA Gatekeeper Agent (Runner)](prompts/qa-agent.md):** Führt die Test-Suite deterministisch in der Shell aus, scannt nach Secrets/Lints und gibt den PR frei (oder liefert `review_feedback.md`).
5. **[Git Governance & Standards](prompts/git-governance.md):** Regeln für Branching (`main` <- `dev` <- `feat/*`), Conventional Commits und PR-Templates.

## Daten- & Arbeitsfluss (Vier-Augen-Prinzip)

```text
               [ Vibecoder (Voice/Text) ]
                            │
                            ▼
                    [ Interview Agent ]
                            │
                            ▼ erzeugt
                       [ spec.md ]
                            │
            ┌───────────────┴───────────────┐
            ▼ (Parallel)                    ▼ (Parallel)
    [ Coding Agent ]             [ Test Engineer Agent ]
    (Produktivcode)              (Test-Suite & Edge Cases)
            │                               │
            └───────────────┬───────────────┘
                            ▼
                 [ QA Gatekeeper Agent ]
                   (Führt Tests in Shell aus)
                   ├── [PASS] ──▶ Auditierter PR (dev Branch)
                   └── [FAIL] ──▶ review_feedback.md ──▶ [Coding Agent]
```
