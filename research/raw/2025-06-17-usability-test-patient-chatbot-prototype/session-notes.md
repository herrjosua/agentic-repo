---
title: Usability Test — Patient Scheduling Chatbot Prototype
date: 2025-06-17
type: usability-test
status: raw
tags:
  - chatbot
  - usability
  - patient-experience
  - scheduling
related_components:
  - patient-chatbot-widget
  - scheduling-widget
related_findings:
  - ../../findings/patient-scheduling-chatbot.md
---

# Usability Test — Patient Scheduling Chatbot Prototype

## Objective
Test the scheduling-only chatbot prototype's usability and confirm the 'talk to a person' escape hatch is discoverable and effective.

## Method
- **Method:** Moderated remote usability test, task-based, 30 min/session
- **Researcher:** M. Okafor
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[HIGH]** *(discoverability)* 3 of 8 participants did not find the 'talk to a person' option when asked to try to reach a human, even though it existed — it was placed in a small text link below the main chat input.
- **[MEDIUM]** *(task success)* Rescheduling an existing appointment had a lower success rate (5/8) than booking a new one (7/8), largely due to the bot asking for an appointment ID participants didn't have handy.
- **[MEDIUM]** *(tone)* Several participants (4/8) described the bot's tone as 'overly cheerful' given they were often scheduling around being unwell, which felt mismatched.
- **[MEDIUM]** *(confidence signaling)* Participants couldn't tell when the bot was confident vs. guessing; one participant proceeded with an incorrect date because the bot stated it 'confidently.'

## Representative Quotes
> "I looked right past that little link. If I hadn't been told it existed, I never would have found it."
> — Patient, P61

> "It kept saying 'Great!' and 'Awesome!' while I'm trying to reschedule because I'm sick. Just... tone it down a little."
> — Patient, P64

## Recommendations
1. Redesign the 'talk to a person' affordance as a persistent, visually prominent button rather than a small inline link.
2. For rescheduling, let the bot look up appointments by name/date instead of requiring an appointment ID.
3. Revisit the bot's tone/copy to be more neutral, especially for interactions likely tied to illness.

## Follow-ups / Open Questions
- Partner with UX writing on a tone pass before next round.
- Re-test discoverability of the escape hatch after the redesign specifically.

## Related
- Synthesized into: [patient-scheduling-chatbot.md](../../findings/patient-scheduling-chatbot.md)
