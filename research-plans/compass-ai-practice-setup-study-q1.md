---
title: Compass AI Practice Setup — Usability Study Plan, Q1
date: 2026-01-27
status: final
designer: Priya Patel
tags:
  - onboarding
  - usability
  - project-onboarding
related_findings:
  - ../research/findings/compass-ai-practice-setup.md
source_type: native
method: moderated-usability
study_dates:
  start: 2026-02-03
  end: 2026-02-03
related_guide: facilitation-guides/compass-ai-practice-setup-usability-guide.md
---

# Compass AI Practice Setup — Usability Study Plan, Q1

## Background
**Evidence basis:** Mixed. Background is Observed, from `raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:27-48`, `:51-56` and `:65-74`. Objectives, Method, Participants, Test environment and What this study can and can't answer are Inferred: the plan's own design, built on that review's recommendation (`:65-67`) and open question (`:72-74`).

The Compass AI practice setup flow is the flow a practice's administrator uses to set Compass AI up
for their practice. This is about admin setup of Compass AI, not staff training.

The 2026-01-20 dashboard review looked at setups started 2025-12-01 to 2026-01-16. Of the 24
started, 12 were still open on 2026-01-20: 7 at Connect calendar and 3 at Invite your team
(`session-notes.md:41-46`). It called Connect calendar the step where setups stop most and Invite
your team the second most common stopping point (`:51-56`), and recommended: "Run a moderated
usability test of the setup flow with both Practice Administrators and IT Administrators, focused
on Connect calendar and Invite your team, to find out why setups stop there." (`:65-67`)

It also said why the dashboard can't answer that itself: "A dashboard can't show reasons: it
records where a setup is open and for how long, not what the person at that step was thinking or
waiting for." (`:72-74`)

## Objectives
1. Find out what happens at Connect calendar when an administrator sets up Compass AI for their
   practice: what they expect the step to do, and what stops them or lets them go on.
2. Find out the same at Invite your team.
3. Note anything at the other three steps that gets in the way, without focusing on them.
4. See whether Practice Administrators and IT Administrators go through steps 3 and 4 differently.

## Method
- **Method:** Moderated usability test, remote, think-aloud, 60 minutes per session, one
  participant per session.
- **Researcher:** Priya Patel (moderator).
- **Steps tested, in order:** 1 Sign in with Meridian SSO; 2 Practice details; 3 Connect calendar
  (read access to the practice's appointment schedule); 4 Invite your team (gives clinicians and
  staff access to Compass AI and sends them an email); 5 Review & finish.
- **Build:** Steps 3 and 4 are required in this build. There is no "Connect later" and no "Skip for
  now"; the only way past each step is to complete it.
- **Design context:** At session setup, the moderator is told the designer's rationale for the
  calendar step: the designer, Sam Okafor, states that it is required because the scribe attaches
  recordings to scheduled encounters. This study does not test that rationale; it is context for
  the moderator, not a question for participants.
- **Script:** see
  [`facilitation-guides/compass-ai-practice-setup-usability-guide.md`](../facilitation-guides/compass-ai-practice-setup-usability-guide.md).

## Participants
- **6 participants:** 4 Practice Administrators and 2 IT Administrators.
- Practice Administrators recruited through ambulatory practice contacts, from administrators who
  have set up, or are about to set up, Compass AI for their practice. IT Administrators recruited
  through the IT department.
- Participant IDs are allocated from `research/participants.yml` when the session folder is
  created.

## Test environment
- Participants sign in with their own Meridian SSO and are asked to set up as they would for their
  own practice.
- The environment is a test one: step 3 connects to a prepared sandbox calendar standing in for the
  practice's schedule, and step 4 uses a prepared test staff list, so no real schedule is read and
  no real staff are emailed.
- **Test accommodation:** if a participant stops at step 3, the moderator tells them it is the
  sandbox calendar and lets them continue. Completing step 3 is then not a result.

## What this study can and can't answer
It can show, for 6 participants, what they say and do at each step of the flow in a test
environment, and what they were thinking at Connect calendar and Invite your team.

It can't answer:
- Why the 24 setups on the dashboard stopped. The dashboard doesn't show who ran each setup or
  why it stopped, so what the 6 participants say can't be matched to those setups.
- Whether a Practice Administrator or an IT Administrator ran each of those setups. The dashboard
  doesn't show the signed-in person's role
  (`raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:36-38`).
- How many practices in the network have set up Compass AI, or a completion rate against all
  practices. The number of practices isn't on the dashboard or in the corpus (`:38-40`).
- Whether the calendar step needs to be required. The designer's rationale is not tested.
- Whether a participant would complete step 3 on their own practice's real calendar, once the
  accommodation is used.
- What happens after setup with a real schedule and real staff, since nothing real is read or sent.

## Gaps going in
- When this build sends the invite email (at step 4 or at Review & finish) isn't known to the
  moderator. If a participant asks, the moderator says they can't answer and notes the question.
- How Compass AI access is provisioned (through SSO groups or through these invites) isn't known to
  the moderator. Same rule.
- How practices were chosen to set up, and when each planned to go live, isn't recorded
  (`raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:21-23`).

## Timeline
- Plan: 2026-01-27
- Sessions: 2026-02-03
- A follow-up with IT may be added, depending on what the test shows.

## Related
- Facilitation guide:
  [`compass-ai-practice-setup-usability-guide.md`](../facilitation-guides/compass-ai-practice-setup-usability-guide.md)
- Motivating review:
  [`2026-01-20-dashboard-review-compass-ai-practice-setup-completion`](../research/raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md)
- Session record (the study as run):
  [`2026-02-03-usability-test-compass-ai-practice-setup-flow`](../research/raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md)
- Synthesized into: [`compass-ai-practice-setup.md`](../research/findings/compass-ai-practice-setup.md)
