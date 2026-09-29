---
name: software-factory
description: Domain-agnostic Software Factory based on Spec-Driven Development (SDD), Scrum Task Packaging, Red-Green TDD, LLM Cost Proxy & NovaSmart AI Governance.
---

# Software Factory (Core)

This skill provides the reusable foundation for an autonomous, cost-optimized Software Factory following **Spec-Driven Development (SDD)**, **agile Scrum packaging**, and **enterprise quality governance**.

## Roles & Agent Prompts

1. **[Interview Agent (Spec Lead & Preview Gatekeeper)](prompts/interview-agent.md):** Engages with the Vibe Coder, slices epics into actionable user stories (`specs/01-xyz.md`), and presents interactive staging previews for human sign-off before production release.
2. **[Scrum Master Agent (Task Packager & Interface Architect)](prompts/scrum-master-agent.md):** Defines **Interface Skeletons** (method signatures & types) to eliminate import mismatches, protects context windows (<3,000 tokens), and locks runtime dependencies.
3. **[Coding Agent (Implementer)](prompts/coding-agent.md):** Implements application code matching the Interface Skeleton under strict **Reuse-First** rules. Never writes own tests.
4. **[Test Engineer Agent (SDET)](prompts/test-engineer-agent.md):** Independently writes comprehensive automated test suites against acceptance criteria and edge cases.
5. **[QA Gatekeeper Agent (Runner, TDD Certifier & Compliance)](prompts/qa-agent.md):** Enforces **Red-Green TDD** (proves tests fail on empty skeletons first), validates hermetic dependencies, rejects code duplicates, and screens for secrets.
6. **[Git Governance & Standards](prompts/git-governance.md):** Lifecycle rules (`main` <- `dev` <- `feat/*`), Conventional Commits, and PR templates.

## Cost & Model Optimization

* **[LLM-Model Proxy & Cost Router](proxy/PROXY_ARCHITECTURE.md):** Distributes tasks across 3 model tiers (Tier 1: Heavyweight, Tier 2: Workhorse, Tier 3: Utility) with dynamic escalation and cost/quality logging (`proxy/templates/model-eval-schema.json`).

## Autonomous Workflow (Hardened)

```text
               [ Vibe Coder (Voice / Text) ]
                            │
                            ▼
                    [ Interview Agent ]  ◄── (Epic Decomposer: Slices Stories)
                            │
                            ▼ generates
                    [ specs/01-story.md ]
                            │
                            ▼
                  [ Scrum Master Agent ] ◄── (Defines Interface Skeleton & Locks Dependencies)
                            │
                ┌───────────┴───────────┐
                ▼                       ▼ (Hands off Skeleton)
        [ Coding Agent ]        [ Test Engineer Agent ]
        (App Code)              (Test Suite against Skeleton)
                │                       │
                │                       ▼ Stage 1: RED Verification
                │              [ QA Gatekeeper Agent ]
                │              (Confirms tests fail on empty skeleton!)
                │                       │
                └───────────┬───────────┘ Stage 2: GREEN Verification
                            ▼
                 [ QA Gatekeeper Agent ] (All tests turn green; Anti-Duplication & Secret check)
                            │
                            ▼ [PASS]
                 [ Pull Request to dev ]
                            │ Squash & Merge
                     [ dev / Staging ]
                            │
                            ▼ Vibe Preview Gate (Interactive Demo)
                    [ Interview Agent ]  ◄── (Asks Human: "Does UX feel right?")
                            │
                            ▼ [HUMAN APPROVAL]
                  [ Release to main ]
```
