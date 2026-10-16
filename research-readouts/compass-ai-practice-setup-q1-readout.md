---
title: Compass AI Practice Setup — Q1 Study Readout
date: 2026-03-10
status: final
designer: Priya Patel
tags:
  - onboarding
  - readout
  - project-onboarding
related_findings:
  - ../research/findings/compass-ai-practice-setup.md
source_type: native
related_analytics:
  - compass-ai-practice-setup-funnel
presented_to: []
---

# Compass AI Practice Setup — Q1 Study Readout

## Summary
**Evidence basis:** Mixed. Observed: what each session did and found, its limits, the recommendations and the open questions are stated in `raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:27-48,51-59,65-76`, `raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:21-55,58-71,74-86` (with `participants.md:20-28` in the same folder) and `raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:20,23,26-30,33-37,40-45`, and each line cites its source; two caveats also cite the finding and the analytics summary, which say the same. Inferred: telling the three sessions as one study, grouping the findings by step and ordering the recommendations by step are this record's own framing. It adds no finding or recommendation of its own.

**Who it's for:** design and engineering for the Compass AI practice setup flow. No presentation,
decision, owner or date for any change is recorded, so this readout records none
(`presented_to` is left empty).

In the Compass AI practice setup flow, where every step is required, setups stop most at Connect
calendar and then at Invite your team. In a usability test, 3 of 4 Practice Administrators stopped at
Connect calendar, saying approving access to the practice's appointment schedule was IT's
decision; both IT Administrators asked which fields are read before connecting; and 3 of 4
Practice Administrators hesitated at Invite your team, not wanting staff emailed before champion
training is booked. An IT Administrator interviewed said schedule access needs a privacy review
request that only IT files. The sessions recorded six recommendations, and leave open when the invite email is sent, how
access is provisioned, whether a privacy review request has been filed and which scheduling
system holds the schedule.
This is about admin setup of Compass AI, not staff training.

## Why this study
A manual review of the internal usage dashboard for the setup flow, on 2026-01-20, looked at the 24
setups started 2025-12-01 to 2026-01-16 (2026-01-20 `session-notes.md:27-29`, `:41`). The flow has
five steps: 1 Sign in with Meridian SSO, 2 Practice details, 3 Connect calendar, 4 Invite your
team, 5 Review & finish (`:33-35`). By 2026-01-20, 12 had finished and 12 were still open: 7 at
Connect calendar (open 4 to 41 days, median 16), 3 at Invite your team (6, 11 and 19 days), 1 at
Practice details (5 days) and 1 at Review & finish (2 days); 13 reached Review & finish (`:42-48`).
In the 12 finished setups, Connect calendar was the step left open longest in 8 of 12 (`:53-54`).
The number of practices in the network isn't recorded, so there is no completion rate (`:38-40`).
These figures are summarized in
[`compass-ai-practice-setup-funnel.md`](../analytics/summaries/compass-ai-practice-setup-funnel.md).

The dashboard couldn't say why: "A dashboard can't show reasons: it records where a setup is open
and for how long, not what the person at that step was thinking or waiting for." (`:72-74`) The
review recommended a moderated usability test "with both Practice Administrators and IT
Administrators, focused on Connect calendar and Invite your team, to find out why setups stop
there" (`:65-67`), and asking the dashboard owners whether the signed-in person's role can be shown
per setup (`:68-69`).

## What was done
- **Usability test, 2026-02-03.** Planned in
  [`compass-ai-practice-setup-study-q1.md`](../research-plans/compass-ai-practice-setup-study-q1.md)
  and run from
  [`compass-ai-practice-setup-usability-guide.md`](../facilitation-guides/compass-ai-practice-setup-usability-guide.md).
  Moderated, remote, think-aloud, 60 minutes, one participant per session; moderator Priya Patel
  (2026-02-03 `session-notes.md:28-30`). 6 participants: 4 Practice Administrators (P154-P157)
  and 2 IT Administrators (P158, P159) (`:32`; `participants.md:20-28`). Participants signed in
  with their own Meridian SSO in a test environment: step 3 connected to a sandbox calendar and
  step 4 used a test staff list, so no real schedule was read and no real staff were emailed
  (`session-notes.md:39-42`).
- **Interview, 2026-02-24.** One 45-minute interview with an IT Administrator (P160) who handles
  access requests for systems used across Meridian's practices and had not used the setup flow
  (2026-02-24 `session-notes.md:23`, `:26`). It followed up the test's calendar findings: what has
  to happen before a new system can read a practice's appointment schedule, and who can start that
  (`:20`). The researcher described steps 3 and 4 without sharing what other participants said
  (`:26`).

## What was found
**Connect calendar.**
- 3 of 4 Practice Administrators (P154, P155, P157) stopped and wouldn't connect it: it gives
  Compass AI access to patient appointments, they did not think they could approve that, and each
  said it was IT's decision. P156 asked the moderator whether connecting the schedule was theirs to
  approve before going on (2026-02-03 `:51`).
  > "That's patient names and visit reasons. That's not my call — that's IT's." — Practice
  > Administrator, P154 (`:58-59`)

  > "Is this mine to say yes to? I'd normally send anything like this to IT." — Practice
  > Administrator, P156 (`:61-62`)
- Both IT Administrators (P158, P159) connected it, but only after asking which fields are read.
  The screen doesn't list them; the moderator couldn't answer, and both went on without an answer
  (`:52`).
  > "Before I connect it I want to know what it pulls. Times and providers, fine. Visit reasons,
  > that's a different conversation." — IT Administrator, P158 (`:67-68`)
- In P160's account, any new system that reads the appointment schedule needs a privacy review
  request before it is connected, and a Practice Administrator can't start one: requests are filed
  by IT. They didn't know whether one had been filed for Compass AI (2026-02-24 `:29`). They called
  scheduling the lowest-risk data on the CMIO's PHI ordering, but still PHI (`:30`).
  > "Lowest risk isn't no risk. It's still patient names on a schedule. It still goes through
  > privacy review, it just shouldn't take long." — IT Administrator, P160 (`:33-34`)

  > "A practice admin can't put in that request. They call us, we file it. If the screen just asks
  > them to click connect, it's asking the wrong person." — IT Administrator, P160 (`:36-37`)

**Invite your team.**
- 3 of 4 Practice Administrators (P154, P156, P157) hesitated. They weren't sure whether the email
  goes out when they finish the step or at Review & finish, and they didn't want staff emailed
  before champion training is booked for the practice. P155 entered the test staff list and went
  on without comment (2026-02-03 `:53`).
  > "If forty people get an email before anyone's booked training, my phone rings all afternoon."
  > — Practice Administrator, P157 (`:64-65`)
- One IT Administrator (P159) asked whether the invites create accounts or rely on the SSO groups
  staff are already in; the moderator couldn't answer (`:54`).
  > "Does this make them an account, or does it just use the groups they're already in? Because if
  > it's a separate list, I'm the one keeping it in sync." — IT Administrator, P159 (`:70-71`)

**Sign in and Practice details.** No issues: 6 of 6 participants completed both without help or
comment on a problem (`:55`).

## What it does and doesn't show
- **Completing step 3 in the test is not a result.** When a participant stopped at Connect
  calendar, the moderator told them it was the sandbox calendar and let them continue
  (2026-02-03 `:43-45`); all 4 Practice Administrators went on only that way (`:51`).
- **Why the calendar step is required is untested.** At session setup, the designer stated that it
  is required because the scribe attaches recordings to scheduled encounters (`:38`). That is the
  designer's stated rationale; no session tested it (finding `:42-44`).
- **The reasons can't be matched to the dashboard's setups.** The dashboard shows setups by
  practice, not the signed-in person's role (2026-01-20 `:36-38`), and not why a setup stopped
  (`:72-74`). So the reasons the 6 participants and P160 gave can't be matched to the 24 setups,
  and the analytics summary, which comes from the same review that prompted the test, isn't
  independent evidence for them (summary `:39-41`).
- **The interview is one account.** It is one IT Administrator's account of the approval process,
  not a review of its records (2026-02-24 `:26`).
- **The counts are small.** 4 Practice Administrators and 2 IT Administrators in a test
  environment, 1 interviewee, 24 setups in one seven-week window.

## Recommendations as recorded
Ordered by step. Each is quoted from the session that recorded it.

**Connect calendar**
1. "List the fields read from the appointment schedule on the Connect calendar step." (2026-02-03
   `:74`)
2. "Add a "Send to IT for approval" path on Connect calendar for an administrator who can't approve
   the access themselves." (`:75-76`)
3. "On Connect calendar, route an administrator who can't approve schedule access to IT,
   consistent with the "Send to IT for approval" path recommended on 2026-02-03" (2026-02-24
   `:40`)
4. "Before more practices set up, confirm with IT whether a privacy review request for Compass AI
   reading the appointment schedule has been filed, and list the fields it covers." (`:41`)

**Invite your team**
5. "Say on the Invite your team screen when the invite email is sent." (2026-02-03 `:77`)
6. "Let administrators schedule the invite email for a date, so it can go out once training is
   booked." (`:78-79`)

No decision on any of these is recorded.

## Open questions
- **When is the invite email sent?** The step 4 screen doesn't say, and the notes don't record
  when this build sends it (2026-02-03 `:46-47`, `:84`).
- **How is Compass AI access provisioned?** Through SSO groups, through the invites, or both isn't
  recorded; neither the moderator nor P160 knew (2026-02-03 `:47-48`, `:82-83`; 2026-02-24 `:45`).
- **Has a privacy review request for Compass AI's schedule access been filed, and which fields does
  it cover?** P160 didn't know (2026-02-24 `:29`, `:44`).
- **Which scheduling system holds the appointment schedule?** P160 didn't name it, and the notes
  don't record it (2026-02-24 `:26`).
- **Do stopped setups finish?** The dashboard review asked for its 12 open setups to be re-checked
  at the next review (2026-01-20 `:75-76`), and the test asked for the dashboard to be checked
  after any copy change to these steps (2026-02-03 `:85-86`).

## Built from this study
Synthesis already made from these sessions, each with its own Evidence basis line:
- Finding: [`compass-ai-practice-setup.md`](../research/findings/compass-ai-practice-setup.md)
- Persona:
  [`practice-administrator-compass-ai-setup.md`](../personas/practice-administrator-compass-ai-setup.md)
  (Mixed)
- Mental model:
  [`compass-ai-schedule-access-and-invites.md`](../mental-models/compass-ai-schedule-access-and-invites.md)
  (Inferred)
- Mindset: [`wants-to-know-what-a-step-commits.md`](../mindsets/wants-to-know-what-a-step-commits.md)
  (Inferred)
- Journey map:
  [`practice-administrator-compass-ai-setup.md`](../journey-maps/practice-administrator-compass-ai-setup.md)
  (Mixed)

## Sessions
- **2026-01-20** — [Dashboard review — Compass AI practice setup completion](../research/raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md)
- **2026-02-03** — [Usability Test — Compass AI Practice Setup Flow](../research/raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md)
- **2026-02-24** — [Interview — IT Administrator on Schedule Access and Staff Invites](../research/raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md)
