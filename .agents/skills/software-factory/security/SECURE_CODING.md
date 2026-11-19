# Secure Coding & Policy Integration

This document defines how the Factory roles apply secure coding guidance and internal security policy
(e.g. ISMS requirements, compliance criteria, audit scope) **while building** (a) and **while reviewing
a pull request** (b).

It is platform-neutral. The policy source is an optional **Policy MCP server** — in Bertelsmann
environments the `secure-coding-isms` MCP (Bertelsmann ISMS policy data + Arvato Systems Secure Coding
Guide, obtained via the API marketplace). Any MCP-capable client (Claude Code, GitHub Copilot, Codex,
JetBrains AI Assistant) can act as the adapter.

> **Not a compliance approval.** Policy-tool results are guidance. They never replace the binding
> sources (Secure Coding Guide, ISMS) or the decision of the responsible human / designated security
> function. No role may claim "compliant" or "approved" based on tool output.

---

## 1. When is a story security-relevant?

The Interview Agent marks a story as security-relevant (spec Section 7) if it touches at least one of:

* Authentication, session handling, authorization / access control, multi-tenancy
* Cryptography, key or secret handling, certificates, randomness
* Input from untrusted sources (HTTP, files, CLI args, queues, LLM output) or output encoding
* Personal or confidential data (storage, transfer, logging, export, deletion)
* Logging, auditing, error handling that may expose internals
* New dependencies, build/CI pipeline, container or infrastructure configuration
* Outbound requests (SSRF), file system paths, deserialization, shell/process execution

If unsure, mark it relevant — the cost is a few tool calls.

---

## 2. Role responsibilities

### (a) Build: secure by design and by implementation

| Role | What it does | Policy tools (if available) |
| --- | --- | --- |
| **Interview Agent** | Fills spec Section 7 (security relevance, data classification, abuse cases as ACs). | — |
| **Scrum Master** | Resolves applicable requirements **once per story** and packages only IDs + short guidance into the kick-off (`🛡️ Security Guidance`). Keeps context small. | `search_requirements` → `get_requirement_with_guides`; `list_guide_topics` / `search_guide` (phases `plan_design`, `coding`) |
| **Coding Agent** | Implements following the referenced guide topics; may look up a specific topic when implementing a sensitive construct. | `get_guide`, `search_guide` |
| **Test Engineer** | Derives negative / abuse-case tests from the security ACs and compliance criteria (e.g. unauthorized access denied, malformed input rejected, no secrets in logs). | `list_compliance_criteria`, `get_guides_for_criteria` (phase `test_release`) |

### (b) Review: pull request security gate

| Role | What it does | Policy tools (if available) |
| --- | --- | --- |
| **QA Gatekeeper** | Keeps the fast deterministic screen (secrets, `eval`, unsafe shell). | — |
| **Security Gatekeeper** | Reviews the PR diff for vulnerabilities with code evidence, maps each finding to policy, checks that the kick-off's security guidance was implemented, and returns a verdict. See [`prompts/security-agent.md`](../prompts/security-agent.md). | `get_data_last_update`, `map_finding_to_policy`, `get_guides_for_cwe`, `get_bam_for_requirement` |

---

## 3. Data minimization (mandatory)

Send the policy server **only the minimum lookup information**:

* ✅ CWE / OWASP IDs, ISREQ / ISCC IDs, short keywords, a finding title, 1–2 neutral sentences.
* ❌ Never source code, diffs, stack traces, file contents, customer or personal data, hostnames,
  internal URLs, credentials, tokens or keys.

---

## 4. Evidence, citation and fallback

* Call `get_data_last_update` once per story/review and record the data date in the artifact.
* Cite IDs (`ISREQ-…`, `ISCC-…`, BAM requirement, guide topic id) — never paraphrase a requirement as
  if it were the binding text.
* **If the policy server or a tool is unavailable:** continue with the code-based analysis and record
  `Policy guidance: NOT CHECKED (<reason>)`. Never imply that policy compliance was verified.
* Tier routing: policy lookups and summaries may run on Tier 2/3; the **security verdict is never made
  by Tier L** (see `proxy/PROXY_ARCHITECTURE.md`).

---

## 5. Credentials for the policy server

The API key is personal (or a CI service key). It must never appear in a repository, prompt, chat,
log or PR.

| Environment | Recommended setup |
| --- | --- |
| Claude Code (local) | `.mcp.json` with `"headersHelper": "<path to script>"`; the script reads the key from the OS keychain (e.g. macOS `security find-generic-password … -w`) and prints `{"x-api-key": "…"}`. Alternative: `"x-api-key": "${ENV_VAR}"`. |
| VS Code / Copilot | `.vscode/mcp.json` with `"x-api-key": "${input:policyApiKey}"` (prompted, stored by VS Code) or `${env:…}`. |
| CI (headless review) | Repository/organization secret, exposed only to the review job's environment; never echoed. |

Repository config files may contain the server name, URL and a **placeholder or helper path only**.

---

## 6. Adapters

The roles above are prompts. A platform adapter wires them to a client:

* **Claude Code:** a subagent (e.g. `.claude/agents/security-gatekeeper.md`) whose tool list is
  restricted to read-only repository tools plus the policy MCP tools; the security-review skill can be
  used for the code analysis and its policy-mapping phase.
* **GitHub Copilot:** reference `prompts/security-agent.md` from the repo's Copilot instructions or a
  custom agent; configure the MCP server in `.vscode/mcp.json`.
* **CI:** a job that runs the Security Gatekeeper headless on the PR diff and posts
  `security_review.md` as a PR comment/artifact. A failing verdict blocks the merge; it never
  auto-approves.

This repository ships the process definition only; no adapter is implemented here.
