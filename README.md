# Autonomous Software Factory (Core, WebApp Overlay & Cost-Engine)

A modular, evolvable Software Factory enabling software engineers to build and operate standardized multi-agent teams. Domain experts and product owners ("Vibe Coders") drive software development via **Spec-Driven Development (SDD)**, voice/text memos, and deterministic quality gates — hardened by **agile Scrum story-slicing**, **context optimization**, **cost-efficient LLM routing**, and **enterprise multi-agent governance** (inspired by **NovaSmart Enterprise AI Governance**).

---

## 🎯 Vision & Core Principles

1. **Scrum Slicing Instead of Giant Specs:**
   * Never implement epics in a single prompt. The **Interview Agent** automatically breaks down large ideas into bite-sized user stories (max. 1–3 REQs per story).
2. **Scrum Master as Context Optimizer:**
   * Crafts tailored **kick-off prompts**, extracts minimal interface skeletons from existing code, and prevents context bloat (<3,000 tokens) and attention degradation.
3. **Economic Efficiency via LLM-Model Proxy:**
   * Three-tier routing (Tier 1: Heavyweight, Tier 2: Workhorse, Tier 3: Fast/Utility). Always starts with the most economical model and escalates only when edge cases fail.
   * Full observability logging token costs, latency, and success rates (`Efficiency Score`).
4. **Reuse-First (Double-Checked Against Greenfield Spam):**
   * **In Coder:** Mandatory workspace research before creating new utility functions or components.
   * **In QA Gatekeeper:** Git diff inspection against code duplication. Reinventing the wheel triggers an automatic rejection!
5. **Four-Eyes Principle & Deterministic QA:**
   * Role separation: The **Coding Agent** writes application code only. An independent **Test Engineer Agent (SDET)** writes test suites against acceptance criteria and edge cases.
   * The **QA Gatekeeper** executes tests deterministically in a shell sandbox (only Exit Code 0 counts), screens for secret leaks, and prepares audited pull requests.

---

## 🏛️ Autonomous Factory Workflow

```text
               [ Vibe Coder (Voice / Text) ]
                            │
                            ▼
                    [ Interview Agent ]  ◄── (Epic Decomposer: Slices User Stories)
                            │
                            ▼ generates
                    [ specs/01-story.md ]
                            │
                            ▼
                  [ Scrum Master Agent ] ◄── (Builds Kick-off Prompt, Protects Context Window)
                            │
                            ▼
                [ LLM Proxy / Cost Router ] (Routes Tier 1 / 2 / 3 by Task Type)
                            │
            ┌───────────────┴───────────────┐ (Parallel Execution on feat/01-story)
            ▼                               ▼
    [ Coding Agent ]             [ Test Engineer Agent ]
    (Inspects existing code,     (Writes Test Suite & Edge Cases
     implements app code)         independently from coder)
            │                               │
            └───────────────┬───────────────┘
                            ▼ Handoff to Sandbox
                 [ QA Gatekeeper Agent ] ◄── (1. Runs Tests, 2. Anti-Duplication Check)
                            │
       ┌────────────────────┴────────────────────────┐
       ▼ [FAIL: Tests Red OR Duplicates Found]       ▼ [PASS: Tests Green & Reuse OK]
  [ review_feedback.md ]                     [ Audited Pull Request ]
  (Retry loop with Scrum Master hint,        (PR Template targeting dev branch)
   optional Proxy escalation to Tier 1)              │
                                                     ▼ Squash & Merge
                                              [ dev / Staging ]
                                                     │
                                                     ▼ Release PR
                                             [ main / Production ]
```

---

## 📁 Repository Structure

```text
.
├── README.md                                          # System documentation
├── specs/                                             # Historic user stories (specs/01-xyz.md)
├── logs/                                              # Evaluation & token cost logs (model-eval.jsonl)
├── src/                                               # Production application code
├── tests/                                             # Independent test suites
└── .agents/
    └── skills/
        └── software-factory/
            ├── SKILL.md                               # Base skill definition
            ├── templates/
            │   ├── spec-template.md                   # Lean spec template with "Code Reuse First"
            │   └── pr-template.md                     # Audited PR template with reuse verification
            ├── prompts/
            │   ├── interview-agent.md                 # PO, Scrum Master & Epic Decomposer
            │   ├── scrum-master-agent.md              # Context Window Protection & Kick-off Prompts
            │   ├── coding-agent.md                    # Implementer (App code with mandatory reuse)
            │   ├── test-engineer-agent.md             # Independent SDET (Test suites & edge cases)
            │   ├── qa-agent.md                        # QA Gatekeeper (Runner & Anti-Duplication Guard)
            │   └── git-governance.md                  # Branching, Conventional Commits & Release Rules
            ├── proxy/                                 # 💰 LLM PROXY & COST CONTROLLING
            │   ├── PROXY_ARCHITECTURE.md              # 3-Tier routing & escalation concept
            │   └── templates/
            │       └── model-eval-schema.json         # JSON schema for token costs & QA tracking
            └── extensions/                            # 🚀 MODULAR DOMAIN OVERLAYS
                └── domain-webapp/
                    ├── EXTENSION.md                   # WebApp architecture & Contract-First doc
                    ├── templates/
                    │   └── api-contract.yaml          # OpenAPI 3.0 Contract Standard
                    └── prompts/
                        ├── frontend-agent.md          # UI, a11y, State, Mock APIs
                        └── backend-agent.md           # API Compliance, Security, DB Migrations
```

---

## 🚦 Roles & Responsibilities

| Role | Primary Responsibility | Cardinal Rule |
| :--- | :--- | :--- |
| **Interview Agent** | Product Owner, Epic Decomposer, Spec Generation | Detect epics, slice to max. 1–3 REQs per story; secure Definition of Ready (DoR). |
| **Scrum Master Agent** | Context Optimizer & Task Packager | Keep context windows small (<3k tokens); generate minimal interface kick-off prompts. |
| **LLM Proxy & Router** | Cost & Quality Optimization | Start at cheapest tier (Workhorse/Local); dynamically escalate to Tier 1 on failures. |
| **Coding Agent** | Application code implementation | **Reuse First:** Search workspace before creating files; never write own tests. |
| **Test Engineer Agent** | Test suite, AC coverage, edge cases | Never write app code; test objectively against the spec. |
| **QA Gatekeeper** | Test runner, Anti-Duplication, Secret scan | **Inspect diff for code duplicates;** unbribable Exit Code 0 verifier. |

---

## 🗺️ Roadmap

- [x] **Core & Governance (MVP0)**
  - [x] Agile story-slicing (Scrum-style, max. 1–3 REQs per story).
  - [x] Scrum Master Agent for context optimization & kick-off prompts.
  - [x] LLM-Model Proxy & Cost-Quality Router (3-Tier model & dynamic escalation).
  - [x] "Code Reuse First" mechanism (in Coder AND as QA gate).
  - [x] Four-Eyes Principle: Coding Agent vs. Test Engineer Agent.
  - [x] QA Gatekeeper Agent (Shell runner & compliance).
  - [x] Git governance, branch protection & PR template (NovaSmart standard).
- [x] **Domain Overlay: Web App (MVP1)**
  - [x] Overlay pattern without copy-paste redundancy (inherits base rules).
  - [x] Specialized roles: Frontend Engineer & Backend Engineer.
  - [x] Contract-First handshake pattern (`api-contract.yaml`).
- [ ] **Tech-Stack Profiles (MVP2)**
  - [ ] Concrete stack profiles (e.g., Angular Frontend + NestJS/Go Backend).
  - [ ] Integrated headless linter and test runner templates.
