# Spec: [Feature / Story Name]

## 1. Goal
[1-2 sentences: Which concrete problem are we solving in this story and why?]

## 2. Scope & Story Slicing (User Story Level)
* **In Scope:** [Max. 1-3 cohesive functional requirements]
* **Out of Scope:** [Items deferred to follow-up stories or future epics]

## 3. Existing Code & Code Reuse (Reuse First)
* **Modules to inspect / reuse:** 
  * [e.g. src/utils/formatters.ts, src/components/Button, src/services/auth.service]
* **Refactoring existing components:**
  * [Yes / No - What needs backward-compatible adaptation without breaking existing features?]

## 4. Requirements
Functional business requirements (max. 1–3 per story):
* **REQ-1:** [Business requirement]
* **REQ-2:** [Business requirement]

## 5. Acceptance Criteria (How do we know it is done?)
Directly mapped to requirements — verifiable from a user perspective:
* **For REQ-1:** 
  - [ ] [Visible / testable user behavior]
* **For REQ-2:** 
  - [ ] [Visible / testable user behavior]

## 6. Verification (QA Check)
* **Command:** [e.g., python3 -m unittest discover -s tests -v / npm test]
* **Expected Result:** [All regression tests AND new tests pass, zero linter warnings]

## 7. Security Considerations (see `security/SECURE_CODING.md`)
* **Security-relevant:** [Yes / No — which trigger? e.g. untrusted input, auth, personal data, new dependency]
* **Data handled:** [e.g. none / internal / confidential / personal data]
* **Abuse cases (as testable ACs):**
  - [ ] [e.g. unauthenticated request is rejected with 401 and no data is returned]
  - [ ] [e.g. malformed input is rejected without stack trace or internal paths in the output]
* **Applicable policy (filled by Scrum Master, IDs only):** [e.g. ISREQ-…, guide topic `coding/input_validation/…` — or "Policy guidance: NOT CHECKED (reason)"]
