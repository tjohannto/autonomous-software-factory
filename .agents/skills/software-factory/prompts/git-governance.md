# Guide: Git Workflow, Branching & Governance (NovaSmart Standard)

This standard governs how agents execute changes on the codebase. No direct pushes allowed.

---

### 1. BRANCHING STRATEGY (Least Privilege Isolation)

* **`main` (Production):**
  * Mirrors the current live production state.
  * **Strict Protection:** Direct push forbidden. Merges only via release PR from `dev`.
* **`dev` (Integration / Staging):**
  * Central integration branch.
  * **Strict Protection:** Direct push forbidden. Changes enter **only via Pull Request**.
* **`feat/<story-name>` or `fix/<issue-name>` (Agent Workspaces):**
  * Each user story runs on a dedicated, isolated branch.
  * Created automatically once `spec.md` is approved.

---

### 2. CONVENTIONAL COMMITS (Mandatory for All Agents)

Every commit must be machine-readable, precise, and traceable:

Format: `<type>(<scope>): <concise present-tense description>`

* `feat(auth): implement login form validation for REQ-1`
* `test(auth): add unit test for invalid password handling`
* `fix(cart): resolve race condition during stock decrement`
* `docs(spec): add approved specification for password reset`
* `refactor(db): optimize query performance without schema changes`

---

### 3. PULL REQUESTS & AUDIT LOGS (NovaSmart Learnings)

1. **No PR Without Spec Reference:** Every PR must link to an existing `specs/<story-name>.md`.
2. **No Merge Without QA Sign-off:** A PR may only merge when QA Gatekeeper outputs `[STATUS: VERIFIED]`.
3. **Squash & Merge:** Feature branches are squash-merged into `dev`. This maintains a clean history: 1 commit = 1 verified story.
4. **Secret & Safety Screening:** Pre-commit checks ensure no tokens, keys, or debug backdoors are included in diffs.
