---
title: Usability Test — Ambient Scribe Sound-Alike Medication Flag Concept
date: 2026-02-10
type: usability-test
status: raw
tags:
  - ambient-scribe
  - usability
  - medication-safety
  - documentation
related_components:
  - ambient-scribe-widget
related_findings:
  - ../../findings/ambient-scribe.md
  - ../../findings/ambient-scribe-post-ga-refinements.md
---

# Usability Test — Ambient Scribe Sound-Alike Medication Flag Concept

## Objective
The GA-candidate round (2026-01-13) recommended treating sound-alike medication errors as an
ongoing post-GA monitoring item rather than a launch blocker, since the existing
`confidence-highlighted` variant already surfaces them as generically low-confidence. This session
tests an early concept that goes one step further: a *distinct* flag specifically for
suspected sound-alike medication names, visually separate from the general low-confidence
underline, to see whether participants notice and act on it differently than they do on
ordinary low-confidence text.

## Method
- **Method:** Moderated usability test, 6 simulated encounters seeded with known sound-alike pairs
  (e.g. hydralazine/hydroxyzine, clonidine/Klonopin), 40 min/session
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[HIGH]** *(flag recognized correctly)* 5 of 6 participants correctly identified the
  medication-specific flag (a distinct amber pill-shaped badge, vs. the generic low-confidence
  underline) as "different from the usual low-confidence thing" within the first two encounters,
  without being told the distinction existed.
- **[MEDIUM]** *(over-trust risk)* 2 participants said the badge's specificity made them *more*
  likely to treat unflagged medication lines as automatically correct — the opposite of the
  intended effect, and worth watching as adoption scales.
- **[LOW]** *(placement)* Badge placement inline with the medication name (vs. in a right-hand
  margin, tested as an alternate) was preferred 5:1 — participants didn't want to look away from
  the text to check a flag.
- **[LOW]** *(false positive tolerance)* One deliberately-seeded false positive (a real but
  unusual drug name) was accepted by all 6 participants as "worth a second look, not annoying" —
  suggests some over-flagging is tolerable if the badge is visually light.

## Representative Quotes
> "That's different from the fuzzy-underline stuff — this one's telling me specifically 'check the
> drug name,' which is exactly what I'd want flagged."
> — Physician, Internal Medicine, P22

> "If it's not flagged, I might just... trust it more than I should. That's on me, but it's worth
> knowing the tool does that to people."
> — Nurse Practitioner, P24

## Recommendations
1. Build the distinct medication-safety flag as its own variant, inline with the medication name,
   separate from generic confidence highlighting.
2. Before rollout, pair the flag with brief onboarding copy or training-pilot messaging that
   explicitly counters the over-trust-on-unflagged-lines risk surfaced by 2 of 6 participants —
   don't let the flag imply "anything unflagged is guaranteed correct."
3. Feed the false-positive tolerance finding to whoever tunes the sound-alike detection
   threshold — participants have headroom for a few extra false positives in exchange for not
   missing a real one.

## Follow-ups / Open Questions
- Needs a larger-N validation pass before this moves from concept test to build-ready spec.
- Over-trust-on-unflagged risk should be checked again once the post-GA monitoring dashboard
  (recommended 2026-01-13) has real error-rate data to compare against self-reported behavior.

## Related
- Synthesized into: [ambient-scribe-post-ga-refinements.md](../../findings/ambient-scribe-post-ga-refinements.md)
