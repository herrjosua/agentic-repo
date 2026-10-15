---
title: Wants to Know What a Step Commits Them To
date: 2026-03-03
status: final
designer: Priya Patel
tags:
  - onboarding
  - mindset
  - project-onboarding
related_findings:
  - ../research/findings/compass-ai-practice-setup.md
source_type: native
segment: "Administrators setting up Compass AI who stop or ask at a step that reaches patient data or staff, until they know what it does and whether its sign-off or prerequisite is in place"
---

# Wants to Know What a Step Commits Them To

## Overview
**Evidence basis:** Inferred. The stance is this record's own reading across what participants said and did at Connect calendar and Invite your team in `raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:51-54,58-71`; no participant described their own attitude, and no session names this stance.

Not a persona: a stance that showed up in both roles in the 2026-02-03 usability test, Practice
Administrators (P154-P157) and IT Administrators (P158, P159), at the two steps where setups stop
most, Connect calendar and Invite your team
(`raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:51-56`).
Both steps reach beyond the setup screen: one gives Compass AI read access to the practice's
appointment schedule, the other gives staff access and sends them an email (2026-02-03
`session-notes.md:33-35`). At each, participants wanted to know what the step would set off and
whether someone else's part was in place before they committed to it. This is about admin setup of
Compass AI, not staff training.

## What the sessions show
- **Whose sign-off it is.** 3 of 4 Practice Administrators stopped at Connect calendar because
  they "did not think they could approve" access to patient appointments; P156 asked whether it was
  theirs to approve before going on (`:51`). "Is this mine to say yes to? I'd normally send
  anything like this to IT." — P156 (`:61-62`)
- **What it reads.** Both IT Administrators asked which fields are read before connecting (`:52`).
  "Before I connect it I want to know what it pulls." — P158 (`:67`)
- **What it sends, and when.** 3 of 4 Practice Administrators hesitated at Invite your team, unsure
  when the email goes out and not wanting staff emailed before champion training is booked (`:53`).
  "If forty people get an email before anyone's booked training, my phone rings all afternoon." —
  P157 (`:64-65`)
- **What it leaves them maintaining.** P159 asked whether invites create accounts or use existing
  SSO groups: "if it's a separate list, I'm the one keeping it in sync." (`:54`, `:70-71`)

In each case the screen didn't answer the question: it doesn't list the fields read (`:52`) or say
when the email is sent (`:46-47`), and the moderator couldn't say how access is provisioned (`:54`).

## Where it doesn't hold
- **The stance didn't stop the IT Administrators.** P158 and P159 connected the calendar and went
  on without an answer (`:52`); the Practice Administrators continued only on the sandbox calendar
  (`:51`, `:43-45`). The same stance led to different actions by role.
- **Not every participant showed it at both steps.** P155 stopped at Connect calendar (`:51`) but
  entered the test staff list at Invite your team "and went on without comment" (`:53`). The notes
  record nothing at Invite your team for P158.
- **Not at the other steps.** Sign in and Practice details gave none of the 6 a problem (`:55`).

## Implications
The recorded recommendations already answer each question the stance raises: list the fields read
on Connect calendar; add a "Send to IT for approval" path there; say on Invite your team when the
email is sent; let administrators schedule the invite email for a date (`:74-79`); and confirm with
IT whether a privacy review request for Compass AI's schedule access has been filed
(`raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:40-41`).
This record adds no recommendation of its own.

## Limits
A mindset is meant as segmentation by attitude that recurs across personas. This study supports
less than that: 6 people in one test environment, at two steps of one flow, thinking aloud rather
than asked about their attitudes (2026-02-03 `session-notes.md:28-32`). It doesn't show how common
the stance is among administrators, whether it holds outside this flow, or what motivates it
beyond what participants said at the time. The dashboard doesn't record who ran each setup or why
it stopped (`raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:36-38`,
`:72-74`), so this stance can't be matched to any of the 24 setups. The IT Administrator
interviewed on 2026-02-24 (P160) didn't use the setup flow
(`raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:26`)
and isn't counted here.
