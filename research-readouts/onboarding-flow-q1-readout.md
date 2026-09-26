---
title: "Onboarding Flow — Q1 Readout"
date: 2026-02-02
status: final
designer: Sam Okafor
tags: ["onboarding", "readout", "q1"]
related_findings: ["onboarding"]
source_type: native
related_analytics: ["onboarding-funnel-dropoff"]
presented_to: ["Product Team", "CX Team"]
---

## Summary
Across all 6 onboarding usability sessions (Jan 19-23, 2026), the single largest source of
first-time-setup friction is step 3 ("Connect calendar") reading as optional when it's actually
required — all 3 participants observed in sessions 1-3 paused there, and 2 of 3 attempted to skip
it outright. This is independently corroborated by the Jan 2026 funnel export, which shows step 3
as the largest drop-off point in the wizard.

## Key findings
- Step 3's wording implies an optionality it doesn't have — see finding `onboarding`.
- The drop-off isn't task difficulty; it's users not realizing the step is required and exiting
  rather than completing it (funnel data, `analytics/summaries/onboarding-funnel-dropoff.md`).
- The sidebar progress indicator is present but effectively unused — no participant referenced it
  unprompted across any of the 6 sessions.

## Recommendations
1. Relabel step 3 to state plainly that calendar connection is required before later functionality
   works.
2. Give visible feedback that invites (entered in step 4) aren't sent until the whole wizard is
   submitted — addressing a related hesitation seen in sessions 4-6.
3. Retest step 3 specifically once the wording change ships, per `research/findings/onboarding.md`'s
   status note.
