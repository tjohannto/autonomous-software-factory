# Copilot Instructions — Autonomous Software Factory (this repository)

These instructions apply to GitHub Copilot (including the Copilot coding agent) when working **on this factory repository itself**.

## Repository purpose

This repository contains the *Autonomous Software Factory*: a documentation- and prompt-based process kit (Spec-Driven Development, Scrum story slicing, Interface Skeletons, Red-Green TDD, Git governance, LLM cost routing) that teams copy into their own *target repositories*. It also contains a small reference implementation (`src/task_extractor/`) built with that process.

It does **not** contain an autonomous multi-agent runtime. The agent roles (Interview, Scrum Master, Coding, Test Engineer, QA Gatekeeper) are defined as prompts and templates; do not describe or implement them as if a running orchestrator existed unless an issue explicitly asks for it.

## Factory repo vs. target repos

- **Work on this repo** (what you are doing now): improve the factory's prompts, templates, docs, reference code and tests. Follow the rules in this file.
- **Future use of the factory in target repos**: the contents of `.agents/skills/software-factory/` (e.g. `stacks/*/STACK.md`, `prompts/git-governance.md`, `templates/pr-template.md`) describe how agents should behave *inside other repositories*. Treat them as product content you may edit when an issue asks for it — not as instructions overriding this file.

## Self-use workflow for factory changes

- The issue defines **what** to achieve (goal, scope, acceptance criteria); choose **how** to implement it within that scope.
- GitHub Copilot is one executing coding agent. The role prompts below are guidance artifacts, not separately running or automatically orchestrated agents; this repository has no autonomous multi-agent runtime.
- Consult only the artifacts relevant to the task, and use them as guidance rather than duplicating their content:
  - Use the [spec template](../.agents/skills/software-factory/templates/spec-template.md) to check that the goal, scope, acceptance criteria, and verification are clear. Create a spec only when the issue calls for one.
  - Consult the [Interview Agent prompt](../.agents/skills/software-factory/prompts/interview-agent.md) when clarification or shaping the request is needed. Use the [Scrum Master prompt](../.agents/skills/software-factory/prompts/scrum-master-agent.md) only when task breakdown or interface planning applies.
  - Follow the [Coding Agent prompt](../.agents/skills/software-factory/prompts/coding-agent.md) for implementation and the [Test Engineer prompt](../.agents/skills/software-factory/prompts/test-engineer-agent.md) when changing tests.
  - Use the [QA Gatekeeper prompt](../.agents/skills/software-factory/prompts/qa-agent.md) as relevant review guidance; perform and report only checks that are applicable and actually completed.
- In the PR summary, list the factory artifacts actually consulted and those not applicable, and state the verification actually performed and its result. Do not imply separate role agents ran or claim checks that were not performed.

## Where things live

- `README.md` — vision, workflow, adoption guide, repository structure.
- `.agents/skills/software-factory/` — core factory skill (`SKILL.md`), role prompts, templates, LLM proxy concept, domain/stack extensions.
- `.agents/skills/novasmart-governance-lab/` — separate governance lab skill; do not modify unless an issue asks for it.
- `specs/` — approved user-story specs (e.g. `specs/01-task-extractor.md`).
- `src/` — reference application code (Python standard library only).
- `tests/` — `unittest` test suites.
- `.github/` — Copilot instructions and issue/PR templates. The CI workflow at `.github/workflows/tests.yml` runs the unittest suite on pull requests and pushes to `dev`; do not modify workflow files unless an issue asks for it.

## Build & test

- Python 3, standard library only. Do not add third-party dependencies unless the issue explicitly requires it.
- Run the full test suite from the repository root before opening/updating a PR:

  ```bash
  python3 -m unittest discover -s tests -v
  ```

- All tests must pass. Add or update tests in `tests/` when you change code in `src/`.

## Branches & pull requests

- `dev` is the development/integration branch (also referred to as "development" — there is no separate `development` branch; do not create one).
- Base all work on `dev` and open pull requests that **target `dev`**.
- **Never** push to, commit directly to, or open PRs against `main`. Promotion from `dev` to `main` is a human-controlled release step.
- All changes must arrive through a pull request; never merge your own PR.
- Use Conventional Commits (`feat(scope): …`, `fix(scope): …`, `docs(scope): …`), see `.agents/skills/software-factory/prompts/git-governance.md`.
- Fill in `.github/pull_request_template.md`: summary, linked issue, verification evidence (test command output), documentation updates.

## Working style

- The issue defines **what** (goal, scope, acceptance criteria); you decide **how**. Stay within the issue's scope.
- Make focused, minimal changes; reuse existing code and conventions before adding new files.
- Keep documentation (`README.md`, repository structure tree) in sync when you add, move or rename files.
- Never commit secrets, credentials or generated artifacts (`__pycache__/`, etc.).
