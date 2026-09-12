---
title: Usability Test — Ambient AI Scribe Prototype v0.2 (Follow-up)
date: 2025-09-23
type: usability-test
status: raw
tags:
  - ambient-scribe
  - usability
  - documentation
  - v0.2
  - longitudinal
related_components:
  - ambient-scribe-widget
  - encounter-view
related_findings:
  - ../../findings/ambient-scribe.md
---

# Usability Test — Ambient AI Scribe Prototype v0.2 (Follow-up)

## Objective
Re-test the ambient scribe after v0.1 fixes (medication dosage accuracy, inline correction, auto-listening, and the draft-retention/Security review from February) to see whether the critical and high findings were resolved.

## Method
- **Method:** Moderated usability test, simulated patient encounters, 45 min/session — follow-up with 3 returning + 2 new participants
- **Researcher:** M. Okafor
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[LOW]** *(phi-handling (resolved))* The draft-retention issue from v0.1 (critical finding, Feb) has been fixed — drafts now auto-expire from the editable state after 10 minutes of inactivity and the behavior is documented for Compliance; verified in all 5 sessions.
- **[MEDIUM]** *(accuracy (improved but not resolved))* Medication dosage errors dropped from 3/5 to 1/5 sessions — a clear improvement, but the remaining error type (misheard similar-sounding drug names) is a known class of error the team should track going forward.
- **[HIGH]** *(trust calibration (unchanged))* Despite accuracy improvements, all 5 participants still read every line before accepting — the returning 3 participants said their behavior from v0.1 hadn't changed at all in the interim, suggesting trust doesn't shift from accuracy improvements alone without something like a track record or confidence indicator.
- **[MEDIUM]** *(interaction (resolved))* In-place line correction (requested in v0.1) works well; all participants successfully corrected a wrong line without regenerating the full note.

## Representative Quotes
> "It's better, no question. But I still read every line, same as last time. Getting it right once doesn't mean I trust it yet."
> — Physician, Internal Medicine, P09 (returning from v0.1)

> "The fix where I can just click and edit one line? That's the difference between me using this and not."
> — Physician, Family Medicine, P11 (returning from v0.1)

## Recommendations
1. Since accuracy fixes alone haven't shifted trust/skim behavior, explore an explicit confidence indicator per line (e.g., highlighting low-confidence transcriptions) as the next trust-building lever, rather than continuing to chase raw accuracy alone.
2. Add a specific test/tracking metric for similar-sounding medication name errors going forward, since it's now the dominant remaining error type.

## Follow-ups / Open Questions
- Design and test a per-line confidence indicator concept for v0.3.
- Check with engineering whether a medication name pronunciation dictionary/fine-tune could reduce the sound-alike error class.

## Related
- Synthesized into: [ambient-scribe.md](../../findings/ambient-scribe.md)
