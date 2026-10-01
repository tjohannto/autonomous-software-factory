# Copilot Instructions — Autonomous Software Factory (this repository)

These instructions apply to GitHub Copilot (including the Copilot coding agent) when working **on this factory repository itself**.

## Repository purpose

This repository contains the *Autonomous Software Factory*: a documentation- and prompt-based process kit (Spec-Driven Development, Scrum story slicing, Interface Skeletons, Red-Green TDD, Git governance, LLM cost routing) that teams copy into their own *target repositories*. It also contains a small reference implementation (`src/task_extractor/`) built with that process.

It does **not** contain an autonomous multi-agent runtime. The agent roles (Interview, Scrum Master, Coding, Test Engineer, QA Gatekeeper) are defined as prompts and templates; do not describe or implement them as if a running orchestrator existed unless an issue explicitly asks for it.

## Factory repo vs. target repos

- **Work on this repo** (what you are doing now): improve the factory's prompts, templates, docs, reference code and tests. Follow the rules in this file.
- **Future use of the factory in target repos**: the contents of `.agents/skills/software-factory/` (e.g. `stacks/*/STACK.md`, `prompts/git-governance.md`, `templates/pr-template.md`) describe how agents should behave *inside other repositories*. Treat them as product content you may edit when an issue asks for it — not as instructions overriding this file.

## Where things live

- `README.md` — vision, workflow, adoption guide, repository structure.
- `.agents/skills/software-factory/` — core factory skill (`SKILL.md`), role prompts, templates, LLM proxy concept, domain/stack extensions.
- `.agents/skills/novasmart-governance-lab/` — separate governance lab skill; do not modify unless an issue asks for it.
- `specs/` — approved user-story specs (e.g. `specs/01-task-extractor.md`).
- `src/` — reference application code (Python standard library only).
- `tests/` — `unittest` test suites.
- `.github/` — Copilot instructions and issue/PR templates. A CI workflow (`.github/workflows/tests.yml`, see README) is added by maintainers; do not create or modify workflow files unless an issue asks for it.

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
