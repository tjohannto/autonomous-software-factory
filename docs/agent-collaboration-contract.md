# Agent Collaboration Contract

This document defines a platform-neutral target contract for collaboration on an
Epic and its dependent Work Packages (WPs). It specifies responsibilities,
artifacts, handoffs, triggers, and gates; it is not an orchestrator, execution
engine, configuration schema, or claim that the Factory currently starts
separate role agents.

## 1. Contract principles and local policy

The following are invariant contract principles:

- Work begins from an approved goal and bounded scope, not an inferred task.
- Roles act only on the exact, approved artifact versions named in their
  handoff. A role may not silently expand scope or change another role's
  responsibility.
- Every handoff identifies its sender, recipient, trigger, inputs, requested
  outputs, scope, non-goals, success criteria, permissions, and stop/escalation
  conditions.
- Decisions and state changes are recorded against the artifact versions they
  approve. A changed artifact invalidates approvals that depended on its old
  version.
- Dependencies must be satisfied before a WP starts. Independent WPs may run
  concurrently only after their shared contracts are approved.
- A failed gate does not advance state. Only the designated approver can accept
  a gate; a role's completion message is not approval.
- The platform used to store issues, documents, code, or status does not define
  the process. A platform adapter may represent the states and approvals, but
  must preserve these principles.

Each Factory-using repository may tune policy parameters, but may not weaken
the principles above. At minimum, local policy records:

| Policy choice | Default if the consuming repository has not specified one |
| --- | --- |
| Maximum rework retries per failed gate | 3 retries after the first failed attempt; then stop and escalate. |
| Gates requiring a human approver | Human approval of the Epic charter before CREATE, material scope changes before work resumes, and final release/acceptance. |
| High-impact or sensitive changes | Require an explicit human approver before implementation and before release. |
| WP sizing threshold | One cohesive, independently verifiable outcome with no more than 1–3 functional requirements; split only when the work has a real boundary or dependency. |

The consuming repository can record these choices in its repository-owned
Factory adoption policy/profile, for example under
`.agents/skills/software-factory/` or `docs/`. The exact location and format are
repository decisions; this contract does not define a configuration schema or
require a runtime to read one. The policy should name retry counts by gate or
role if they differ, identify which approval gates are human-only, name
approver roles, define any risk/scope thresholds, and record the selected
defaults or explicit alternatives. If no local policy exists, use the defaults
above and do not infer permission to skip a human gate.

## 2. Work hierarchy and scope boundaries

- **Epic:** A user or business outcome that is too broad to implement and verify
  as one unit. It defines the outcome, affected users, success measures,
  constraints, and explicit non-goals.
- **Work Package:** A cohesive, bounded deliverable that can be implemented,
  reviewed, and accepted on its own. Each package has its own requirements,
  acceptance criteria, permitted changes, verification, and dependencies.
- **Dependency:** A named artifact or accepted outcome that a downstream WP
  requires. A dependency is not satisfied by an informal message; the specified
  upstream output must be reviewed and accepted.

Avoid **over-fragmentation**: do not make a WP for each file, function, tiny
edit, or role handoff. Group work that shares one cohesive outcome and can be
verified together. Avoid **unbounded scope**: do not put multiple unrelated
outcomes, unbounded cleanup, or unresolved architectural choices into one WP.
Split when a package has independently useful outcomes, distinct acceptance
criteria or owners, or a dependency that can be made explicit. If a package
cannot be bounded without inventing missing requirements, stop and return it
for clarification rather than splitting speculatively.

## 3. Roles and permission boundaries

| Role | Responsibility and permitted work | Must not |
| --- | --- | --- |
| Human Product Owner / maintainer | Owns the intended outcome, approves the Epic charter and material scope changes, resolves product questions, and records release/acceptance decisions. | Delegate the accountability for required human decisions to an agent. |
| Interview Agent | Elicits missing user context, drafts the Epic and acceptance outcomes, and presents the final verified result for human acceptance. | Approve its own draft or infer approval from silence. |
| Scrum Master | Decomposes the approved Epic into dependent WPs, defines interfaces, dependency order, context selection, and handoff packets. | Change approved requirements or start workers on an unapproved/ambiguous package. |
| Test Engineer | Derives independent tests and verification cases from the approved requirements and interfaces; returns test artifacts and results. | Change application code or weaken acceptance criteria to make tests pass. |
| Coding Agent | Implements only the assigned WP against its approved contract and returns the implementation and verification evidence requested. | Write or alter acceptance criteria, approve its own work, or take out-of-scope actions. |
| QA Gatekeeper | Independently checks the requested evidence against acceptance criteria, verification policy, security/reuse constraints, and scope; returns a pass or actionable failure report. | Repair the work it is reviewing or waive a failed gate. |
| Human release owner | Makes the configured human-only final acceptance/release decision after required evidence and approvals exist. This may be the Product Owner or maintainer. | Treat a green automated check as release authorization. |

One person or tool may perform more than one role in a small repository, but
approval must still be attributable to the required approver, and independent
review must not be represented as independent if the same worker produced both
the change and its review.

## 4. Versioned artifacts and handoff envelope

Artifacts are durable records, not just conversation history. At minimum, an
Epic produces a charter and dependency map. Each WP produces a package brief,
approved interface/contract where applicable, test/verification plan,
implementation, and QA decision. A finalization record captures the accepted
versions and release decision.

Every artifact has a stable identifier, version (or immutable revision such as
a commit), owner, state, and links to its parent and dependencies. Do not
overwrite an approved version in place: publish a new version, state what
changed, and identify which downstream handoffs or approvals must be repeated.
Handoffs name exact artifact versions rather than referring to “latest”.

Each role handoff contains:

1. Sender, receiving role, requested action, trigger, and reason.
2. Approved context manifest: only the relevant Epic/WP artifacts, interfaces,
   source paths, and prior decisions needed for this action. Exclude unrelated
   private data, credentials, broad logs, and unapproved instructions.
3. Exact input artifact IDs and versions, including dependency outputs and
   their acceptance state.
4. Expected output artifacts, format/location as selected by the repository,
   and what the receiver must return if blocked.
5. In-scope changes and allowed resources/paths; explicit non-goals and
   forbidden actions.
6. Measurable success criteria and the repository's verification commands or
   evidence requirements.
7. Permission boundary, retry budget, stop conditions, escalation contact or
   role, and any approval required to continue.

A receiver acknowledges the named inputs and scope before acting. If an input
is absent, stale, contradictory, or outside its approved context, the receiver
returns a blocker instead of guessing.

## 5. Triggers and state transitions

These are process triggers, not platform-specific events. A repository may
implement them with its chosen tools, but a status change alone is not proof
that a role actually ran or produced its required output.

| State / trigger | Who starts the role and when | Required output and transition condition |
| --- | --- | --- |
| **INTAKE → PLAN**: a human submits an idea or requests a change | The Human Product Owner starts the Interview Agent to clarify the outcome and why it matters. | Draft Epic charter: outcome, success measures, constraints, non-goals, and open questions. Missing material context returns to INTAKE. |
| **PLAN**: charter is complete enough for decomposition | The Interview Agent hands the draft to the Scrum Master; the human Product Owner starts/approves planning. | Scrum Master returns a versioned WP map with dependencies, package briefs, interfaces, acceptance criteria, and estimated bounded scope. Human approval of the Epic charter and plan moves it to READY. |
| **READY → CREATE**: an individual WP and all prerequisite outputs are approved | The Scrum Master sends the package handoff. The Test Engineer and Coding Agent are started for that WP; they may work in parallel only after shared interfaces and scope are frozen. | Test Engineer returns tests/verification cases; Coding Agent returns scoped implementation and run evidence. Any interface or requirement change returns to PLAN for approval. |
| **CREATE → REVIEW**: required WP outputs are submitted | The Scrum Master requests QA review only after both implementation and test/verification artifacts are identified by version. | QA returns a versioned decision and evidence. Pass moves the WP to ACCEPTED; failure returns it to CREATE with specific remediation. |
| **REVIEW → CREATE**: QA reports a remediable failure | QA starts the bounded rework handoff to the responsible Coding Agent or Test Engineer, with failed criteria and prior attempt number. | A new artifact version and evidence are returned for review. Exhausting the retry budget moves the WP to BLOCKED and escalates to a human. |
| **ACCEPTED → FINALIZE**: every required WP is accepted and dependencies are reconciled | The Scrum Master assembles the final evidence; the Interview Agent presents the outcome to the human release owner. | Finalization record lists accepted WP/artifact versions, acceptance criteria results, unresolved risks, and requested release decision. Required human acceptance authorizes release; rejection returns to PLAN or CREATE with the decision recorded. |

State names are canonical process concepts. A platform may use different
labels, but it must preserve the transitions and evidence. A failed check,
missing approval, or unresolved dependency never advances state.

## 6. PLAN / CREATE / REVIEW / FINALIZE gates

| Phase | Required participants | Gate to leave the phase |
| --- | --- | --- |
| **PLAN** | Interview Agent, Scrum Master, Human Product Owner | Approved Epic charter; bounded WPs; explicit dependencies; acceptance criteria and non-goals; named owners; available interfaces/context; risk and verification plan; recorded human approval. |
| **CREATE** | Coding Agent and Test Engineer for each ready WP; Scrum Master coordinates dependencies | Work stays within the approved package; required implementation and independent tests/evidence exist; outputs identify their input versions; blockers and scope changes are reported instead of absorbed. |
| **REVIEW** | QA Gatekeeper; relevant worker for remediation; configured human approver when a policy gate requires one | Every criterion is demonstrably met; repository-required tests/checks pass; scope, security, and dependency constraints are satisfied; failure reports name evidence and corrective action. QA cannot waive failed criteria. |
| **FINALIZE** | Scrum Master assembles evidence; Interview Agent presents; Human release owner decides | All required WPs and dependencies are accepted; final acceptance criteria and unresolved risks are visible; the configured human release/acceptance decision is recorded against exact versions. Only then is release/closure authorized. |

An adapter may automate repeatable checks, collect evidence, or notify the next
role. It must not convert an unperformed prompt instruction into a completed
role, equate a requested assignment with execution, or let an automated status
stand in for a required human approval.

## 7. Retries, stop conditions, and escalation

- A failed gate returns a structured report: gate and attempt number, artifact
  versions reviewed, failed criterion, concise evidence, specific responsible
  role, and the next requested output.
- The default budget is three rework retries per failed gate after its first
  failure. A retry must address the stated failure and produce a new version;
  repeating an unchanged attempt does not reset the budget.
- The receiving repository may set a smaller or larger local retry budget by
  gate/role in its policy. It must define counting and escalation. A missing
  value uses the default; an exhausted budget always pauses for human review.
- Stop immediately for unclear or contradictory requirements, missing approval,
  unsafe/unauthorized action, suspected secret exposure, broken dependency
  contract, or proposed material scope change. Do not retry around a permission
  or approval boundary.
- On stop, preserve current artifacts, mark the affected WP BLOCKED, report the
  reason and decision needed to the designated human, and wait. Resume only
  from a recorded decision and updated/confirmed artifact version.
- Human escalation is also required when retries are exhausted, the required
  context cannot be safely supplied, criteria cannot be verified, or a risk
  cannot be resolved within the approved scope.

## 8. Worked example: account data export

**Epic E-EXPORT (approved charter, version 1):** Account owners can download a
CSV of their own records. Success means an authorized owner can retrieve the
specified records in a spreadsheet-compatible CSV; unauthenticated and
cross-account access is denied. **Out of scope:** scheduled exports, admin
exports, and formats other than CSV. The human Product Owner approves this
outcome and scope before CREATE.

| WP | Bounded outcome and acceptance | Dependency and handoff |
| --- | --- | --- |
| **WP-1: Export service and authorization** | Define and implement the CSV export service for the approved record fields. Verify owner-only authorization, empty-result behavior, and the agreed CSV encoding/headers. Do not build a user interface or add scheduling. | Starts from E-EXPORT v1. Scrum Master publishes the service interface and field contract. Coding Agent and Test Engineer return implementation and independent tests; QA accepts only with service/authorization evidence. WP-1 outputs an accepted, versioned API/interface contract for WP-2. |
| **WP-2: Account download control** | Add the account-page action that invokes the accepted WP-1 contract and downloads the CSV; verify success, empty results, and visible failure behavior. Do not add new export formats or change the service's field/authorization contract. | Depends on WP-1's accepted interface and authorization behavior. It cannot start CREATE until those exact output versions are approved. If a contract change is needed, return to PLAN and reapprove the affected package(s). |

These are two substantial, separately verifiable deliverables with an explicit
service-to-interface dependency, not a package per source file. Conversely,
the Epic does not silently include scheduling, admin access, other formats, or
unbounded account-data cleanup. A further package is created only if a
separately valuable in-scope requirement is approved, not merely to distribute
small edits across more roles.

## 9. Factory repository status and inspected guidance

Status labels distinguish existing repository behavior from the contract's
intended use:

- **Implemented in this Factory repository:** the small reference application
  extracts open Markdown tasks and provides a CLI, with a `unittest` suite.
  These are working code, not collaboration orchestration:
  [extractor](../src/task_extractor/extractor.py),
  [CLI](../src/task_extractor/cli.py), and
  [tests](../tests/test_task_extractor.py).
- **Prompt/documentation-only:** the Factory's role descriptions, suggested
  steps, and gates are guidance artifacts, not separately running agents.
  Inspected sources include the [Factory README](../README.md),
  [Copilot self-use instructions](../.github/copilot-instructions.md),
  [core skill](../.agents/skills/software-factory/SKILL.md),
  [spec template](../.agents/skills/software-factory/templates/spec-template.md),
  [Interview prompt](../.agents/skills/software-factory/prompts/interview-agent.md),
  [Scrum Master prompt](../.agents/skills/software-factory/prompts/scrum-master-agent.md),
  [Coding prompt](../.agents/skills/software-factory/prompts/coding-agent.md),
  [Test Engineer prompt](../.agents/skills/software-factory/prompts/test-engineer-agent.md),
  [QA prompt](../.agents/skills/software-factory/prompts/qa-agent.md),
  [Git governance guide](../.agents/skills/software-factory/prompts/git-governance.md),
  and [PR template](../.agents/skills/software-factory/templates/pr-template.md).
- **Target state:** this collaboration contract describes the desired common
  process. No state machine, handoff executor, policy parser, workflow
  generator, multi-agent runtime, or collaboration-specific configuration
  schema is implemented here.

Platform-specific forms, comments, assignments, workflow events, and CI checks
are adapter choices, not the portable process definition. This document does
not prescribe or implement any such adapter.
