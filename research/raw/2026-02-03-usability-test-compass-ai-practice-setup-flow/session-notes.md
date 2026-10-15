---
title: Usability Test — Compass AI Practice Setup Flow
date: 2026-02-03
type: usability-test
status: raw
researcher: Priya Patel
tags:
  - onboarding
  - usability
  - scheduling
  - phi
  - rollout
related_components: []
related_findings:
  - ../../findings/compass-ai-practice-setup.md
---

# Usability Test — Compass AI Practice Setup Flow

## Objective
The 2026-01-20 dashboard review found setups of Compass AI for a practice stopping most at Connect calendar
(7 of 24 setups started) and then at Invite your team (3 of 24), and said a dashboard can't show why
(`2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:47-48,74`). This session
watched administrators go through the practice setup flow to find out what happens at those two
steps. It is about admin setup of Compass AI, not staff training (in
`2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md:62`, "onboarding" means
training copy for clinicians).

## Method
- **Method:** Moderated usability test, remote, think-aloud, 60 min/session, one participant per
  session
- **Researcher:** Priya Patel (moderator)
- **Full participant roster:** see `participants.md` in this folder
- **Participants:** 6 — 4 Practice Administrators (P154-P157) and 2 IT Administrators (P158, P159)
- **Steps tested, in order:** 1 Sign in with Meridian SSO; 2 Practice details; 3 Connect calendar
  (read access to the practice's appointment schedule); 4 Invite your team (gives clinicians and
  staff access to Compass AI and sends them an email); 5 Review & finish.
- **Build:** Steps 3 and 4 are required in this build. There is no "Connect later" and no "Skip for
  now"; the only way past each step is to complete it.
- **Design context:** At session setup, the designer, Sam Okafor, stated that the calendar step is required because the scribe attaches recordings to scheduled encounters.
- **Test environment:** Participants signed in with their own Meridian SSO and were asked to set up
  as they would for their own practice. The environment was a test one: step 3 connected to a
  prepared sandbox calendar standing in for the practice's schedule, and step 4 used a prepared
  test staff list, so no real schedule was read and no real staff were emailed.
- **Test accommodation:** When a participant stopped at step 3, the moderator told them it was the
  sandbox calendar and let them continue. Every participant completed step 3 this way or on their
  own, so completing step 3 in this session is not a result.
- **Not covered:** The step 4 screen doesn't say when the invite email is sent, and these notes
  don't record when this build sends it. How Compass AI access is provisioned (through SSO groups
  or through these invites) wasn't known to the moderator and isn't recorded in the corpus.

## Key Findings
- **[HIGH]** *(calendar: who can approve)* 3 of 4 Practice Administrators (P154, P155, P157) stopped at Connect calendar and wouldn't connect it: it gives Compass AI access to patient appointments, and they did not think they could approve that. Each said it was IT's decision. The fourth (P156) asked the moderator whether connecting the schedule was theirs to approve before going on. All 4 continued only on the sandbox calendar (see Test accommodation).
- **[MEDIUM]** *(calendar: what is read)* Both IT Administrators (P158, P159) connected the calendar, but only after asking which fields are read (for example, whether visit reasons are included). The screen doesn't list them; the moderator couldn't answer, and both went on without an answer.
- **[HIGH]** *(invite: timing and training)* 3 of 4 Practice Administrators (P154, P156, P157) hesitated at Invite your team. They weren't sure whether the email goes out when they finish the step or at Review & finish, and they didn't want staff emailed before champion training is booked for the practice. P155 entered the test staff list and went on without comment.
- **[MEDIUM]** *(invite: provisioning)* One IT Administrator (P159) asked whether the invites create accounts or rely on the SSO groups staff are already in. The moderator couldn't answer, and the corpus doesn't record how access is provisioned.
- **[LOW]** *(sign in and practice details)* No issues at Sign in or Practice details: 6 of 6 participants completed both without help or comment on a problem.

## Representative Quotes
> "That's patient names and visit reasons. That's not my call — that's IT's."
> — Practice Administrator, P154

> "Is this mine to say yes to? I'd normally send anything like this to IT."
> — Practice Administrator, P156

> "If forty people get an email before anyone's booked training, my phone rings all afternoon."
> — Practice Administrator, P157

> "Before I connect it I want to know what it pulls. Times and providers, fine. Visit reasons, that's a different conversation."
> — IT Administrator, P158

> "Does this make them an account, or does it just use the groups they're already in? Because if it's a separate list, I'm the one keeping it in sync."
> — IT Administrator, P159

## Recommendations
1. List the fields read from the appointment schedule on the Connect calendar step.
2. Add a "Send to IT for approval" path on Connect calendar for an administrator who can't approve
   the access themselves.
3. Say on the Invite your team screen when the invite email is sent.
4. Let administrators schedule the invite email for a date, so it can go out once training is
   booked.

## Follow-ups / Open Questions
- How is Compass AI access provisioned: through SSO groups, through these invites, or both? Ask the
  setup flow's engineering team.
- When does this build send the invite email: at step 4 or at Review & finish?
- Check the setup dashboard after any copy change to these steps, to see whether setups still stop
  at Connect calendar and Invite your team.

## Related
- Synthesized into: [compass-ai-practice-setup.md](../../findings/compass-ai-practice-setup.md)
