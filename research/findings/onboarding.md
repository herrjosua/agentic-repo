---
title: Onboarding flow — setup step confusion
date: 2026-02-03
type: synthesis
status: synthesized
researcher: Priya Patel
tags: [onboarding, project-onboarding]
related_components: []
related_findings: []
related_analytics: [onboarding-funnel-dropoff]
---

## Summary
New admins hesitate at, or attempt to skip, step 3 of the onboarding wizard
("Connect calendar") because its wording implies the step is optional, when
it's actually required for later functionality. This is the largest single
source of friction in first-time setup.

A separate, related hesitation sits at step 4 ("Invite your team"): admins
aren't sure whether invites send immediately or only when the wizard is
submitted.

## Step numbering
Steps are numbered per `user-flows/onboarding-flow.md`, where Signup is step 1:
1 Signup, 2 Basics, 3 Connect calendar, 4 Invite your team, 5 Preferences,
6 Review & finish. Some early records counted from the first step after
Signup — session 2's raw notes call the calendar step "step 2", and the
sessions 1–3 topline originally called the invite step "step 3". Those refer
to the same steps as above: step 3 is always "Connect calendar", and step 4 is
always "Invite your team".

## Evidence
Sourced from `raw/2026-01-19-onboarding-usability-test/` — 6 participants,
moderated usability sessions, Jan 19–23 2026. In sessions 1–3, 2 of 3
participants tried to skip step 3 ("Connect calendar"): session 1 tried to
exit via the step label, and session 2 tried to skip it before hitting the
"required" indicator. Sessions 4–6 read the step as optional in the same way.
The step 4 invite hesitation comes from session 3 ("I'm worried this is going
to email my whole team before I'm ready") and the sessions 1–3 topline
(`topline-summaries/example-topline-summary.md`).

Corroborated by funnel data — see `analytics/summaries/onboarding-funnel-dropoff.md`,
which independently shows step 3 as the largest drop-off point.

## Recommendation
Relabel step 3 to state clearly that calendar connection is required, and
give visible feedback that invites (entered in step 4, "Invite your team") aren't sent
until the whole wizard is submitted.

## Status
Synthesized Feb 3, 2026, from sessions 1–6. Revisit after the step 3 wording
change (proposed in `research-readouts/onboarding-flow-q1-readout.md`) ships
and gets retested.
