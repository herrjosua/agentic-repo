---
title: Dashboard review — Compass AI practice setup completion
date: 2026-01-20
type: analytics
status: raw
researcher: Priya Patel
tags:
  - onboarding
  - funnel
related_components: []
related_findings:
  - ../../findings/compass-ai-practice-setup.md
---

# Dashboard review — Compass AI practice setup completion

## Objective
Manually review the internal usage dashboard for the Compass AI practice setup flow, the flow a
practice's administrator uses to set Compass AI up for their practice, to see where setups stop
and how long they stay stopped. This is about admin setup of Compass AI, not staff training. The
dashboard records setups, not why a practice started one or which Compass AI features it was
setting up for, and the corpus doesn't record how practices were chosen to set up or when each
planned to go live. This review is not tied to the ambient scribe GA: the GA candidate was still
under test on 2026-01-13 (`2026-01-13-usability-test-ambient-scribe-ga-release-candidate`).

## Method
- **Method:** Manual dashboard review (no moderated session, no participants) — internal usage
  dashboard for the practice setup flow, covering setups started 2025-12-01 to 2026-01-16 (seven
  weeks), with step status as of the review date, 2026-01-20
- **Researcher:** Priya Patel
- **Full participant roster:** none — this is an analytics review, not a research session; see
  `participants.md` in this folder for why
- **Context:** The flow has five steps: 1 Sign in with Meridian SSO, 2 Practice details, 3 Connect
  calendar, 4 Invite your team, 5 Review & finish. Every step is required in this build; a setup
  can't skip a step, it can only be left open at it. A setup counts as started when someone signs
  in at step 1. "Stopped" means the setup was still open at that step on 2026-01-20. The dashboard
  shows setups by practice; it doesn't show the signed-in person's role, so whether a Practice
  Administrator or an IT Administrator ran each setup isn't known. The number of practices in the
  network isn't on the dashboard and isn't recorded in the corpus, so no completion rate against
  all practices is given here.
- **Counts (24 setups started in the window):**
  - Finished (completed Review & finish): 12 of 24
  - Still open on 2026-01-20: 12 of 24, stopped at:
    - Practice details: 1 of 24, open 5 days
    - Connect calendar: 7 of 24, open 4 to 41 days (median 16 days)
    - Invite your team: 3 of 24, open 6, 11 and 19 days
    - Review & finish: 1 of 24, open 2 days
  - Reached Review & finish: 13 of 24 (the 12 finished plus the 1 still open there)

## Key Findings
- **[HIGH]** *(stall at Connect calendar)* Connect calendar is where setups stop most: 7 of the 24
  setups started (7 of the 12 still open) were open at that step on 2026-01-20, and they had sat
  there longest, 4 to 41 days (median 16). In the 12 finished setups, Connect calendar was also the
  step left open longest in 8 of 12.
- **[MEDIUM]** *(stall at Invite your team)* Invite your team is the second most common stopping
  point: 3 of 24 setups started (3 of the 12 still open), open 6, 11 and 19 days.
- **[LOW]** *(other steps)* 1 of 24 was open at Practice details (5 days) and 1 of 24 at Review &
  finish (2 days). No setup was open at Sign in, because a setup only counts as started once
  someone has signed in.

## Representative Quotes
None — this session has no participants.

## Recommendations
1. Run a moderated usability test of the setup flow with both Practice Administrators and IT
   Administrators, focused on Connect calendar and Invite your team, to find out why setups stop
   there.
2. Ask the dashboard owners whether the signed-in person's role can be shown per setup, so later
   reviews can tell Practice Administrator setups from IT Administrator ones.

## Follow-ups / Open Questions
- Why do setups stop at Connect calendar and Invite your team? A dashboard can't show reasons:
  it records where a setup is open and for how long, not what the person at that step was
  thinking or waiting for.
- Do stopped setups eventually finish, or are they abandoned? Re-check these 12 open setups at the
  next review.

## Related
- Synthesized into: [compass-ai-practice-setup.md](../../findings/compass-ai-practice-setup.md)
