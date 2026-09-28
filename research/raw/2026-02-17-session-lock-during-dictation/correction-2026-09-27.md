---
title: Correction — Contextual Inquiry — Session Lock During Active Ambient Scribe Dictation
date: 2026-09-27
type: contextual-inquiry
status: raw
tags:
  - ambient-scribe
  - sso
  - mfa
  - authentication
  - phi
related_components: []
related_findings:
  - ../../findings/ambient-scribe-post-ga-refinements.md
---

# Correction — Session Lock During Active Ambient Scribe Dictation

Corrects `session-notes.md` in this folder. That file is left unedited (`raw/` is append-only).

## Participant count
`session-notes.md` says:

> Contextual inquiry / shadowing, 5 clinicians observed through at least one natural
> idle-timeout event during a real or simulated dictation session, plus 1 IT Security stakeholder
> interviewed on the technical constraints

`participants.md` says:

> **Count:** 5
>
> **Recruitment note:** 4 clinicians recruited from regular ambient-scribe users on units with known
> short idle-timeout windows; 1 IT Security stakeholder recruited directly for technical context
> rather than shadowed.

**Correct count:** 5 participants in total, made up of 4 clinicians who were shadowed and 1 IT
Security stakeholder who was interviewed but not shadowed. The session notes counted the IT
Security stakeholder as a fifth clinician. `participants.md` is the more precise source.

## Draft-loss result
`session-notes.md` says "4 of 5 clinicians assumed the draft was lost." Only the 4 shadowed
clinicians went through a lock during dictation, so this means **all 4 clinicians** assumed the
draft was lost and started dictating again after they re-authenticated.
