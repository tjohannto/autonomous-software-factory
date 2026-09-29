# Tech-Stack Profile: mbargo Reporting (V4)

This stack profile specializes the `domain-webapp` overlay for the **mbargo Reporting V4** application. It provides concrete toolchains, execution paths, environment constraints, and domain-specific code-reuse policies.

---

## 🏗️ Architecture & Versions

* **Frontend:**
  * **Framework:** Angular 21 (currently 21.1.x)
  * **Architecture:** Standalone components, Dependency Injection (`inject()`), Signals, lazy loading.
  * **Styling & UI:** Bootstrap 5.x + ng-bootstrap (`^20.0.0` - requires `--legacy-peer-deps`).
  * **Charts & Customizations:** billboard.js with custom legend padding patched via `npx patch-files@latest <file-path>`.
  * **Test Suite:** Jest (`cd ui && npm test`).
  * **Workspace Root:** `/ui` (Node 20+ recommended, npm).
* **Backend:**
  * **Framework:** Play Framework 3.0.x
  * **Languages:** Java 17 LTS, Scala 3.3.x
  * **Architecture:** MVC, async & stateless; Routes -> Controllers -> JSON; Twirl templates.
  * **Test Suite:** JUnit 5 (`sbt test`).
  * **Build Tool:** sbt 1.10.x.
  * **Workspace Root:** `/app`, `/conf`, `/project`.
* **Distribution:**
  * `sbt dist` bundles both the Play backend and the production Angular build (emitted into `/public`).

---

## 🔒 Hermetic Environment & Commands

| Stage | Command | Directory | Notes |
| :--- | :--- | :--- | :--- |
| **Frontend Dependencies** | `npm install --legacy-peer-deps` | `/ui` | Mandatory flag until ng-bootstrap ships native Angular 21 support. |
| **Frontend Verification** | `npm test -- --silent --watchAll=false` | `/ui` | Jest headless runner. |
| **Backend Verification** | `sbt test` | Root | JUnit 5 test execution. |
| **Billboard.js Patches** | `npx patch-files@latest <file-path>` | `/ui` | Re-apply or refresh patches when billboard styling changes. |

---

## ♻️ Mandatory Domain Code-Reuse: `shared-export-utils.ts`

Any task dealing with reports, exports (PPTX, PDF, Images), or tables **MUST** inspect and reuse:
`ui/src/app/services/export/shared-export-utils.ts`

### Key Utilities:
* `stripDataUrlPrefix(dataUrl)`: Defensive base64 payload extraction from `data:*;base64,` strings.
* `slug(text)`: Deterministic NFKD + underscore normalization with length cap (default 60 chars).
* `decideSmoothing(type)`: Canonical heuristic for canvas smoothing (`auto` => `LINE|AREA|GAUGE`).
* `computeRankingFontSize(lines, availableHeight)`: Adaptive font scaling (proportional + 0.5pt refinement) ensuring ranking tables shrink text down to 4pt minimum instead of truncating rows (header always retained).
* `buildReportTitle(title, period)`: Canonical title formatting `<title> (<period>)` used by both PDF and PPTX exporters.
* `getLogoElement() / computeLogoDimensions()`: Shared, null-safe logo resolution and aspect-ratio sizing.
* `resolveChartExports(charts)`: Unified `Promise.all` orchestration and export error propagation.
* `collectChartSizes()`: Shared chart-size collection for generic PDF/PPTX chart export flows.
* `collectRankingRows() / applyTopN() / mergeRowsPreserveOrder()`: Shared ranking table row partitioning and Top-N logic.
* `ExportHelperService.buildOutputFilename(reportTitle, extension)`: Centralized output filename construction.

### Hardened Error Rule:
* **Never swallow file write or export errors.** Failures must be logged and re-thrown (`throw error`) so the UI can surface actionable error alerts to the user.
