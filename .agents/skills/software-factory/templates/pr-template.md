## 📝 Summary
Concise summary of changes (2–3 clear sentences).

## 🎯 Spec Reference
* **Spec File:** `specs/[story-name].md`
* **Status:** Approved by Interview Agent (DoR fulfilled)

## 📐 Interface Skeleton & Contracts
- [x] **Skeleton Followed:** Coding Agent and Test Engineer implemented strictly against the pre-agreed signatures.
- [x] **No Naming Mismatches:** Function/method names and type definitions are 100% aligned.

## 🧪 Red-Green TDD & QA Certification
- [x] **Stage 1 (RED Verified):** Test suite was proven valid by failing on empty/stubbed skeleton (no tautological tests).
- [x] **Stage 2 (GREEN Verified):** All tests passed against implementation (Exit Code 0).
- [x] **Test Report:** `[X]` tests executed, `0` failures.
- [x] **Regression Guard:** All existing regression test suites continue to pass.

## ♻️ Code Reuse & Maintainability
- [x] **Reuse-First Verified:** Existing modules, utilities, and components reused.
- [x] **Anti-Greenfield Guard:** No redundant helper functions created.

## 🔒 Security & Hermetic Runtime
- [x] **Hermetic Dependencies:** No undeclared or unpinned third-party packages introduced.
- [x] **Secret Screening:** No API keys, credentials, or insecure patterns in diff.
- [x] **Scope Guard:** All "Out of Scope" items strictly respected.

## 🛡️ Security Review (Security Gatekeeper)
* **Security-relevant story:** [Yes / No — spec Section 7]
* **Verdict:** [SECURITY_VERIFIED / SECURITY_FAILED / HUMAN_DECISION_REQUIRED] — report: `security_review.md`
* **Policy data date:** [date — or "Policy guidance: NOT CHECKED (reason)"]
- [ ] **Guidance implemented:** All `🛡️ Security Guidance` rules and abuse-case ACs implemented and tested.
- [ ] **Open findings:** None ≥ Medium, or human risk decision recorded: [link]
* *Policy references are guidance, not a compliance approval.*

## 🎨 Vibe Preview (Staging Verification)
* **Preview Command / URL:** `[e.g., python3 -m src.task_extractor.cli sample.md --json]`
* **Vibe Coder UX Sign-off:** [ ] Pending / [x] Approved for Production Release
