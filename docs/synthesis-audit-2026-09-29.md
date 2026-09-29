# Synthesis Overreach Audit — 2026-09-29

Audit of synthesis records (findings, readouts, toplines, deliverables and
components) for claims stronger than the raw sessions behind them. The
question for each claim: would a UX researcher who clicks from the record
to its raw session find the claim supported? Ties to v0.5.31.

Like `ask-audit-2026-09-27.md`, this file lives in `docs/`, which
`/api/ask` doesn't index, so its quotes of old wording won't confuse
retrieval.

## Method

A manual read, not an `/api/ask` run. Every factual claim in 21 records
was checked against the raw session lines it depends on:

- **Tier 1**: the 10 non-raw records cited in the CRUD UI's published
  static answers (`backend/ask/static/answers.json`, captured at corpus
  commit `4ba145f`).
- **Tier 2**: the other toplines and findings for onboarding, ambient
  scribe, prior authorization, care coordination and session lock (2
  records).
- **Tier 2b**: the rest of the known suspects plus the session-lock
  records (9 records).

Verdicts: SUPPORTED, OVERREACH (stronger than the evidence), UNSUPPORTED
(no raw source), STALE (contradicted by a later record) or LABELED
INFERENCE (a legitimate synthesis, but not labeled as one).

| Tier | Claims | Supported | Overreach | Unsupported | Stale | Labeled inference |
|---|---|---|---|---|---|---|
| 1 | 73 | 48 | 16 | 7 | 0 | 2 |
| 2 | 15 | 11 | 3 | 1 | 0 | 0 |
| 2b | 50 | 17 | 9 | 7 | 2 | 15 |
| **Total** | **138** | **76** | **28** | **15** | **2** | **17** |

Raw sessions were not edited (`raw/` is append-only). Line numbers below
refer to the pre-edit records at `4ba145f`.

## Fixed

### Cited in a published static answer

| # | Record | Claim (old line) | Raw evidence | Fix |
|---|---|---|---|---|
| A1 | `journey-maps/longitudinal-physician-ambient-scribe.md` | :21 — A frustration plateau: "why doesn't this feel any different?" | `raw/2025-09-23-usability-test-ambient-scribe-v02/session-notes.md:36` — "It's better, no question. But I still read every line, same as last time. Getting it right once doesn't mean I trust it yet." The quoted line appears in no raw session. | Replaced with P09's actual v0.2 quote; dropped "frustration plateau". |
| A2 | same | :18-19 — "medication dosage errors present in 3 of 5 sessions reinforce that caution" | `raw/2025-02-25-usability-test-ambient-scribe-v01/session-notes.md:30` — "missed or garbled medication dosages in 3 of 5 — physicians said this was disqualifying for direct sign-off without review"; `:36` (P09) — "I love what it got right, but I have to read every word anyway right now, so where's the time savings?" | Stated as a round-level count, separate from P09's own reason, which is now quoted. |
| A3 | same | :14-15 — "composite of participant P09 across all four ambient-scribe touchpoints she's been part of" | P09 is named in `raw/2025-02-25…/session-notes.md:37`, `raw/2025-09-23…/session-notes.md:37` and `raw/2026-01-13…/session-notes.md:37`. `raw/2026-02-10…/session-notes.md:53,57` names P22 and P24; `raw/2026-02-17…/session-notes.md:56,60` names P31 and P33. No raw file places P09 in the 2026-02 sessions or records a pronoun. | Now says the persona is modeled on P09 in the three test rounds and that the post-GA stage is inferred from other participants. |
| A4 | same | :23 — "Relief" | No emotion recorded in `raw/2026-01-13…/session-notes.md`. | Removed. |
| A5 | same | :28 — "a 'the tool ate my work' scare" | `raw/2026-02-17-session-lock-during-dictation/session-notes.md:54` (P31) — "I genuinely thought I'd lost it." | Replaced with P31's words. |
| A6 | `research/findings/ambient-scribe-post-ga-refinements.md` | :31-32 — "A distinct sound-alike-medication flag outperforms generic confidence highlighting for this specific error class." | `raw/2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md:36-39` — "5 of 6 participants correctly identified the medication-specific flag … as 'different from the usual low-confidence thing'"; `:70` — "Needs a larger-N validation pass". No catch-rate comparison was made. | "In a 6-person concept test, a distinct sound-alike-medication flag was recognized as different from generic confidence highlighting." |
| A7 | `topline-summaries/example-topline-summary.md` | :14-15 — "All 3 participants paused at step 4 ('Invite your team')" | `raw/2026-01-19-onboarding-usability-test/session-notes.md:27-28` (session 3 only) — "I guess I'm worried this is going to email my whole team before I'm ready." Sessions 1–2 (`:14-24`) record only the calendar step. | "1 of 3 (session 3) hesitated before inviting the team". `ask-audit-2026-09-27.md` records this overstatement as corrected in the finding and readout; the topline kept it through the renumbering in `49d2969`. |
| A8 | same | :18 — "Nobody read the sidebar progress indicator" | Not in `raw/2026-01-19-onboarding-usability-test/` (neither file mentions a sidebar, scrolling or progress). | Deleted. Data gap 2. |
| A9 | same | :18 — "all navigated by scrolling" | Same as A8. | Deleted. Data gap 2. |
| A10 | `research/findings/onboarding.md` | :19-21 — "admins aren't sure whether invites send immediately or only when the wizard is submitted" | `raw/2026-01-19-onboarding-usability-test/session-notes.md:27-28` — one participant. | "one admin (session 3) worried that invites would email the whole team before they were ready." |
| A11 | same | :16-17 — "This is the largest single source of friction in first-time setup." | `raw/2026-01-19-onboarding-usability-test/session-notes.md:31-33` — "step 3 wording read as optional by all participants". No other friction point is recorded or ranked. | "the most consistently observed friction point in first-time setup (all 6 sessions)." |
| A12 | `research-readouts/onboarding-flow-q1-readout.md` | :14-15 — "the single largest source of first-time-setup friction" | Same as A11. | Same wording as A11. |
| A13 | same | :17-18 — "independently corroborated by the Jan 2026 funnel export" | No `analytics/raw/` export exists; `analytics/summaries/onboarding-funnel-dropoff.md` says the export is "not included in this fictional dataset". | Now attributed to the funnel summary, with the export noted as missing. Data gap 4. |
| A14 | `research/findings/ambient-scribe.md` | :29-30 — "3 of the original 5 physician participants retained across all three rounds" | `raw/2025-09-23-usability-test-ambient-scribe-v02/session-notes.md:25` — "follow-up with 3 returning + 2 new participants"; `raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:37` names only "P09 (returning from v0.1 and v0.2)"; `raw/2025-02-25-usability-test-ambient-scribe-v01/participants.md:21-23` lists a Nurse Practitioner among the roles. | "3 of the original 5 participants returned for v0.2, and at least one (P09) also took part in the GA-candidate round". Data gap 9. |
| A15 | `research/findings/clinician-experience-documentation-burden.md` | :41-42 — "This is now the official pre-AI baseline" | `raw/2025-09-09-survey-clinician-burnout-documentation-burden-baseline/session-notes.md:40`, a recommendation — "Use this survey as the official baseline metric for measuring Compass AI's impact … (e.g., 6 and 12 months post-rollout)". No later raw session records adoption. | "The session recommends it as the official pre-AI baseline …" |
| A16 | `research/findings/prior-authorization.md` | :35-36 — "The team deliberately limited v1 testing to 'straightforward' cases (defined jointly with the nursing supervisor)" | `raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md:23` — "4 realistic case scenarios"; `:43` — "Consider limiting initial pilot scope to 'straightforward' case types"; `:47` — "Ask supervisor to help define what counts as a 'straightforward' case"; `raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md:24` — "4 case scenarios (2 straightforward, 2 complex)". | "After v1, the team limited pilot scope to 'straightforward' cases, with the nursing supervisor helping define them … v2 tested 2 straightforward and 2 complex cases". |

### Same records, not cited

| # | Record | Claim (old line) | Raw evidence | Fix |
|---|---|---|---|---|
| B1 | `research/findings/onboarding.md` | :38-40 — the invite hesitation "comes from session 3 … and the sessions 1–3 topline" | The topline is a synthesis with no raw link, and its "All 3" was itself unsupported (A7). `raw/2026-01-19-onboarding-usability-test/session-notes.md:27` — "Same step 3 hesitation as session 1." | Cites session 3 only, and notes that the raw notes file it under a "step 3 hesitation" label. |
| B2 | same | :42-43 — funnel data "independently shows step 3 as the largest drop-off point" | No `analytics/raw/` export. | Kept as a pointer to the summary; no longer called independent corroboration. Data gap 4. |
| B3 | `research-readouts/onboarding-flow-q1-readout.md` | :22-23 — "The drop-off isn't task difficulty; it's users not realizing the step is required and exiting" | `raw/2026-01-19-onboarding-usability-test/session-notes.md:16` — "Completed step"; `:22-23` — "Backed out when the 'required' indicator appeared". Neither participant exited. | "consistent with users misreading the step as optional; funnel data alone can't show why users drop off." |
| B4 | same | :24-25 — "no participant referenced [the sidebar progress indicator] unprompted across any of the 6 sessions" | Not in the raw session. | Deleted. Data gap 2. |
| B5 | same | :31-32 — "seen in session 3 and the sessions 1-3 topline" | Circular, as in B1. | "seen in session 3." |
| B38 | `personas/physician-longitudinal-scribe-user.md` | :25-26 — "one of the 3 returning participants present across all three … testing rounds" | Same as A14. | "one of the 3 participants who returned from v0.1 for v0.2, and the one confirmed in all three … rounds". |

### Link fixes (no claim changed)

| Record | Change | Raw evidence |
|---|---|---|
| `topline-summaries/example-topline-summary.md` | Added `related_findings: ["onboarding"]` and the raw path. | `raw/2026-01-19-onboarding-usability-test/` |
| `topline-summaries/ambient-scribe-ga-adoption-first-4-weeks.md` | Added the raw path. | `raw/2026-01-27-dashboard-review-ambient-scribe-ga-adoption/` |
| `research/findings/ambient-scribe.md` | Added 2026-01-27 to the Evidence Trail. | `raw/2026-01-27-dashboard-review-ambient-scribe-ga-adoption/session-notes.md:51` already lists this finding as where it was synthesized. |
| `research/findings/care-coordination-triage.md` | Added 2025-11-18 to the Evidence Trail; the finding's touch-target paragraph already relied on it. | `raw/2025-11-18-accessibility-audit-mobile-clinician-app/session-notes.md:29` — "Several action icons in the alert triage list … are 32x32px" |
| `user-flows/ambient-scribe-session-lock-recovery.md` | Cited the correction file for "all 4 observed clinicians". | `raw/2026-02-17-session-lock-during-dictation/correction-2026-09-27.md:41-42` — "this means **all 4 clinicians** assumed the draft was lost" |
| `research/findings/him-coding-and-billing.md` | "she" changed to "they"; P71's pronoun isn't recorded. | `raw/2025-07-29-usability-test-ai-coding-billing-suggestions/session-notes.md:35` — "Medical Coder (certified, senior), P71" |

## Data gaps

Each item needs new raw evidence before a claim can rest on it. Nothing
here should be restated as a finding until that evidence exists.

1. **Per-step timing in onboarding.** The only recorded duration is
   "paused ~15s at step 3" (session 1). No record can say which step
   users stall at longest.
2. **Sidebar and progress-indicator use, and how participants
   navigated.** Not recorded in the onboarding session. The sidebar and
   scrolling claims were removed from the topline and readout for this
   reason.
3. **Invite-step hesitation in sessions 1, 2 and 4–6.** Only session 3
   is recorded.
4. **The Jan 2026 onboarding funnel export.** `analytics/raw/` has none.
5. **The experience at onboarding steps 5–6 and at completion.** Not
   recorded.
6. **Admins' pre-use model of setup.** The facilitation guide asks "What
   does 'workspace' mean to you before you've used the product?", but no
   answers are recorded.
7. **Dana's demographics, time pressure and goals.** No raw source.
8. **Whether P09 took part in the 2026-02-10 or 2026-02-17 sessions.**
   Not recorded.
9. **Whether all 3 v0.1 returners took part in the GA-candidate round.**
   Only P09 is confirmed.
10. **How the 15-minute versus 4-hour re-auth question was settled**
    (`raw/2025-05-20…:30,35`), and how it relates to the fixed 10-minute
    idle timeout in `raw/2026-02-17…:49`.
11. **Whether the alert-triage queue shows its ranking basis.** Not
    recorded in `raw/2025-08-26…`.
12. **Alert-triage ranking accuracy.** Not measured; `raw/2025-08-26…:28`
    records disagreement, not accuracy.

## Raw inconsistency — P17's role

`raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md:35`
labels P17 "Utilization Review Nurse". But
`raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md:36`
calls P17 "Utilization Review Nurse (supervisor), P17 (returning from
v1)". Both rosters list a supervisor.
`research/findings/prior-authorization.md`'s "same … supervisor across
both" rests on the v2 line.

This needs an append-only correction file in the v1 folder, like
`raw/2026-02-17-session-lock-during-dictation/correction-2026-09-27.md`.
Not created in this change.

## Logged, not changed

The remaining Part B items: B6–B37 and B39–B46.

- **Findings**
  - `ambient-scribe.md`: "driven by fixing outright garbling"; "Approved for GA release".
  - `clinician-experience-documentation-burden.md`: "accuracy or trust" should read "accuracy or privacy"; alert fatigue "confirmed" should read "echoed".
  - `care-coordination-triage.md`: three overreaches and one unsupported causal claim.
- **Components**
  - `encounter-view` and `sso-mfa-login` Notes are stale after `raw/2026-02-17…`.
- **Design deliverables** (inference labels and content fixes)
  - Onboarding journey map, including "stalls here longest".
  - Onboarding storyboard.
  - Both mental models.
  - Both personas.
  - Session-lock user flow: "part of why" should read "likely part of why".

## Not a corpus problem

- **Static answers.** Seven answers in the CRUD UI's `answers.json` cite
  text changed here and need a recapture. `capture-static-answers.js verify`
  reports 9 of 23 cited sources no longer matching, across:
  all-scribe-draft-trust, scribe-medication-flag, onboarding-calendar-step,
  scribe-draft-retention, all-documentation-burden, prior-auth-time-savings
  and all-coders-billing-suggestions. The last one is only the HIM
  finding's "she" changing to "they".
- **The session-lock correction file isn't shown anywhere** (RR-97).
  - The raw loader reads only `session-notes.md` and `participants.md`,
    so `search.html`, the CRUD UI record view, `export_records.py` and
    Ask all show the uncorrected "4 of 5 clinicians".
  - The finding's link to the correction is a plain relative href in both
    UIs.
