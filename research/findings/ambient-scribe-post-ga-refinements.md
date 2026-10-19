---
title: Ambient Scribe — Post-GA Refinements
date: 2026-02-17
type: synthesis
status: synthesized
researcher: Priya Patel
reviewed_by: Jordan Lee
tags:
  - ambient-scribe
  - medication-safety
  - sso
  - mfa
  - phi
  - longitudinal
  - project-ambient-scribe
related_components:
  - ambient-scribe-widget
  - encounter-view
related_findings:
  - ambient-scribe.md
  - governance-and-phi.md
---

# Ambient Scribe — Post-GA Refinements

## Overview
Two follow-up threads opened by [ambient-scribe.md](ambient-scribe.md)'s GA-candidate round and
by an open edge case noted directly in the `encounter-view` component — neither a launch blocker,
both worth closing before they harden into permanent gaps.

- **In a 6-person concept test, a distinct sound-alike-medication flag was recognized as
  different from generic confidence highlighting.** The GA-candidate round treated sound-alike medication errors as an
  ongoing monitoring item, relying on the general `confidence-highlighted` variant to surface
  them. A concept test of a dedicated, visually distinct flag found 5 of 6 participants correctly
  recognized it as categorically different from generic low confidence — but also surfaced a new
  risk: 2 of 6 participants said the flag's specificity made them trust *unflagged* medication
  lines more than they should. Any rollout needs to actively counter that over-trust framing, not
  just ship the flag.
- **On the same medication thread, whether the flag stays visible to people who read the note
  after it is signed is an open design question, not a finding.** The flag has so far been
  designed and tested for the person signing the note. An infusion nurse (P143) who reads the note
  after it is signed and acts on its medication lines said they have not seen any marking on
  medication lines in the signed notes they read, neither a flag nor an underline, and assume every
  medication line in a signed note was checked by the provider; that is what they see, not how the
  product behaves (2026-09-15, session-notes.md:30). They said that if a line had been flagged and
  the provider then confirmed or changed it, they would want to know, because that is the line they
  would check against the order first; that is an expectation, and no such view exists (:30).
  Whether the flag, or any confidence marking, stays visible after a note is signed is not recorded
  in the corpus and was not settled in that interview (:45). A primary care clinic nurse (P138) is a
  counter-pattern for readers of the note: they also assume the provider read it all, but said
  knowing which parts the provider edited and which the scribe drafted would not change how they
  act on a note, only tell them where to ask questions; a stated expectation, with no alternative
  view shown (2026-03-17, session-notes.md:32).
- **Session lock during active dictation currently reads as silent data loss, even though it
  isn't.** The `locked` state's interaction with an in-progress recording was flagged as
  unresolved in `encounter-view`'s own notes, sourced from a May 2025 SSO/MFA interview side
  comment. Direct observation confirms the practical impact: all 4 shadowed clinicians assumed a
  locked session had destroyed their draft and restarted dictation from scratch, even though the draft
  is preserved server-side. IT Security confirmed the 10-minute idle-timeout policy itself is fixed, but an
  explicit "paused, draft preserved" state is a UI-only fix, not a policy change.
- Both threads point the same direction: **the underlying safety/reliability behavior is already
  correct (drafts are preserved; sound-alike names are technically detectable) — what's missing is
  UI that tells the clinician that, specifically and distinctly, rather than relying on a generic
  low-confidence signal to carry two very different kinds of meaning.**

## Evidence Trail
- **2026-02-10** — [Usability Test — Ambient Scribe Sound-Alike Medication Flag Concept](../raw/2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md) *(`usability-test`)*
- **2026-02-17** — [Contextual Inquiry — Session Lock During Active Ambient Scribe Dictation](../raw/2026-02-17-session-lock-during-dictation/session-notes.md) *(`contextual-inquiry`)* — 5 participants: 4 shadowed clinicians plus 1 IT Security stakeholder (see the session's [correction](../raw/2026-02-17-session-lock-during-dictation/correction-2026-09-27.md); the session notes say "5 clinicians")
- **2026-03-17** — [Interview — Clinic Nurse on Reading Scribe-Drafted Visit Notes](../raw/2026-03-17-interview-clinic-nurse-reading-scribe-drafted-notes/session-notes.md) *(`interview`)* — cited for P138's counter-pattern for readers of the note (session-notes.md:32) only
- **2026-09-15** — [Interview — Infusion Nurse on Medication Changes in Scribe-Drafted Notes](../raw/2026-09-15-interview-infusion-nurse-medication-changes-in-scribe-notes/session-notes.md) *(`interview`)* — cited for the open question of whether the medication flag stays visible after signing (session-notes.md:30, :45) only

## Related Findings
- [Ambient AI Scribe](ambient-scribe.md)
- [AI Governance, PHI & Compliance](governance-and-phi.md)
