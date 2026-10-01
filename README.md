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

## 🚀 How to Use: Integrating into Existing Repositories

You can integrate this Software Factory into any existing repository in two ways: **manually** or **via an AI-driven bootstrap prompt**.

---

### Option A: Manual Integration (Step-by-Step)

Follow these steps to equip any existing codebase with the factory:

#### Step 1: Copy the Factory Skill
Copy the `.agents/` folder from this repo into your target project:
```bash
cp -r /path/to/autonomous-software-factory/.agents /path/to/your-repo/
```

#### Step 2: Initialize Governance Directories & Branches
Ensure your repository has integration branches and operational folders:
```bash
cd /path/to/your-repo

# Create required factory directories
mkdir -p specs tasks logs

# Ensure dev and main branches exist
git checkout -b dev
git push -u origin dev
```

#### Step 3: Pick or Create Your Tech-Stack Profile
* If your project is an **Angular 21 + Play 3** app, activate:  
  `.agents/skills/software-factory/extensions/domain-webapp/stacks/mbargo-reporting/`
* If your project is an **Apache Wicket 9 + Java 17** app, activate:  
  `.agents/skills/software-factory/extensions/domain-webapp/stacks/mbargo-admin-webtop/`
* **For a new stack:** Duplicate one of the stack folders, rename it, and adjust `STACK.md` with your build commands (e.g. `npm test`, `pytest`, `cargo test`) and existing utility paths for "Reuse-First".

#### Step 4: Run Your First Story
Start by calling the **Interview Agent** with your feature idea or voice transcript.

---

### Option B: Prompt-Driven Integration (Zero-Touch AI Bootstrap)

Open your AI assistant (Antigravity, Cursor, GitHub Copilot, or Claude Code) inside your existing repository and paste the following bootstrap prompt:

````markdown
You are now adopting the "Autonomous Software Factory" architecture into this repository.

Follow these bootstrapping steps:
1. **Analyze Tech Stack:**
   - Detect the languages, frameworks, package managers, and build tools in this workspace.
   - Locate the test runners and the exact verification commands (e.g., `npm test`, `pytest`, `mvn test`).
2. **Catalog Reusable Modules (Anti-Greenfield Guard):**
   - Identify existing shared utilities, base components, database access layers, and API clients.
   - List them explicitly as mandatory "Reuse-First" modules.
3. **Install Factory Assets:**
   - Clone or copy `.agents/skills/software-factory` into `.agents/skills/software-factory`.
   - Create a dedicated stack profile under `.agents/skills/software-factory/extensions/domain-webapp/stacks/<detected-stack>/`:
     - `STACK.md`: Set commands, paths, and package manager constraints.
     - `prompts/`: Tailor coder and SDET prompts to match local conventions.
     - `templates/kickoff-<stack>-template.md`: Interface skeleton template.
4. **Git Hygiene & Verification:**
   - Check if `dev` branch exists; create it if missing.
   - Create `specs/`, `tasks/`, and `logs/` directories.
5. **Report Readiness:**
   - Print a summary of the detected stack, verification commands, and reusable modules.
   - Signal: `[FACTORY_READY] The Autonomous Software Factory is active. Tell me what feature to build!`
````

---

### Daily Feature Lifecycle (How You Work With It)

Once installed, your day-to-day workflow looks like this:

1. **Ideation:** Tell the Interview Agent: *"I want to add CSV export to the customer dashboard."*
2. **Scrum Slicing:** The Interview Agent asks 1–2 clarifying questions and writes `specs/02-csv-export.md`.
3. **Task Packaging:** The Scrum Master defines the Interface Skeleton in `tasks/kickoff-csv-export.md`.
4. **Autonomous Parallel Work:**
   * The **Coding Agent** implements the feature on `feat/02-csv-export` using existing export utils.
   * The **Test Engineer (SDET)** writes independent tests covering edge cases.
5. **Automated QA Gate:** 
   * QA verifies **Red-Green TDD** (tests fail on empty stubs first, then pass on implementation).
   * QA inspects git diff for duplicate code and secret leaks.
6. **Preview & Release:** 
   * QA squash-merges into `dev`.
   * The Interview Agent presents an interactive preview / CLI demo to you.
   * You say: *"Looks great, ship it!"* $\rightarrow$ Release PR merges into `main`.

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

## 🤖 Using GitHub Copilot on this Factory Repo

This section is about contributing to **this factory repository itself** with the GitHub Copilot coding agent. It is separate from using the factory in your *target* repositories (see "How to Use" above). The factory roles described in this README are prompts and templates — this repository does not ship an autonomous multi-agent runtime.

### Repository files

| File | Purpose |
| :--- | :--- |
| `.github/copilot-instructions.md` | Repository instructions for Copilot: purpose, doc locations, test command, `dev`-only PRs. |
| `.github/ISSUE_TEMPLATE/factory-change.yml` | Issue form: problem/goal, scope, acceptance criteria, context, verification. |
| `.github/pull_request_template.md` | PR checklist: summary, linked issue, verification evidence, doc updates. |
| `.github/workflows/tests.yml` *(to be added by a maintainer, see below)* | Runs `python3 -m unittest discover -s tests -v` on PRs targeting `dev` and pushes to `dev` (read-only token). |

### Prerequisites (maintainer / admin settings)

These files do **not** by themselves make Copilot available, and nothing here merges pull requests automatically. A maintainer must ensure:

1. **Copilot plan with coding agent access** — a paid Copilot plan (Pro, Pro+, Business or Enterprise). For Business/Enterprise, an organization/enterprise admin must enable the Copilot coding agent policy; it is off by default there.
2. **Repository not opted out** — the coding agent must be allowed for this repository (repository/organization Copilot settings).
3. **`dev` branch protection (recommended)** — in repository settings, protect `dev` and `main` (require PRs and human review); on `dev`, once the workflow below exists, also require the `unittest` status check. These are GitHub settings, not files in this repo.
4. **CI workflow** — create `.github/workflows/tests.yml` on `dev` (via a PR) with the content below. Automated agents typically lack the `workflows` permission needed to add workflow files, so a maintainer adds it:

   ```yaml
   name: Tests

   on:
     pull_request:
       branches: [dev]
     push:
       branches: [dev]

   permissions:
     contents: read

   jobs:
     unittest:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: actions/setup-python@v5
           with:
             python-version: "3.12"
         - name: Run unittest suite
           run: python3 -m unittest discover -s tests -v
   ```

5. **Workflow approval** — by default GitHub requires a user with write access to approve before Actions workflows run on Copilot-authored PRs; use the "Approve and run workflows" button on the PR.

Exact menu names and defaults may change; see the GitHub Docs for the Copilot coding agent for the current settings.

### Issue → Agent → PR flow

1. **Define the "what":** open an issue with the *Factory repository change* form (goal, scope, acceptance criteria, verification). Leave the "how" to the agent.
2. **Assign Copilot:** assign the issue to Copilot (or start a task from the Agents panel) and select **`dev` as the base branch**. If `dev` is not the repository's default branch, Copilot otherwise starts from the default branch — check the base before starting.
3. **Agent works:** Copilot creates its own branch from `dev`, follows `.github/copilot-instructions.md`, runs the test suite and opens a (draft) PR targeting `dev`.
4. **Review:** approve the CI run if prompted, review the diff and the PR template evidence, and request changes via PR comments mentioning `@copilot`.
5. **Merge (human):** a maintainer merges into `dev`. Promotion from `dev` to `main` remains a separate, human-approved release step. Never target `main` directly.

---

## 📁 Repository Structure

```text
.
├── README.md                                          # System documentation
├── .github/
│   ├── copilot-instructions.md                        # Copilot coding-agent instructions for this repo
│   ├── ISSUE_TEMPLATE/factory-change.yml              # Issue form for factory-repo changes
│   ├── pull_request_template.md                       # PR template (summary, issue, evidence, docs)
│   └── workflows/tests.yml                            # CI: unittest suite for PRs/pushes to dev (not yet present; maintainer adds it)
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
