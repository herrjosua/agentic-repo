---
title: "Care-Gap Badge & Alert Triage Queue — Status-Indicator Screening"
date: 2026-01-08
status: final
designer: Sam Okafor
tags: ["accessibility", "wcag", "section-508", "components", "care-coordination", "alert-triage"]
related_findings: ["../research/findings/accessibility-cross-cutting.md", "../research/findings/care-coordination-triage.md"]
source_type: native
wcag_level: "AA"
scope: "care-gap-badge and alert-triage-queue status-indicator instances (color-only red/yellow/green dots)"
issues_found: 1
---

## Scope
Targeted WCAG 2.1 AA re-screening of the two live components carrying the color-only status-dot
pattern named as a likely shared root cause in the Nov 2025 cross-cutting accessibility review:
`care-gap-badge` (clinician dashboard) and `alert-triage-queue` (care coordination).

## Issues found
| Issue | WCAG criterion | Severity | Location |
|---|---|---|---|
| Both components render status as color-only dots (red/yellow/green) with no text or pattern alternative — confirmed as the same underlying markup pattern, not just a visual coincidence | 1.4.1 Use of Color | High | `care-gap-badge`, `alert-triage-queue` |

## Recommendations
Confirmed: one shared root cause, not three independent bugs. Fix at the design-system level
rather than patching each surface separately — see
`design-system/v4-1-status-indicator-component.md` for the resulting shared component.

## Related Findings
- [Accessibility (Cross-Cutting)](../research/findings/accessibility-cross-cutting.md)
- [Care Coordination & Alert Triage](../research/findings/care-coordination-triage.md)
