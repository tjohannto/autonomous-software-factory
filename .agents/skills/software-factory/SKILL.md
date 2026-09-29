---
name: software-factory
description: Domain-agnostic Software Factory based on Spec-Driven Development (SDD), Scrum Task Packaging, LLM Cost Proxy & NovaSmart AI Governance.
---

# Software Factory (Core)

This skill provides the reusable foundation for an autonomous, cost-optimized Software Factory following **Spec-Driven Development (SDD)**, **agile Scrum packaging**, and **four-eyes quality governance**.

## Roles & Agent Prompts

1. **[Interview Agent (Spec Lead)](prompts/interview-agent.md):** Engages with the Vibe Coder (voice/text-ready) and slices epics into actionable user stories (`specs/01-xyz.md`).
2. **[Scrum Master Agent (Task Packager)](prompts/scrum-master-agent.md):** Extracts minimal interface skeletons from existing code, protects context windows (<3,000 tokens), and builds concise **kick-off prompts**.
3. **[Coding Agent (Implementer)](prompts/coding-agent.md):** Implements application code under strict **Reuse-First** rules. Does not write own tests.
4. **[Test Engineer Agent (SDET)](prompts/test-engineer-agent.md):** Independently writes comprehensive automated test suites (including malicious edge cases) derived from acceptance criteria.
5. **[QA Gatekeeper Agent (Runner & Compliance)](prompts/qa-agent.md):** Executes test suites deterministically in a shell sandbox, checks diffs for code duplication (anti-greenfield guard), screens secrets, and approves PRs.
6. **[Git Governance & Standards](prompts/git-governance.md):** Branching rules (`main` <- `dev` <- `feat/*`), Conventional Commits, and PR templates.

## Cost & Model Optimization

* **[LLM-Model Proxy & Cost Router](proxy/PROXY_ARCHITECTURE.md):** Distributes tasks across 3 model tiers (Tier 1: Heavyweight, Tier 2: Workhorse, Tier 3: Utility) with dynamic escalation and cost/quality logging (`proxy/templates/model-eval-schema.json`).

## Autonomous Workflow

```text
               [ Vibe Coder (Voice / Text) ]
                            │
                            ▼
                    [ Interview Agent ]  ◄── (Epic Decomposer: Slices Stories)
                            │
                            ▼ generates
                    [ specs/01-story.md ]
                            │
                            ▼
                  [ Scrum Master Agent ] ◄── (Builds Kick-off Prompt, Protects Context Window)
                            │
                            ▼
                [ LLM Proxy / Cost Router ] (Selects Tier 1 / 2 / 3 per Task)
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
    [ Coding Agent ]             [ Test Engineer Agent ]
    (Reuse First,                (Writes Test Suite & Edge Cases
     Application Code)            independently from Coder)
            │                               │
            └───────────────┬───────────────┘
                            ▼ Handoff to Sandbox
                 [ QA Gatekeeper Agent ] ◄── (1. Run Tests, 2. Anti-Duplication Check)
                            │
       ┌────────────────────┴────────────────────────┐
       ▼ [FAIL: Tests Red OR Duplicates Found]       ▼ [PASS: Tests Green & Reuse OK]
  [ review_feedback.md ]                     [ Audited Pull Request ]
  (Retry with Scrum Master hint,             (PR Template targeting dev branch)
   optional Proxy escalation to Tier 1)              │
                                                     ▼ Squash & Merge
                                              [ dev / Staging ]
```
