---
title: Interview — Returning Care Coordinator on Override-Reason Capture
date: 2026-07-07
type: interview
status: raw
researcher: Priya Patel
tags:
  - care-coordination
  - alert-triage
  - trust-in-ai
  - workflow
related_components:
  - alert-triage-queue
related_findings:
  - ../../findings/care-coordination-triage.md
---

# Interview — Returning Care Coordinator on Override-Reason Capture

## Objective
Get a reaction to the override-reason capture screens (`wireflows/alert-triage-override-reason-capture.md`) from a coordinator who asked for exactly this kind of capture. The participant is P81, returning from 2025-08-26-usability-test-alert-triage-ai-care-coordination (August 2025); this interview is in July 2026. In that test they said they wanted to tell the ranking "this one's more urgent because I know this patient's history" and had nowhere to put it. The question was whether the reason list and the flow fit the reasons they actually have.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The participant reacted to the in-review wireflow screens: the "Override" action on a ranked queue item, the reason-capture modal (patient-history risk / recency not clinically relevant / other + free text) and the skip-reason branch. The wireflow is designed and in review, not built, and the AI-ranked queue hasn't been built; their team still works the chronological queue.

## Key Findings
- **[HIGH]** *(reason list)* Their most common reason for moving an alert is something the patient or a family member said on the phone that isn't in the chart yet. That reason isn't in the list. Looking at the screens, they said they would pick "other" most of the time, so the reason the capture most needs to collect would land in the least useful bucket.
- **[MEDIUM]** *(effort)* They would give a reason if it took one tap. They would not type free text on every override, and expected that on a busy day they would skip the modal rather than type. This is what they said they would do; nothing was observed in use.
- **[MEDIUM]** *(feedback loop)* If they never saw any effect from the reasons they gave, they said they would stop giving them after a while. The wireflow logs reasons for model-tuning review and doesn't show coordinators anything back.

## Representative Quotes
> "Half the time it's something the daughter told me on the phone yesterday. That's not in the chart yet, and it's not on your list, so I'd be hitting 'other' all day."
> — Care Coordinator, P81 (returning from 2025-08-26-usability-test-alert-triage-ai-care-coordination)

> "One tap, fine. But if I never see it change anything, I'll stop bothering."
> — Care Coordinator, P81 (returning from 2025-08-26-usability-test-alert-triage-ai-care-coordination)

## Recommendations
1. Add a one-tap reason for information from the patient or family that isn't in the chart yet, before the wireflow leaves review.
2. Keep every reason one tap, with free text optional, so a busy coordinator doesn't skip the modal altogether.
3. Decide how coordinators will see that their reasons are used, and say so in the design.

## Follow-ups / Open Questions
- How often overrides would fall under "other" with the current list is not known; this is one coordinator's expectation.
- Whether a feedback loop would keep coordinators giving reasons is untested.
- How the 2025 ranking weighted its inputs, and how accurate it is, are still not documented.

## Related
- Synthesized into: [care-coordination-triage.md](../../findings/care-coordination-triage.md)
