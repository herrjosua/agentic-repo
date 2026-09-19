---
title: Usability Test — AI Alert Triage for Care Coordination
date: 2025-08-26
type: usability-test
status: raw
tags:
  - alert-triage
  - usability
  - care-coordination
  - alert-fatigue
related_components:
  - alert-triage-queue
related_findings:
  - ../../findings/care-coordination-triage.md
---

# Usability Test — AI Alert Triage for Care Coordination

## Objective
Test whether an AI-prioritized alert queue (ranking care coordination alerts by urgency) actually improves triage speed/accuracy over the current chronological queue.

## Method
- **Method:** Moderated usability test, simulated alert queue, 45 min/session
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[HIGH]** *(ranking trust)* 4 of 5 participants disagreed with the AI's top-3 ranking on at least one of three test queues, generally because the model weighted 'recency' more heavily than coordinators' own sense of clinical risk — echoes the alert-fatigue concern from the May dashboard testing.
- **[HIGH]** *(override friction)* When participants disagreed with the ranking, there was no way to note why they reprioritized, meaning that correction signal isn't captured anywhere for future model improvement.
- **[MEDIUM]** *(speed)* Despite ranking disagreements, participants still completed triage of a 20-item queue faster with AI ranking present (avg 6.5 min) vs. chronological (avg 9 min) in this simulated test.
- **[MEDIUM]** *(supervisor concern)* Supervisor worried that speed gains could mask a coordinator rubber-stamping the AI order without real judgment, similar to the concern raised by the prior-auth supervisor in April.

## Representative Quotes
> "It's fast, I'll give it that. But fast and wrong is worse than slow and right in this job."
> — Care Coordinator Supervisor, P79

> "I wanted to tell it 'no, this one's more urgent because I know this patient's history,' but there was nowhere to put that."
> — Care Coordinator, P81

## Recommendations
1. Add a lightweight 'why did you reprioritize' capture on override, both to improve the model and to give coordinators a sense of agency the current design lacks.
2. Investigate incorporating patient history/continuity signals into ranking logic, not just recency, before wider testing.

## Follow-ups / Open Questions
- Share the override-capture idea with the Data Science team working on the care-gap flagging model (May findings) — likely the same underlying tuning problem.

## Related
- Synthesized into: [care-coordination-triage.md](../../findings/care-coordination-triage.md)
