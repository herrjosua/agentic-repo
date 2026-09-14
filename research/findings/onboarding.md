---
title: Onboarding flow — setup step confusion
date: 2026-02-03
type: synthesis
status: synthesized
tags: [onboarding]
related_components: []
related_findings: []
related_analytics: [onboarding-funnel-dropoff]
---

## Summary
New admins hesitate at, or attempt to skip, step 3 of the onboarding wizard
("Connect calendar") because its wording implies the step is optional, when
it's actually required for later functionality. This is the largest single
source of friction in first-time setup.

## Evidence
Sourced from `raw/2026-01-19-onboarding-usability-test/` — 6 participants,
moderated usability sessions, Jan 19–23 2026. All 3 participants observed in
sessions 1–3 paused at step 3; 2 of 3 attempted to skip it outright.

Corroborated by funnel data — see `analytics/summaries/onboarding-funnel-dropoff.md`,
which independently shows step 3 as the largest drop-off point.

## Recommendation
Relabel step 3 to state clearly that calendar connection is required, and
give visible feedback that invites (entered later, in step 4) aren't sent
until the whole wizard is submitted.

## Status
Synthesized Feb 3, 2026, from sessions 1–6. Revisit after the step 3 wording
change (proposed in `research-readouts/onboarding-flow-q1-readout.md`) ships
and gets retested.
