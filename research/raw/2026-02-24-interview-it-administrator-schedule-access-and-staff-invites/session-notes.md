---
title: Interview — IT Administrator on Schedule Access and Staff Invites
date: 2026-02-24
type: interview
status: raw
researcher: Priya Patel
tags:
  - onboarding
  - phi
  - privacy
  - security
related_components: []
related_findings:
  - ../../findings/compass-ai-practice-setup.md
---

# Interview — IT Administrator on Schedule Access and Staff Invites

## Objective
In the 2026-02-03 usability test, 3 of 4 Practice Administrators stopped at Connect calendar because they did not think they could approve Compass AI's access to patient appointments, and both IT Administrators asked which fields are read before connecting (`2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:51-52`). This session asked one IT Administrator who approves access requests across practices what has to happen before a new system can read a practice's appointment schedule, and who can start that. It is about admin setup of Compass AI, not staff training (in `2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md:62`, "onboarding" means training copy for clinicians).

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The participant is an IT Administrator who handles access requests for systems used across Meridian's practices. They had not used the Compass AI practice setup flow. The researcher described steps 3 (Connect calendar) and 4 (Invite your team) as the 2026-02-03 build shows them, and what the step 3 screen does and doesn't say, without sharing what other participants said. The participant did not name the scheduling system that holds the appointment schedule, and these notes don't record which system it is. This is their account of the approval process, not a review of its records.

## Key Findings
- **[HIGH]** *(schedule access: privacy review)* In their account, any new system that reads the appointment schedule needs a privacy review request before it is connected, and a Practice Administrator can't start one: requests are filed by IT. A practice that wants the calendar connected has to ask IT to file the request. They didn't know whether one had been filed for Compass AI.
- **[MEDIUM]** *(schedule access: still PHI)* They described scheduling as the lowest-risk data on the CMIO's PHI ordering, but still PHI: the schedule carries patient names and, depending on the fields read, visit reasons. They saw this as consistent with the ordering, not a contradiction of it, because the ordering ranks the risk and doesn't remove the review.

## Representative Quotes
> "Lowest risk isn't no risk. It's still patient names on a schedule. It still goes through privacy review, it just shouldn't take long."
> — IT Administrator, P160

> "A practice admin can't put in that request. They call us, we file it. If the screen just asks them to click connect, it's asking the wrong person."
> — IT Administrator, P160

## Recommendations
1. On Connect calendar, route an administrator who can't approve schedule access to IT, consistent with the "Send to IT for approval" path recommended on 2026-02-03 (`2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:75-76`).
2. Before more practices set up, confirm with IT whether a privacy review request for Compass AI reading the appointment schedule has been filed, and list the fields it covers.

## Follow-ups / Open Questions
- Has a privacy review request for Compass AI's schedule access been filed, and which fields does it cover?
- How is Compass AI access provisioned: through SSO groups, through the setup flow's invites, or both? The participant didn't know.

## Related
- Synthesized into: [compass-ai-practice-setup.md](../../findings/compass-ai-practice-setup.md)
