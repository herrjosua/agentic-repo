---
title: Compass AI Practice Setup — The Five Steps as Built
date: 2026-03-17
status: final
designer: Priya Patel
tags:
  - onboarding
  - user-flow
  - scheduling
  - project-onboarding
related_findings:
  - ../research/findings/compass-ai-practice-setup.md
source_type: native
flow_name: Compass AI practice setup, the five required steps in the build tested on 2026-02-03
screens_count: 5
---

# Compass AI Practice Setup — The Five Steps as Built

## Description
**Evidence basis:** Observed. The steps, what each does and the rules between them are stated in `raw/2026-01-20-dashboard-review-compass-ai-practice-setup-completion/session-notes.md:33-36,44-48,58-59` and `raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:33-38,46-48,52-53,55,84`; the Sign in variants are from `design-tokens/components/sso-mfa-login.md:13-14`, which the finding cites. Each line below cites its source. This is the flow as built, not a redesign, and it adds no recommendation.

The flow a practice's administrator uses to set Compass AI up for their practice, as it stood in
the build tested on 2026-02-03. Five steps, in order (2026-02-03 `session-notes.md:33-35`; the
2026-01-20 dashboard review lists the same five, `session-notes.md:33-34`). This is about admin
setup of Compass AI, not staff training.

Rules that hold across the flow:
- **Every step is required.** "Every step is required in this build; a setup can't skip a step,
  it can only be left open at it" (2026-01-20 `:34-35`). For steps 3 and 4: "There is no "Connect
  later" and no "Skip for now"; the only way past each step is to complete it" (2026-02-03
  `:36-37`).
- **When a setup counts as started, and as stopped.** "A setup counts as started when someone signs
  in at step 1. "Stopped" means the setup was still open at that step on 2026-01-20" (2026-01-20
  `:35-36`).

## Details
1. **Sign in with Meridian SSO** — the existing sign-in, with badge-tap and manual MFA variants
   (`design-tokens/components/sso-mfa-login.md:13-14`; finding `:38-39`). On 2026-01-20 no setup
   was open here, "because a setup only counts as started once someone has signed in"
   (2026-01-20 `:58-59`).
2. **Practice details** — the session notes name the step but don't describe its fields
   (2026-02-03 `:33`, `:55`). Open on 2026-01-20: 1 of 24 setups, for 5 days (2026-01-20 `:44`).
3. **Connect calendar** — "read access to the practice's appointment schedule" (2026-02-03
   `:33-34`). "The screen doesn't list" which fields are read (`:52`). At session setup the
   designer stated "that the calendar step is required because the scribe attaches recordings to
   scheduled encounters" (`:38`); that is the designer's stated rationale, and no session tested
   it (finding `:42-44`). Open on 2026-01-20: 7 of 24 setups, for 4 to 41 days (median 16)
   (2026-01-20 `:45`).
4. **Invite your team** — "gives clinicians and staff access to Compass AI and sends them an
   email" (2026-02-03 `:34-35`). "The step 4 screen doesn't say when the invite email is sent"
   (`:46`). Open on 2026-01-20: 3 of 24 setups, for 6, 11 and 19 days (2026-01-20 `:46`).
5. **Review & finish** — the session notes name the step (2026-02-03 `:35`) and otherwise mention
   it only as one of the two points where the invite email might go out (`:53`, `:84`). Open on
   2026-01-20: 1 of 24 setups, for 2 days; 13 of 24 reached it (2026-01-20 `:47-48`).

Not shown, because it isn't recorded:
- **When the invite email is sent.** The notes "don't record when this build sends it" (2026-02-03
  `:46-47`), and the question is left open: "When does this build send the invite email: at step 4
  or at Review & finish?" (`:84`). This flow places the email at neither step.
- **How access is provisioned.** "How Compass AI access is provisioned (through SSO groups or
  through these invites) wasn't known to the moderator and isn't recorded in the corpus"
  (`:47-48`). This flow doesn't show where access is created.
- **Which fields Connect calendar reads**, for the same reason (`:52`).

For what participants did and said at each step, see the journey map
([`practice-administrator-compass-ai-setup.md`](../journey-maps/practice-administrator-compass-ai-setup.md));
for the study as a whole, the finding
([`compass-ai-practice-setup.md`](../research/findings/compass-ai-practice-setup.md)).
