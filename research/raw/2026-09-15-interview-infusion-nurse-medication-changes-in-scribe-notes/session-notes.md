---
title: Interview — Infusion Nurse on Medication Changes in Scribe-Drafted Notes
date: 2026-09-15
type: interview
status: raw
researcher: Priya Patel
tags:
  - nursing
  - ambient-scribe
  - medication-safety
  - documentation
related_components: []
related_findings:
  - ../../findings/ambient-scribe-post-ga-refinements.md
---

# Interview — Infusion Nurse on Medication Changes in Scribe-Drafted Notes

## Objective
The medication thread in `ambient-scribe-post-ga-refinements.md` rests on a concept test of a distinct sound-alike medication flag with the people who review and sign scribe drafts: physicians and NPs (2026-02-10-ambient-scribe-medication-flag-concept/participants.md). Nobody who reads a signed, scribe-drafted note and then gives the medication has been asked about it. This session asked an infusion nurse how they check medication changes in the treating provider's visit note before they administer, and what, if anything, they see on medication lines in a signed note.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The participant is a registered nurse in an ambulatory infusion clinic, mid-career. Patients come in for scheduled infusions, and before starting one the nurse checks the infusion order against the treating provider's most recent visit note, which since the January 2026 GA is often scribe-drafted. The scribe drafts visit notes for physicians, NPs and PAs only; the participant doesn't use it, and their own charting is manual. They did not take part in any earlier session. They are not P138, the primary care clinic nurse interviewed in March 2026, and they don't do care coordination or post-discharge calls. The distinct medication flag is recorded in the corpus as a concept test (2026-02-10) and a wireframe in review (`wireframes/ambient-scribe-medication-flag.md`), whose hover copy reads "verify before signing"; nothing was shown in this session.

## Key Findings
- **[HIGH]** *(checking before administering)* Before every infusion they compare the order with the treating provider's latest visit note, looking for a medication change: a changed dose, a held infusion, a premedication added or stopped, or a lab value that has to be checked first. They give the medication from the order, not the note; the note is how they find out whether the order still reflects what was decided at the visit. When the two disagree, they hold the infusion and contact the provider before starting. In scribe-drafted notes they sometimes find a change in the body of the note, written up from the conversation, rather than in the plan, or worded so that they can't tell whether it was decided ("we'll probably bring the dose down"). They recalled holding an infusion to check for this reason "maybe once or twice a month" since GA; that is an informal recollection, not a count, and they couldn't say how many of those came from the scribe's drafting and how many from the provider. This is the same pattern of plan items landing in the body that the March 2026 clinic nurse described (2026-03-17-interview-clinic-nurse-reading-scribe-drafted-notes/session-notes.md:30), in a different setting: here the cost is a delayed infusion before administration, not a delayed callback.
- **[MEDIUM]** *(the flag and readers)* The medication flag has so far been designed and tested for the person signing the note. This nurse reads the note after it is signed and acts on its medication lines. In the signed notes they read, they said they have not seen any marking on medication lines, neither a flag nor an underline; that is what they see, not a statement of how the product behaves. Their working assumption is that every medication line in a signed note was checked by the provider. That is a reader's version of the over-trust risk the concept test found in 2 of 6 signers, who trusted unflagged lines more: a reader who never sees a flag treats every signed line as checked. They said that if a line had been flagged and the provider then confirmed or changed it, they would want to know, because that is the line they would check against the order first. That is an expectation; no such view exists. This extends the medication-flag finding to readers who didn't write the note.

## Representative Quotes
> "I don't hang anything off the note, I hang it off the order. The note is how I find out if the order's still right."
> — Registered Nurse (infusion clinic), P143

> "If it's signed, I assume they checked the meds. I've never seen anything on a med line that tells me different."
> — Registered Nurse (infusion clinic), P143

## Recommendations
1. Share with the ambient scribe team that medication changes decided at the visit need to reach the plan section as decided changes, because infusion nurses check them against the order before administering.
2. When the medication flag's design is next reviewed, include nurses who read signed notes and give the medication as a user group, and decide explicitly whether anything about a flag, and what the signer did with it, should reach them. Don't assume either answer.
3. Keep this evidence separate from the care coordination evidence on after-visit summaries: this is the visit note checked against the order before administration, not the summary a patient takes home.

## Follow-ups / Open Questions
- Whether the medication flag, or any confidence marking, stays visible after a note is signed is not recorded in the corpus and was not settled here. This nurse has not seen any marking on signed notes, which says what they see, not how the product behaves; and the corpus records the distinct flag only as a concept test and a wireframe in review.
- How often an infusion is held because the note and the order disagree is not measured; "once or twice a month" is one nurse's recollection, and how many of those trace back to scribe drafting is not known.
- Whether other infusion nurses, or nurses in other clinics, check the note against the order the same way is not known; this is one interview.
- How often the after-visit summary misses medication changes remains open in the care coordination evidence; it was not discussed here.

## Related
- Synthesized into: [ambient-scribe-post-ga-refinements.md](../../findings/ambient-scribe-post-ga-refinements.md)
