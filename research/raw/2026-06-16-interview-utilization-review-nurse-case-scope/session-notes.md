---
title: Interview — Returning Utilization Review Nurse on Pilot Case Scope
date: 2026-06-16
type: interview
status: raw
researcher: Priya Patel
tags:
  - nursing
  - prior-auth
  - utilization-management
  - trust-in-ai
related_components:
  - prior-auth-drafting-panel
related_findings:
  - ../../findings/prior-authorization.md
---

# Interview — Returning Utilization Review Nurse on Pilot Case Scope

## Objective
Check the prior-auth scope decision in `prior-authorization.md` against daily work, with a nurse who now uses the drafting panel. The finding says scope discipline held: pilot scope was limited to "straightforward" cases and complex cases were kept out (`findings/prior-authorization.md`:35-38), and that inline citations are actively used rather than ignored (lines 32-34). Both rest on test sessions with realistic scenarios. The participant is P19, returning from 2025-04-08-usability-test-prior-auth-ai-v1, where they said they liked the draft "for the boring, obvious cases" and wanted it kept away from complicated ones. The questions were whether the straightforward boundary matches the cases that actually reach them, how they check the panel's citations, and which cases they still do by hand.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** A limited pilot of the prior-auth drafting panel has run in the utilization review department since early 2026, on straightforward cases only, the scope the v2 test recommended (2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md:39). Complex cases stay manual. The pilot is not generally available and has not reached other departments. The panel shows inline citations to the chart entries behind each part of the draft. The participant is in the pilot and uses the panel on their own straightforward cases. They took part in the April 2025 v1 test only, not the November 2025 v2 test, so nothing here speaks to v2. They are not P17, the utilization review supervisor quoted in v1 and v2. No pilot outcomes data was reviewed in this session, and the written straightforward-case definition was not reviewed either; what the participant says about it is their own description.

## Key Findings
- **[HIGH]** *(boundary vs case mix)* The boundary holds as a rule but does not sort their cases cleanly up front. In their own words, a straightforward case is "one request, one current diagnosis, criteria we see every week." On their informal estimate, roughly half of what reaches them in a week looks like that at intake, and some of those turn out not to be once they are into the chart: an older related request, a prior claim denial on the same service, or evidence spread over years of notes. When that happens they stop using the draft and finish the case by hand, so the decision is made case by case, partway through, by the nurse. This complicates the finding's "scope discipline held" claim: the scope held in testing, where cases were labelled straightforward or complex in advance, but in daily work the label is not known until the nurse has read enough of the chart.
- **[MEDIUM]** *(citation checking)* They open the citations for the diagnosis and for the date of the most recent supporting note on every case, and skim the rest. They check dates first because of the outdated-code issue they saw in v1. They said they have not seen an outdated code in the pilot; that is their account, not a count, and v2's no-recurrence result covered 4 test cases. This confirms the finding's claim that citations are used rather than ignored, and extends it from a test session to one nurse's daily use; it says nothing about how other pilot users check.
- **[MEDIUM]** *(manual cases)* Cases they still do entirely by hand: anything following a prior claim denial, requests covering several services at once, and cases with long histories where they have to judge which evidence matters. Their reason was the same for all three: the work is deciding what to include, and a draft that includes things they then have to remove is slower than starting blank. Their rule when unsure is to treat the case as complex.

## Representative Quotes
> "The definition's fine on paper. The trouble is a lot of my cases look straightforward right up until I'm into the chart."
> — Utilization Review Nurse, P19 (returning from 2025-04-08-usability-test-prior-auth-ai-v1)

> "I click the dates first. After the old-codes problem last year, I don't trust a diagnosis until I've seen when it was written."
> — Utilization Review Nurse, P19 (returning from 2025-04-08-usability-test-prior-auth-ai-v1)

## Recommendations
1. When `prior-authorization.md` is next revised, say that the straightforward boundary is applied by the nurse during the case, not only at intake, and that cases leave the draft partway through.
2. Treat a case that starts in the panel and moves to manual as a normal path, and ask the pilot team whether it is recorded, since it is part of what the pilot is testing.
3. Keep dates prominent in the citations; this nurse checks them before anything else.

## Follow-ups / Open Questions
- How the pilot is performing is not known: no outcomes data (time, accuracy, claim denials) is recorded in the corpus, and none was reviewed here. The only time figures on record are v1's estimate and v2's measurement on 2 straightforward test cases.
- What "pilot expansion" in the v2 recommendation meant (how many nurses, how many weeks, what go/no-go metric) is still the open question v2 left; this participant did not know, and was not in v2.
- How often a case leaves the draft partway through is not measured; "roughly half" looking straightforward at intake is one nurse's estimate.
- Whether other pilot users check citations the same way is not known; this is one interview.

## Related
- Synthesized into: [prior-authorization.md](../../findings/prior-authorization.md)
