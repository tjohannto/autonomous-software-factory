# Guide: Git Workflow, Branching & Governance (NovaSmart Standard)

This standard governs how agents execute changes on the codebase. No direct pushes allowed.

---

### 1. BRANCHING STRATEGY & LIFECYCLE (Least Privilege Isolation)

```text
[ main ] (Production)
   ▲
   │ (Release PR: Requires Human Vibe Coder Preview Sign-off!)
[ dev ]  (Staging / Integration)
   ▲
   │ (Feature PR: Requires Red-Green TDD & QA Gatekeeper Sign-off)
[ feat/<story-name> ] (Isolated Agent Workspace)
```

* **`main` (Production):**
  * Mirrors the live production state.
  * **Strict Protection:** Direct push forbidden. Merges only via release PR from `dev` **after explicit human preview sign-off**.
* **`dev` (Integration / Staging):**
  * Central integration branch.
  * **Strict Protection:** Direct push forbidden. Changes enter **only via Pull Request** after QA Gatekeeper certification.
* **`feat/<story-name>` or `fix/<issue-name>` (Agent Workspaces):**
  * Each user story runs on a dedicated, isolated branch.
  * Created automatically once `spec.md` is approved.

---

### 2. QUALITY & AUDIT GATES

1. **Pre-Coding Handshake:** Scrum Master publishes Interface Skeleton to eliminate naming/import mismatches.
2. **Red-Green TDD Audit:** QA Gatekeeper runs tests against stubbed skeleton first. Tests **must fail (RED)** to prove they are not tautological, then pass **(GREEN)** against implementation.
3. **Hermetic Runtime:** No undeclared packages. Dependencies must be locked.
4. **Squash & Merge:** Feature branches are squash-merged into `dev`. This maintains a clean history: 1 commit = 1 verified story.
5. **Vibe Coder Preview Gate:** Interview Agent presents interactive staging preview to human before promoting `dev` to `main`.

---

### 3. CONVENTIONAL COMMITS (Mandatory for All Agents)

Format: `<type>(<scope>): <concise present-tense description>`

* `feat(auth): implement login form validation for REQ-1`
* `test(auth): add unit test for invalid password handling`
* `fix(cart): resolve race condition during stock decrement`
* `docs(spec): add approved specification for password reset`
* `refactor(db): optimize query performance without schema changes`
