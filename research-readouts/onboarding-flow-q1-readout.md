---
title: "Onboarding Flow — Q1 Readout"
date: 2026-02-02
status: final
designer: Sam Okafor
tags: ["onboarding", "readout", "q1", "project-onboarding"]
related_findings: ["onboarding"]
source_type: native
related_analytics: ["onboarding-funnel-dropoff"]
presented_to: ["Product Team", "CX Team"]
---

## Summary
Across all 6 onboarding usability sessions (Jan 19-23, 2026), the most consistently observed
first-time-setup friction is step 3 ("Connect calendar") reading as optional when it's actually
required — 2 of 3 participants in sessions 1-3 attempted to skip it outright, and sessions 4-6
read it as optional in the same way. The funnel summary (`analytics/summaries/onboarding-funnel-dropoff.md`)
reports step 3 as the largest drop-off point, but the underlying export isn't in the repo.

## Key findings
- Step 3's wording implies an optionality it doesn't have — see finding `onboarding`.
- The step 3 drop-off in the funnel summary is consistent with users misreading the step as
  optional; funnel data alone can't show why users drop off.

## Recommendations
1. Relabel step 3 to state plainly that calendar connection is required before later functionality
   works.
2. Give visible feedback that invites (entered in step 4, "Invite your team") aren't sent until
   the whole wizard is submitted — addressing a related hesitation seen in session 3.
3. Retest step 3 specifically once the wording change ships, per `research/findings/onboarding.md`'s
   status note.
