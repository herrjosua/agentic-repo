---
title: Onboarding
date: 2026-09-11
type: synthesis
status: synthesized
tags: [onboarding, first-run, mobile]
related_components: [onboarding-carousel, cta-primary]
related_findings: []
related_analytics: [onboarding-funnel-dropoff.md]
---

# Onboarding

## Current understanding

The permissions screen (step 2 of 4) is the weakest point in onboarding.
Users don't reliably understand that it's skippable, and the primary/
secondary CTA pairing doesn't visually communicate which action is the
"default" path. This shows up in both moderated testing and product
analytics (see the linked analytics summary) — the funnel data confirms
the drop-off is real, not a small-sample artifact.

Step 4 (account linking) has no observed issues in either research or
analytics and does not need attention right now.

## Supporting evidence

- `research/raw/2026-09-11-onboarding-flow-usability-test/` — moderated
  usability test, 5 participants, step 2 was the stall point for 4 of 5
- `analytics/summaries/onboarding-funnel-dropoff.md` — confirms step 2 as
  the largest single drop-off point in the live funnel

## Open questions

- Would isolating step 2's copy (without the rest of the flow) reproduce
  the same confusion, or is it a flow-position effect?
- Does the drop-off rate differ meaningfully between iOS and Android?

## Revision history

- 2026-09-11 — initial synthesis from first usability test round
