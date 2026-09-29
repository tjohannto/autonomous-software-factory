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
            └── extensions/                            # 🚀 MODULAR DOMAIN OVERLAYS
                └── domain-webapp/
                    ├── EXTENSION.md                   # WebApp architecture & Contract-First doc
                    ├── templates/
                    │   └── api-contract.yaml          # OpenAPI 3.0 Contract Standard
                    ├── prompts/
                    │   ├── frontend-agent.md          # UI, a11y, State, Mock APIs
                    │   └── backend-agent.md           # API Compliance, Security, DB Migrations
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
                                ├── wicket-engineer-agent.md  # HTML/Java pairs, IModel, POI exports
                                └── test-engineer-webtop.md   # WicketTester, DAO & edge-case testing
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

---

## 🗺️ Supported Tech-Stack Profiles

1. **`mbargo-reporting` (Modern SPA + Microservices):**
   * Angular 21 (Standalone components, Signals, Bootstrap 5, Jest in `/ui`).
   * Play Framework 3.0.x (Java 17 / Scala 3, sbt).
   * Strict reuse of `shared-export-utils.ts` and billboard.js patch management.
2. **`mbargo-admin-webtop` (Server-Rendered Java Enterprise):**
   * Apache Wicket 9.22.0 + Java 17 LTS (WAR deployed to Tomcat).
   * Component & Markup pairing (`*.java` + `*.html` with matching `wicket:id`).
   * Memory & state isolation via `IModel<T>` (`LoadableDetachableModel`).
   * Microsoft SQL Server persistence & Apache POI 5.5.1 Excel reporting.
   * Maven build profile verification: `mvn clean install -P test`.
