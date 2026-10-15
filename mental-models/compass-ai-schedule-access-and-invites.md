---
title: "Practice and IT Administrators' Mental Model of Schedule Access and Staff Invites"
date: 2026-03-03
status: final
designer: Priya Patel
tags:
  - onboarding
  - mental-model
  - project-onboarding
related_findings:
  - ../research/findings/compass-ai-practice-setup.md
source_type: native
scope: "Compass AI practice setup: who approves access to the appointment schedule (Connect calendar) and what Invite your team does"
---

# Practice and IT Administrators' Mental Model of Schedule Access and Staff Invites

## Overview
**Evidence basis:** Inferred. The model is this record's own reading of what participants said and did at Connect calendar and Invite your team in `raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:51-54,58-71` and what the IT Administrator interviewed said in `raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:29-30,33-37,45`; participants were asked to think aloud, not asked how they model approval or invites, and no session states the model.

Covers how Practice Administrators (P154-P157) and IT Administrators (P158, P159 in the 2026-02-03
usability test; P160 in the 2026-02-24 interview) think about two things in the Compass AI practice
setup flow: who can approve Compass AI reading the practice's appointment schedule, and what the
Invite your team step does. Quotes and counts are what participants said and did; the model drawn
from them is inferred. This is about admin setup of Compass AI, not staff training.

What the build says each step does: Connect calendar is "read access to the practice's appointment
schedule"; Invite your team "gives clinicians and staff access to Compass AI and sends them an
email" (2026-02-03 `session-notes.md:33-35`). The screens don't list the fields read or say when
the email is sent (`:46-47`, `:52`). At session setup the designer stated that the calendar step is
required because the scribe attaches recordings to scheduled encounters (`:38`); that is the
designer's stated rationale, not something any session tested.

## Who approves schedule access
**Practice Administrators: it's IT's call.** Connecting the calendar reads as approving access to
patient data, and that approval sits with IT, not with them. 3 of 4 (P154, P155, P157) stopped and
"Each said it was IT's decision"; P156 asked the moderator whether it was theirs to approve (`:51`).
- "That's patient names and visit reasons. That's not my call — that's IT's." — P154 (`:58-59`)
- "Is this mine to say yes to? I'd normally send anything like this to IT." — P156 (`:61-62`)

**IT Administrator interviewed: it goes through a privacy review that IT files.** In P160's account,
any new system that reads the appointment schedule needs a privacy review request before it is
connected, and only IT can file one; a practice has to ask IT (2026-02-24 `session-notes.md:29`).
They placed scheduling as the lowest-risk data on the CMIO's PHI ordering (described in
[governance-and-phi.md](../research/findings/governance-and-phi.md), `:53`) but still PHI, needing the
review (`:30`).
- "Lowest risk isn't no risk. It's still patient names on a schedule. It still goes through privacy
  review, it just shouldn't take long." — P160 (`:33-34`)
- "A practice admin can't put in that request. They call us, we file it. If the screen just asks
  them to click connect, it's asking the wrong person." — P160 (`:36-37`)

**IT Administrators in the test: they connected, after asking what is read.** Both P158 and P159
connected the calendar "but only after asking which fields are read"; the moderator couldn't
answer and both went on without an answer (2026-02-03 `session-notes.md:52`). Their question was
what is read, not who approves:
- "Before I connect it I want to know what it pulls. Times and providers, fine. Visit reasons,
  that's a different conversation." — P158 (`:67-68`)

**Where the accounts don't line up.** The Practice Administrators and P160 agree that approval is
IT's. P158 and P159 connected it themselves, on the sandbox calendar (`:40-42`). The notes don't
record whether they treated connecting as their approval to give, or whether they expected a
privacy review first, so their behavior and P160's account aren't reconciled here. P160 didn't know
whether a privacy review request had been filed for Compass AI (2026-02-24 `session-notes.md:29`).

**Which fields are read is unsettled.** P154 took the calendar to mean "patient names and visit
reasons"; P158 separated times and providers from visit reasons; P160 said the schedule carries
patient names and, "depending on the fields read", visit reasons (2026-02-24 `:30`). Which fields
Compass AI reads isn't on the screen or in the notes (2026-02-03 `:52`).

## What Invite your team does
**Practice Administrators: it emails staff, and timing matters because of training.** 3 of 4
(P154, P156, P157) hesitated: "They weren't sure whether the email goes out when they finish the
step or at Review & finish, and they didn't want staff emailed before champion training is booked
for the practice." P155 went on without comment (2026-02-03 `:53`).
- "If forty people get an email before anyone's booked training, my phone rings all afternoon."
  — P157 (`:64-65`)

The notes don't record whether the Practice Administrators thought the invite also gives staff
access, or only sends the email.

**IT Administrator: does it create accounts, or use SSO groups?** P159 asked "whether the invites
create accounts or rely on the SSO groups staff are already in" (`:54`):
- "Does this make them an account, or does it just use the groups they're already in? Because if
  it's a separate list, I'm the one keeping it in sync." — P159 (`:70-71`)

**Not known.** The moderator couldn't answer P159 (`:54`), P160 didn't know either (2026-02-24
`:45`), and how access is provisioned "wasn't known to the moderator and isn't recorded in the
corpus" (2026-02-03 `:47-48`). When this build sends the invite email isn't recorded either
(`:46-47`). This record doesn't resolve either question.

## Limits
- Seven people: 4 Practice Administrators and 2 IT Administrators in a test environment with a
  sandbox calendar and a test staff list (2026-02-03 `:39-42`), and 1 IT Administrator describing
  the approval process, not reviewing its records (2026-02-24 `:26`).
- All 4 Practice Administrators went past Connect calendar only on the sandbox calendar (2026-02-03
  `:51`), so completing that step says nothing about their model (`:43-45`).
- The dashboard doesn't show who ran each setup
  (`raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:36-38`), so
  this model can't be matched to the 7 setups open at Connect calendar or the 3 at Invite your team (`:45-46`).
