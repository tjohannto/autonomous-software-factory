# Autonomous Software Factory (Enterprise Edition)

A modular, evolvable Software Factory enabling software engineers to build and operate standardized multi-agent teams. Domain experts and product owners ("Vibe Coders") drive software development via **Spec-Driven Development (SDD)**, voice/text memos, and deterministic quality gates — hardened by **agile Scrum story-slicing**, **Interface Skeletons**, **Red-Green TDD validation**, **cost-efficient LLM routing**, and **enterprise multi-agent governance** (inspired by **NovaSmart Enterprise AI Governance**).

---

## 🎯 Vision & Core Principles

1. **Scrum Slicing Instead of Giant Specs:**
   * Never implement epics in a single prompt. The **Interview Agent** automatically breaks down large ideas into bite-sized user stories (max. 1–3 REQs per story).
2. **Interface Skeletons & Contract Handshake:**
   * Before parallel execution begins, the **Scrum Master Agent** establishes empty function/class signatures and types. This prevents naming and import mismatches between Coder and SDET.
3. **Red-Green TDD Certification (Anti-Fake Test Guard):**
   * The **QA Gatekeeper** tests the SDET's test suite against the empty skeleton *first*. Tests **must fail (RED)** to prove they are not tautologies (`assert True == True`). Only then are they run against the Coder's implementation to turn **pass (GREEN)**.
4. **Hermetic Dependencies & Anti-Greenfield Guard:**
   * No arbitrary runtime package installations. Strict diff inspection rejects PRs if existing functions are duplicated or undeclared dependencies are introduced.
5. **Economic Efficiency via LLM-Model Proxy:**
   * Three-tier routing (Tier 1: Heavyweight, Tier 2: Workhorse, Tier 3: Fast/Utility). Always starts with the most economical model and escalates only when edge cases fail.
6. **Vibe Coder Preview Gate (Human-in-the-Loop Release):**
   * Staging changes (`dev`) are presented as an interactive preview or CLI demo to the human Vibe Coder before any promotion to Production (`main`).

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
                  [ Scrum Master Agent ] ◄── (1. Defines Interface Skeleton, 2. Locks Dependencies)
                            │
                ┌───────────┴───────────┐
                ▼ (Reads Skeleton)      ▼ (Reads Skeleton)
        [ Coding Agent ]        [ Test Engineer Agent ]
        (Implements Code)       (Writes Test Suite against Skeleton)
                │                       │
                │                       ▼ Stage 1: RED Verification
                │              [ QA Gatekeeper Agent ]
                │              (Proves tests FAIL on empty skeleton!)
                │                       │
                └───────────┬───────────┘ Stage 2: GREEN Verification
                            ▼
                 [ QA Gatekeeper Agent ] ◄── (All tests turn green; Anti-Duplication & Secret check)
                            │
                            ▼ [PASS]
                 [ Pull Request to dev ]
                            │ Squash & Merge
                     [ dev / Staging ]
                            │
                            ▼ Vibe Preview Gate (Interactive Demo / URL)
                    [ Interview Agent ]  ◄── (Asks Human: "Does UX feel right?")
                            │
                            ▼ [HUMAN APPROVAL: "Ship it!"]
                  [ Release to main ]
```

---

## 🌐 The "Web App" Domain Overlay & Real-World Stack Examples

The Software Factory is organized in three distinct architectural layers to eliminate copy-paste configuration drift:

```text
[ Layer 0: Core Factory ] (SDD, Scrum Master, Red-Green TDD, Git Governance, LLM Cost Proxy)
         ▲
         │ inherits & extends
[ Layer 1: domain-webapp ] (Contract-First OpenAPI, Frontend/Backend Role Decoupling)
         ▲
         │ specializes for concrete frameworks
[ Layer 2: Concrete Tech-Stack Profiles ]
         ├── mbargo-reporting    (Angular 21 + Play Framework 3 + Jest)
         └── mbargo-admin-webtop (Apache Wicket 9.x + Java 17 + Tomcat + WicketTester)
```

### Stack Profile 1: `mbargo-reporting` (Modern Reactive SPA + Microservices)
* **Location:** `.agents/skills/software-factory/extensions/domain-webapp/stacks/mbargo-reporting/`
* **Architecture:** Angular 21 (Standalone components, Signals, Bootstrap 5) + Play Framework 3 (Java 17 / Scala 3, sbt).
* **Test Tooling:** Jest in `/ui` (`npm test -- --watchAll=false`) and JUnit 5 via `sbt test`.
* **Domain Guard:** Enforces reuse of `shared-export-utils.ts` (adaptive font scaling, base64 stripping, error re-throwing) and billboard.js patch management.

### Stack Profile 2: `mbargo-admin-webtop` (Server-Rendered Java Enterprise)
* **Location:** `.agents/skills/software-factory/extensions/domain-webapp/stacks/mbargo-admin-webtop/`
* **Architecture:** Apache Wicket 9.22.0 + Java 17 LTS + Apache Maven (WAR packaging to Apache Tomcat).
* **Test Tooling:** `WicketTester` + JUnit under `src/test/java/` (`mvn clean install -P test`).
* **Domain Guard:** 1:1 pairing of Java classes and HTML markup with synchronized `wicket:id` bindings; mandatory `IModel<T>` state detachment to prevent session leaks; parameterized SQL Server DAOs.

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
            │   └── pr-template.md                     # Audited PR template (TDD, Skeletons, Previews)
            ├── prompts/
            │   ├── interview-agent.md                 # PO, Epic Decomposer & Vibe Preview Gatekeeper
            │   ├── scrum-master-agent.md              # Interface Architect & Context Optimizer
            │   ├── coding-agent.md                    # Implementer (App code with mandatory reuse)
            │   ├── test-engineer-agent.md             # Independent SDET (Test suites & edge cases)
            │   ├── qa-agent.md                        # QA Gatekeeper (Runner, TDD Certifier, Reuse Guard)
            │   └── git-governance.md                  # Lifecycle, Conventional Commits & Release Rules
            ├── proxy/                                 # 💰 LLM PROXY & COST CONTROLLING
            │   ├── PROXY_ARCHITECTURE.md              # 3-Tier routing & escalation concept
            │   └── templates/
            │       └── model-eval-schema.json         # JSON schema for token costs & QA tracking
            └── extensions/                            # 🚀 MODULAR DOMAIN OVERLAYS (Layer 1)
                └── domain-webapp/
                    ├── EXTENSION.md                   # WebApp architecture & Contract-First doc
                    ├── templates/
                    │   └── api-contract.yaml          # OpenAPI 3.0 Contract Standard
                    ├── prompts/
                    │   ├── frontend-agent.md          # Generic UI, a11y, State, Mock APIs
                    │   └── backend-agent.md           # Generic API Compliance, Security, DB Migrations
                    └── stacks/                        # ⚡ CONCRETE TECH-STACK PROFILES (Layer 2)
                        ├── mbargo-reporting/          # Angular 21 + Play Framework 3 BI Stack
                        │   ├── STACK.md               # Tooling, paths, commands & reuse rules
                        │   ├── templates/
                        │   │   └── kickoff-mbargo-template.md
                        │   └── prompts/
                        │       ├── frontend-agent-mbargo.md
                        │       ├── test-engineer-mbargo.md
                        │       └── backend-agent-play.md
                        └── mbargo-admin-webtop/       # Apache Wicket 9.x + Java 17 + Tomcat Stack
                            ├── STACK.md               # Wicket patterns, Maven profiles & SQL Server
                            ├── templates/
                            │   └── kickoff-webtop-template.md
                            └── prompts/
                                ├── wicket-engineer-agent.md
                                └── test-engineer-webtop.md
```

---

## 🚦 Roles & Responsibilities

| Role | Primary Responsibility | Cardinal Rule |
| :--- | :--- | :--- |
| **Interview Agent** | Product Owner, Epic Decomposer, Preview Gatekeeper | Slices stories to max. 1–3 REQs; obtains human sign-off on staging preview before `main` release. |
| **Scrum Master Agent** | Interface Architect & Context Optimizer | **Publishes Interface Skeletons** before parallel execution; locks dependencies; keeps context <3k tokens. |
| **LLM Proxy & Router** | Cost & Quality Optimization | Start at cheapest tier (Workhorse/Local); dynamically escalate to Tier 1 on failures. |
| **Coding Agent** | Application code implementation | **Follow Skeleton & Reuse First:** Search workspace before creating files; never write own tests. |
| **Test Engineer Agent** | Test suite, AC coverage, edge cases | **Target Skeleton Signatures:** Never write app code; test objectively against the spec. |
| **QA Gatekeeper** | TDD Certifier, Test Runner, Anti-Duplication Guard | **Red-Green TDD:** Confirm tests fail on stubs first, then pass on implementation; verify zero duplicates. |
