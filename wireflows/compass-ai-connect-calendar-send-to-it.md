---
title: Compass AI Practice Setup — Connect Calendar "Send to IT for Approval" Wireflow
date: 2026-03-17
status: draft
designer: Priya Patel
tags:
  - onboarding
  - wireflow
  - scheduling
  - phi
  - project-onboarding
related_findings:
  - ../research/findings/compass-ai-practice-setup.md
source_type: native
flow_name: Connect calendar, with a "Send to IT for approval" branch for an administrator who can't approve schedule access
---

## Overview
**Evidence basis:** Mixed. Observed: why the branch exists and the recommendations behind it are stated in `raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:33-37,39-42,51-52,61-62,75-76` and `raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:26,29,36-37,40,44`, and each line below cites its source. Illustrative: the screens and the order of the branch are this record's design; no session saw or tested them. The parts nobody recorded are shown as open ends, not designed.

Combines the logic of a "Send to IT for approval" branch on step 3 of the Compass AI practice
setup flow, Connect calendar, with the screens it touches. The screen is the wireframe
[`compass-ai-connect-calendar-fields-and-it-approval.md`](../wireframes/compass-ai-connect-calendar-fields-and-it-approval.md);
the flow it sits in is
[`compass-ai-practice-setup-five-step-flow.md`](../user-flows/compass-ai-practice-setup-five-step-flow.md).
This is about admin setup of Compass AI, not staff training.

Why the branch: 3 of 4 Practice Administrators in the 2026-02-03 usability test stopped at Connect
calendar because "they did not think they could approve" Compass AI's access to patient
appointments, and "Each said it was IT's decision" (2026-02-03 `session-notes.md:51`). "Is this
mine to say yes to? I'd normally send anything like this to IT." — Practice Administrator, P156
(`:61-62`). The usability test recommended: "Add a "Send to IT for approval" path on Connect
calendar for an administrator who can't approve the access themselves." (`:75-76`) The 2026-02-24
interview recommended the same route (2026-02-24 `session-notes.md:40`). No decision on either is
recorded ([readout](../research-readouts/compass-ai-practice-setup-q1-readout.md) `:152`).

## Flow + screens
Step 2 (Practice details) complete -> Connect calendar loads, showing what connecting does, the
fields read (a placeholder until they are confirmed) and two actions, Connect and Send to IT for
approval -> the administrator chooses one.

**Connect branch.** Administrator who can approve the access -> Connect -> step 4 (Invite your
team), as in the build (2026-02-03 `:33-35`). In the test, both IT Administrators (P158, P159)
connected, "but only after asking which fields are read" (`:52`); they did so on a sandbox
calendar (`:39-42`).

**Send to IT for approval branch.** Administrator who can't approve the access -> Send to IT for
approval -> [open end: what IT receives isn't recorded or designed] -> IT's side, as one IT
Administrator described it on 2026-02-24: any new system that reads the appointment schedule
needs a privacy review request before it is connected, and requests are filed by IT (2026-02-24
`:29`). "A practice admin can't put in that request. They call us, we file it." — IT
Administrator, P160 (`:36-37`). That is one account of the process, from someone who hadn't used
the setup flow, not a review of its records (`:26`). Whether a privacy review request has been
filed for Compass AI isn't known (`:29`, `:44`) -> [open end: whether the setup stays open at
Connect calendar while IT acts isn't recorded or designed] -> [open end: how the administrator
comes back to finish the step isn't recorded or designed] -> Connect calendar is completed ->
step 4 (Invite your team).

No skip branch. The build has no "Connect later" and no "Skip for now"; the only way past the step
is to complete it (2026-02-03 `:36-37`). This wireflow adds neither: Send to IT for approval hands
the decision to IT, it doesn't skip the step.
