---
title: The Practice Administrator — Compass AI Practice Setup
date: 2026-03-03
status: final
designer: Priya Patel
tags:
  - onboarding
  - persona
  - project-onboarding
related_findings:
  - ../research/findings/compass-ai-practice-setup.md
source_type: native
segment: Practice Administrator (admin-staff) setting up Compass AI for their practice
based_on:
  - compass-ai-practice-setup.md
---

# The Practice Administrator — Compass AI Practice Setup

## Summary
**Evidence basis:** Mixed. Observed: each trait, quote and dependency below is stated in `raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:39-40,51,53,55,58-65` and `participants.md:23-26,32-35` in the same folder, or, for the IT side of the approval, by the IT Administrator interviewed in `raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:29,36-37`, and each line below cites its source. Inferred: drawing P154-P157 together as one archetype is this record's own framing; no session describes a single "Practice Administrator" type.

The administrator who uses the Compass AI practice setup flow to set Compass AI up for their
practice (`raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:18-19`).
Modeled on the 4 Practice Administrators (role class admin-staff), P154, P155, P156 and P157, in
the 2026-02-03 usability test (`participants.md:23-26`). They were recruited through ambulatory
practice contacts, "from administrators who had set up, or were about to set up, Compass AI for
their practice", and were new to the research (`participants.md:32-35`).

This is about admin setup of Compass AI, not staff training.

## What they do and say in setup
- Sign in with their own Meridian SSO and set up as they would for their own practice
  (`session-notes.md:39-40`). Sign in and Practice details gave none of the 6 participants a
  problem: "6 of 6 participants completed both without help or comment on a problem" (`:55`).
- Don't treat schedule access as theirs to approve. At Connect calendar, 3 of 4 (P154, P155, P157)
  "stopped at Connect calendar and wouldn't connect it: it gives Compass AI access to patient
  appointments, and they did not think they could approve that. Each said it was IT's decision."
  P156 "asked the moderator whether connecting the schedule was theirs to approve before going on"
  (`:51`).
  - "That's patient names and visit reasons. That's not my call — that's IT's." — P154 (`:58-59`)
  - "Is this mine to say yes to? I'd normally send anything like this to IT." — P156 (`:61-62`)
- Hold back the staff email until training is booked. 3 of 4 (P154, P156, P157) hesitated at
  Invite your team: "They weren't sure whether the email goes out when they finish the step or at
  Review & finish, and they didn't want staff emailed before champion training is booked for the
  practice." P155 "entered the test staff list and went on without comment" (`:53`).
  - "If forty people get an email before anyone's booked training, my phone rings all
    afternoon." — P157 (`:64-65`)

## What they depend on
- **IT, for approval of schedule access.** The 3 who stopped said connecting the calendar was IT's
  decision, and P156 would "normally send anything like this to IT" (`:51`, `:61-62`). The IT
  Administrator interviewed on 2026-02-24 described the same dependency from IT's side: any new
  system that reads the appointment schedule needs a privacy review request first, "a Practice
  Administrator can't start one: requests are filed by IT", and they didn't know whether one had been
  filed for Compass AI (`raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:29`).
  "A practice admin can't put in that request. They call us, we file it." — P160 (`:36-37`). That is
  one IT Administrator's account of the process, not a review of its records (`:26`).
- **Champion training being booked before staff are emailed.** The 3 who hesitated at Invite your
  team "didn't want staff emailed before champion training is booked for the practice"
  (`raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:53`).

## Gaps
- **Not on the dashboard.** The setup dashboard "doesn't show the signed-in person's role", so how
  many of the 24 setups it records were run by a Practice Administrator isn't known
  (`raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:36-38`).
  Nothing links this persona to any of those setups.
- **No background beyond the recruitment note.** `participants.md` records role, role class and how
  they were recruited (`:23-26`, `:32-35`), nothing else. The session notes don't record their
  answers to the facilitation guide's warm-up questions about their role
(`facilitation-guides/compass-ai-practice-setup-usability-guide.md:40-42`). Age, tenure, practice
  size and comfort with technology aren't recorded, so this persona doesn't give them. The "forty
  people" in P157's quote is what P157 said, not a recorded staff count.
- **Four people, in a test environment.** Every step 4 action used a prepared test staff list and
  step 3 a sandbox calendar (`raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:39-42`),
  and all 4 continued past Connect calendar only on that sandbox calendar (`:51`, `:43-45`).
- **One Practice Administrator didn't hesitate at the invite step.** P155 went on without comment
  (`:53`); the persona's invite-step behavior is 3 of 4, not all.
- Whether invites give staff access themselves or rely on SSO groups, and when the email is sent,
  isn't recorded (`:46-48`).

## Based on
The 2026-02-03 usability test (P154-P157), the 2026-02-24 interview (P160, for IT's side of the
approval dependency) and the 2026-01-20 dashboard review (for what the flow is and what the
dashboard can't show), as synthesized in
[`compass-ai-practice-setup.md`](../research/findings/compass-ai-practice-setup.md).
