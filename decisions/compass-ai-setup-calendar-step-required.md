---
title: Connect calendar is a required step in Compass AI practice setup
date: 2026-10-23
status: draft
decision_status: shipped
decision_status_source:
  - research/raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:27-29,33-35
date_decided: not recorded
decided_by: not recorded
superseded_by: ""
evidence:
  - source: research/raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md
    lines: "27-29,33-35,45"
  - source: research/raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md
    lines: "33-38,51-52,74-76"
  - source: research/raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md
    lines: "29,40"
  - source: research/findings/compass-ai-practice-setup.md
    lines: "37-44,96-97"
tags:
  - onboarding
  - scheduling
  - privacy
  - project-onboarding
related_findings:
  - compass-ai-practice-setup.md
related_components: []
---

# Connect calendar is a required step in Compass AI practice setup

## Decision
Connect calendar (step 3: read access to the practice's appointment schedule) is a required step
in Compass AI practice setup. There is no "Connect later" and no "Skip for now"; the only way past
it is to complete it
(`research/raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:33-37`).

Decision status: shipped. Setups started from 2025-12-01 to 2026-01-16 ran in a build where every
step is required; a setup can't skip a step, it can only be left open at it
(`research/raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:27-29,33-35`).
No record says the step was ever optional.

## Alternatives considered
not recorded. The recommendations on record change the step without making it optional: list the
fields read from the schedule, and add a "Send to IT for approval" path for an administrator who
can't approve the access
(`research/raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:74-76`;
`research/raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:40`).

## Rationale
**Evidence basis:** Mixed. The cost figures below are Observed in the cited raw session lines.
The rationale is the designer's statement at session setup, which no session tested.

At session setup, the designer stated that the calendar step is required because the scribe
attaches recordings to scheduled encounters
(`research/raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:38`). That
is the only rationale on record, and no session tested it
(`research/findings/compass-ai-practice-setup.md:42-44,96-97`).

What the step costs, as recorded:
- 7 of 24 setups were still open at Connect calendar on 2026-01-20, for 4 to 41 days
  (`research/raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:45`).
- 3 of 4 Practice Administrators stopped at Connect calendar because they did not think they could
  approve Compass AI's access to patient appointments, and both IT Administrators asked which
  fields are read before connecting
  (`research/raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:51-52`).
- An IT Administrator said any new system that reads the appointment schedule needs a privacy
  review request before it is connected
  (`research/raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:29`).

## Conditions to revisit
not recorded

## Not recorded
- Who decided: not recorded. The designer stated the rationale; whether they made the decision is
  not recorded.
- When it was decided: not recorded.
- Whether making the step optional was considered: not recorded.
- Whether the step needs to be required: not tested
  (`research/findings/compass-ai-practice-setup.md:96-97`).
