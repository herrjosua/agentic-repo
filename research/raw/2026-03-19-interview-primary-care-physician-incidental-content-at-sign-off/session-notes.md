---
title: Interview — Primary Care Physician on Incidental Content in Scribe Drafts
date: 2026-03-19
type: interview
status: raw
researcher: Priya Patel
tags:
  - ambient-scribe
  - documentation
  - phi
  - privacy
  - clinician-workflow
related_components:
  - ambient-scribe-widget
related_findings:
  - ../../findings/ambient-scribe.md
---

# Interview — Primary Care Physician on Incidental Content in Scribe Drafts

## Objective
Earlier ambient-scribe research looked at what the scribe gets wrong: medication dosages and sound-alike drug names, and whether clinicians trust the draft enough to skim it. It did not look at what the scribe writes down correctly but that doesn't belong in a visit note: small talk, a patient's remarks about other people, side conversations with a family member in the room. This session asked a primary care physician, two months after the January 2026 GA, what of that kind ends up in their drafts and what they remove before they sign.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The participant is an internal medicine physician in an ambulatory primary care clinic, mid-career. They opted in to the ambient scribe after the January 2026 GA and use it for most of their visits. The scribe drafts visit notes for physicians, NPs and PAs; the clinician reviews the draft, corrects single lines in place, and signs. Low-confidence transcription is shown with a subtle underline. They did not take part in any earlier session. This is an interview about their own practice; nothing was shown or observed.

## Key Findings
- **[HIGH]** *(incidental content)* Their drafts regularly contain things that were said in the room but that they would not have written themselves: small talk at the start of the visit, a patient's remarks about a relative's health, comments made by a family member who came to the visit, and their own asides ("let me pull up your labs"). They remove these line by line with the in-place edit before signing. They put it at "most visits, a line or two", an informal impression, not a count.
- **[MEDIUM]** *(not underlined)* The underline marks lines where the scribe was unsure what it heard. Incidental content is usually transcribed accurately, so it is not underlined, and nothing in the draft points them to it. It also doesn't land in a predictable section: they have found it in the history of present illness and in the social history. To catch it they read the whole draft, including sections where nothing is underlined. That is one physician's practice; whether others do the same is not known.
- **[MEDIUM]** *(judgement)* What counts as incidental is a judgement call. A remark about stress at home can be clinically relevant and stay in the note; the same remark in passing about someone else is removed. They would not want the scribe to remove anything on its own. They could see value in it pointing out lines that might not belong, as long as they decide. That is an expectation; nothing was shown.

## Representative Quotes
> "It writes down everything that was said, not everything that matters. The sister's surgery is in my note until I take it out."
> — Physician (Internal Medicine), P146

> "The underline tells me where it wasn't sure what it heard. It heard the small talk perfectly, so nothing tells me to look there."
> — Physician (Internal Medicine), P146

## Recommendations
1. Share with the ambient scribe team that the confidence underline doesn't help with incidental content, because that content is usually transcribed accurately; reviewing for it means reading the whole draft.
2. If anything is designed for this, explore pointing out lines that may not belong in the note rather than removing them, so the clinician makes the call.
3. Keep this separate from the transcription-confidence work: it is about what belongs in the note, not whether it was heard correctly.

## Follow-ups / Open Questions
- How often drafts contain incidental content is not measured; "most visits, a line or two" is one physician's impression.
- Whether other physicians, NPs and PAs remove the same kinds of content, and how long it takes them, is not known; this is one interview.
- What happens to text a clinician removes before signing is not recorded in the corpus and was not discussed in this session.

## Related
- Earlier sessions: [2025-09-23 v0.2 usability test](../2025-09-23-usability-test-ambient-scribe-v02/session-notes.md) (in-place line correction), [2026-01-13 GA release candidate](../2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md) (confidence underline)
- Synthesized into: [ambient-scribe.md](../../findings/ambient-scribe.md)
