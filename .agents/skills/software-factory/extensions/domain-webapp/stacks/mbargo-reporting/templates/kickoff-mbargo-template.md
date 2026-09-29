# Kick-off: [Story Name] (mbargo Reporting V4)

## 🎯 Goal
[Concise 1-sentence description of feature or fix]

## 📐 Interface Skeleton (Mandatory Contract)
```typescript
// Define exact Angular component/service interface or Play controller signature
export interface TargetExportPayload {
  reportTitle: string;
  period: string;
  data: any[];
}
```

## 🧩 Mandatory Domain Code Reuse (Reuse First!)
* **Shared Export Utilities:** `ui/src/app/services/export/shared-export-utils.ts`
  * Inspect: `computeRankingFontSize`, `stripDataUrlPrefix`, `buildReportTitle`, `resolveChartExports`.
  * **Rule:** Do NOT write duplicate font scalers or slug normalizers!

## 🔒 Hermetic Environment & Constraints
* **Frontend Target Directory:** `/ui/src/app/`
* **Dependency Rule:** `npm install --legacy-peer-deps` (if modifying dependencies).
* **Verification Command:** `cd ui && npm test -- --silent --watchAll=false`
* **Error Propagation:** Re-throw export/file write errors after logging. Never swallow with empty `catch`.
