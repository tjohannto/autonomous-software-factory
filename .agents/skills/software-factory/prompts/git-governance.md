# Leitfaden: Git-Workflow, Branching & Governance (NovaSmart-Style)

Dieser Standard regelt, wie Agenten Änderungen am Codebase durchführen. Niemand committet unkontrolliert.

---

### 1. BRANCHING-STRATEGIE (Least Privilege Isolation)

* **`main` (Production):**
  * Spiegelt den aktuellen Stand auf Live/Prod wider.
  * **Strikter Schutz:** Direct Push verboten. Merges nur via Release-PR aus `dev`.
* **`dev` (Integration / Staging):**
  * Zentraler Entwicklungszweig.
  * **Strikter Schutz:** Direct Push verboten. Änderungen gelangen **nur via Pull Request** hierher.
* **`feat/<feature-name>` oder `fix/<issue-name>` (Agent Workspaces):**
  * Jeder Feature-Auftrag erhält einen dedizierten, isolierten Branch.
  * Wird automatisch vom Coding Agent erzeugt, sobald die `spec.md` approved ist.

---

### 2. CONVENTIONAL COMMITS (Pflicht für alle Agenten)

Jeder Commit muss maschinenlesbar, präzise und rückverfolgbar sein:

Format: `<type>(<scope>): <kurze beschreibung im präsens>`

* `feat(auth): implement login form validation for REQ-1`
* `test(auth): add unit test for invalid password handling`
* `fix(cart): resolve race condition during stock decrement`
* `docs(spec): add approved specification for password reset`
* `refactor(db): optimize query performance without schema changes`

---

### 3. PULL REQUESTS & AUDIT LOGGING (NovaSmart Learnings)

1. **Kein PR ohne Spec-Referenz:** Jeder PR muss auf eine existierende `specs/<feature-name>.md` verweisen.
2. **Kein Merge ohne QA-Sign-off:** Ein PR darf erst gemergt werden, wenn der QA Agent das Siegel `[STATUS: VERIFIED]` vergeben hat.
3. **Squash & Merge:** Feature-Branches werden beim Merge in `dev` "gesquasht". Das garantiert eine saubere Historie: 1 Commit = 1 vollständiges, verifiziertes Feature.
4. **Secret & Safety Screening:** Vor dem Commit prüft der Agent (oder die Pre-Commit-Hook), dass keine Tokens, privaten Keys oder Debug-Backdoors im Diff enthalten sind.
