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
| A3 | same | :14-15 — "composite of participant P09 across all four ambient-scribe touchpoints she's been part of" | P09 is named in `raw/2025-02-25…/session-notes.md:37`, `raw/2025-09-23…/session-notes.md:37` and `raw/2026-01-13…/session-notes.md:37`. `raw/2026-02-10…/session-notes.md:53,57` names P22 and P24; `raw/2026-02-17…/session-notes.md:56,60` names P31 (P119 since `raw/2026-02-17-session-lock-during-dictation/correction-2026-10-13.md`) and P33. No raw file places P09 in the 2026-02 sessions or records a pronoun. | Now says the persona is modeled on P09 in the three test rounds and that the post-GA stage is inferred from other participants. |
| A4 | same | :23 — "Relief" | No emotion recorded in `raw/2026-01-13…/session-notes.md`. | Removed. |
| A5 | same | :28 — "a 'the tool ate my work' scare" | `raw/2026-02-17-session-lock-during-dictation/session-notes.md:54` (P31 (P119 since `raw/2026-02-17-session-lock-during-dictation/correction-2026-10-13.md`)) — "I genuinely thought I'd lost it." | Replaced with that participant's words. |
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
    recorded in `raw/2025-08-26…`. Phase 3b deleted the care-coordinator
    mental model's claim that "the queue doesn't surface its ranking basis"
    (P21).
12. **Alert-triage ranking accuracy.** Not measured; `raw/2025-08-26…:28`
    records disagreement, not accuracy. Phase 3b deleted the mental model's
    claim that the coordinator/model mismatch, "not raw ranking accuracy, is
    why 4 of 5 participants disagreed" (P22).

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
Not created in this change. **Made 2026-10-13:**
`raw/2025-04-08-usability-test-prior-auth-ai-v1/correction-2026-10-13.md`
labels P17 the supervisor.

## Logged, not changed

The remaining Part B items: B6–B37 and B39–B46. Phase 3b (below) handles
them under new IDs.

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

## Phase 3b (2026-10-08)

### Renumbering

The individual B-numbers for B6–B37 and B39–B46 weren't recorded, only
the grouped summary under "Logged, not changed". This phase uses new IDs,
P1–P40, rebuilt from that summary and the tier totals in Method:

| Tier | Problem claims | Fixed in phases 1–3a | Left | Records | IDs |
|---|---|---|---|---|---|
| 1 | 25 | A1–A16, B1–B5 | 4 | `ambient-scribe.md`, `clinician-experience-documentation-burden.md` | P1–P4 |
| 2 | 4 | — | 4 | `care-coordination-triage.md` | P5–P8 |
| 2b | 33 | B38 | 32 | `encounter-view`, `sso-mfa-login`, the session-lock user flow, both personas, both mental models, the onboarding journey map and storyboard | P9–P40 |
| **Total** | **62** | **22** | **40** | | |

40 matches the count of B6–B37 plus B39–B46. Per-claim verdicts are this
phase's reading; they aren't guaranteed to match the original audit's.
Line numbers below refer to the records at `291ff63`.

### Changed

| # | Record | Claim (old line) | Raw evidence | Fix |
|---|---|---|---|---|
| P1 | `research/findings/ambient-scribe.md` | :36-37 — dosage errors dropped "driven by fixing outright garbling" | `raw/2025-09-23-usability-test-ambient-scribe-v02/session-notes.md:31` — "Medication dosage errors dropped from 3/5 to 1/5 sessions — a clear improvement, but the remaining error type (misheard similar-sounding drug names) is a known class of error the team should track going forward." No cause given. | States the drop without a cause. |
| P2 | same | :45-46 — "Approved for GA release. Sound-alike medication errors move to post-GA monitoring" | `raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:43` — "Approve for GA release"; `:44` — "Continue tracking sound-alike medication errors as a post-GA metric rather than delaying release further". Both are recommendations; no raw session records the approval. | "The GA-candidate session recommends GA release …" |
| X1 | same | :38 — sound-alike errors are "now a tracked, monitored issue" | `raw/2026-01-13…:48` — "Set up post-GA monitoring dashboard for sound-alike medication error rate."; `raw/2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md:71-72` — "once the post-GA monitoring dashboard (recommended 2026-01-13) has real error-rate data". | Says the dashboard was recommended. |
| P3 | `research/findings/clinician-experience-documentation-burden.md` | :38 — "ahead of accuracy or trust concerns that were originally hypothesized to dominate" | `raw/2025-02-11-survey-nursing-attitudes-ai-documentation/session-notes.md:29` — "not accuracy or privacy as originally hypothesized." | "not accuracy or privacy as originally hypothesized." |
| P4 | same | :50 — "the same alert-fatigue pattern later confirmed in the care-coordination alert triage testing" | `raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md:28` — "echoes the alert-fatigue concern from the May dashboard testing." | "later echoed this alert-fatigue concern". |
| P5 | `research/findings/care-coordination-triage.md` | :29, :31-33 — "The baseline shaped what got built"; the August concept "is a variant of that same idea" | `raw/2025-01-29-contextual-inquiry-chart-review-baseline/session-notes.md:41` — "Scope an early AI concept around 'what changed since last review' rather than full summarization". `raw/2025-08-26…:20` (objective) doesn't mention the baseline. | Both causal claims dropped; the bullet now says the baseline recommended a scope. |
| P6 | same | :29-30 — "Coordinators explicitly said they didn't want full AI summarization" | `raw/2025-01-29…:37` (P05 only) — "I don't need it to think for me." | "One coordinator (P05) said …" |
| P7 | same | :31 — "what changed since I last looked." | `raw/2025-01-29…:37` — "If it could just tell me what changed since I last touched this chart, that alone would save me time. I don't need it to think for me." | P05 quoted exactly. |
| P8 | same | :40-42 — the missing override capture "undercuts the sense of agency the supervisor specifically flagged as a risk (fast-but-wrong …)" | `raw/2025-08-26…:31` — "Supervisor worried that speed gains could mask a coordinator rubber-stamping the AI order without real judgment"; `:34` (P79) — "fast and wrong is worse than slow and right in this job."; `:41` (recommendation) — "to give coordinators a sense of agency the current design lacks." | Rubber-stamping and the quote attributed to the supervisor; agency attributed to the study's recommendation. |
| X2 | `design-tokens/components/chart-review-summary-panel.md` (Notes) | :25 — "coordinators explicitly asked for 'what changed since I last looked'" | Same as P6 and P7; `raw/2025-01-29…:41` for the scope. | Cites the recommendation and quotes P05 exactly. |
| X3 | `wireflows/alert-triage-override-reason-capture.md` | :14-16 — "a sense of coordinator agency the study's supervisor specifically flagged as a risk" | Same as P8. | Agency attributed to the recommendation; the supervisor's rubber-stamping concern stated separately. |
| P9 | `design-tokens/components/encounter-view.md` (Notes) | :27 — "an open edge case … not yet resolved in this component" | `raw/2026-02-17-session-lock-during-dictation/session-notes.md:38-41` — "a session lock mid-recording simply freezes the ambient-scribe widget with no message"; `correction-2026-09-27.md:41-42` — "**all 4 clinicians** assumed the draft was lost". `user-flows/ambient-scribe-session-lock-recovery.md` is `status: in-review`. | Studied, and a recovery flow is designed and in review; not called resolved. |
| P10 | `design-tokens/components/sso-mfa-login.md` (Notes) | :28 — 15-minute re-auth "unresolved as of the 2025-05-20 interview" | `raw/2025-05-20-interview-it-security-sso-mfa-modernization/session-notes.md:30` — "re-authentication requirement every 15 minutes, down from the current 4 hours"; `raw/2026-02-17…:49-50` — "IT Security confirmed the 10-minute idle timeout is not adjustable per-feature". | Keeps the 2025-05-20 facts; adds the 10-minute idle timeout and says how the two relate isn't recorded (data gap 10). Adds the in-review recovery flow. |
| T1 | `design-tokens/components/care-gap-badge.md` (Notes) | :26 — "Currently reuses the same color scheme as the existing EHR acuity indicators … Needs a visually distinct treatment" | `raw/2025-05-06-usability-test-clinician-dashboard-redesign-v1/session-notes.md:32` — "Badge color scheme was confused with existing acuity color-coding already used elsewhere in the EHR"; `accessibility-screenings/status-indicator-remediation-screening.md:22` — "Both components render status as color-only dots"; `design-system/v4-1-status-indicator-component.md:14-17` — "replace the color-only status-dot markup". | Says v4.1 replaces the colour-only markup and that whether it resolves the acuity-colour confusion isn't recorded. Not an original audit item (the audit counted 2 stale claims). |
| T2 | `design-tokens/components/alert-triage-queue.md` (Notes) | :28 — "No override-reason capture exists yet" | `raw/2025-08-26…:29` — "there was no way to note why they reprioritized"; `wireflows/alert-triage-override-reason-capture.md` is `status: in-review`. | Designed and in review, not built. Not an original audit item. |
| P11 | `user-flows/ambient-scribe-session-lock-recovery.md` | :48 — re-auth numbness "was part of why the current silent freeze reads as broken" | `raw/2026-02-17…:47-48` — "this framing gap likely drives the abandon-and-redictate behavior above as much as the missing UI does." | Uses the session's "likely drives". Adds an Evidence basis line. |
| P12–P14 | `personas/physician-longitudinal-scribe-user.md` | :32, :33-34, :35 — Goals presented as P09's | Goal 1: P09, `raw/2025-02-25…:36-37`, `raw/2025-09-23…:36-37`, `raw/2026-01-13…:36-37`. Goal 2: P22, `raw/2026-02-10…:51-53` — "this one's telling me specifically 'check the drug name'". Goal 3: P31 (P119 since `raw/2026-02-17-session-lock-during-dictation/correction-2026-10-13.md`) and P33, `raw/2026-02-17…:54-60`. | Each goal tagged with its source; goals 2–3 marked inferred, not observed for P09. |
| P15 | same | :43-45 — Post-GA stage as the persona's own experience | `raw/2026-02-10…:51-57` names P22 and P24; no raw session places P09 there (data gap 8). | Labeled "inferred from other participants", following `journey-maps/longitudinal-physician-ambient-scribe.md:14-16,28`. |
| P16–P17 | same | :48, :49-50 — Frustrations | P22 (`raw/2026-02-10…:51-53`); P31 (P119 since `raw/2026-02-17-session-lock-during-dictation/correction-2026-10-13.md`) and P33 (`raw/2026-02-17…:54-60`). | Each tagged as inferred, with its session. |
| P18 | same | :53 — "Longitudinal composite of participant P09 across the three sessions above, plus …" | As P15; no sessions are listed above. | Names P09's three sessions and says the 2026-02 material comes from other participants. Adds an Evidence basis line. |
| P19 | `mental-models/care-coordinator-alert-ranking.md` | :18-19 — "the system should defer to my sense of this patient's history-driven risk", in quotation marks | Not a raw quote. Closest: `raw/2025-08-26…:37` (P81) — "I wanted to tell it 'no, this one's more urgent because I know this patient's history,' but there was nowhere to put that." | Unquoted, presented as the designer's paraphrase, with P81 quoted. |
| P20 | same | :20 — "The model actually ranks by recency-weighted signals." | `raw/2025-08-26…:28` — "the model weighted 'recency' more heavily than coordinators' own sense of clinical risk" — what participants saw, not how the model works. | "Participants saw the ranking weight recency more heavily than their own sense of clinical risk". |
| P21 | same | :21 — "the queue doesn't surface its ranking basis" | Not recorded. | Deleted. Data gap 11. |
| P22 | same | :22-23 — "This mismatch, not raw ranking accuracy, is why 4 of 5 participants disagreed" | Not recorded; accuracy wasn't measured. | Deleted. Data gap 12. |
| P23 | same | :23 — "objectively faster than manual review" | `raw/2025-08-26…:30` — "faster with AI ranking present (avg 6.5 min) vs. chronological (avg 9 min) in this simulated test." | "faster … than with a chronological queue in this simulated test". Adds an Evidence basis line. |
| X4 | `research/findings/care-coordination-triage.md` | :34-37 — "The triage ranking works, but not for the reason initially expected"; disagreement because the model weighted recency over coordinators' "patient-history-driven risk" | `raw/2025-08-26-usability-test-alert-triage-ai-care-coordination/session-notes.md:28` — "4 of 5 participants disagreed with the AI's top-3 ranking on at least one of three test queues, generally because the model weighted 'recency' more heavily than coordinators' own sense of clinical risk"; `:30` — "faster with AI ranking present (avg 6.5 min) vs. chronological (avg 9 min) in this simulated test." | Bullet now says the AI-ranked queue was faster in a simulated test but most participants disagreed with its ranking; "clinical risk" and the raw's disagreement wording used. |
| X5 | `research/findings/clinician-experience-documentation-burden.md` | :51-52 — "suggesting it's a property of how these flagging models are currently tuned generally, not a one-off UI problem" | `raw/2025-08-26…:45` — "Share the override-capture idea with the Data Science team working on the care-gap flagging model (May findings) — likely the same underlying tuning problem." Neither session tested it, and nothing covers flagging models "generally". | Labeled as the August session's inference, quoting "likely the same underlying tuning problem"; "generally" dropped. |
| X6 | `user-flows/ambient-scribe-session-lock-recovery.md` | :47-48 — "clinicians already numb to frequent unrelated re-auth prompts" | `raw/2026-02-17-session-lock-during-dictation/session-notes.md:45-47` — "Clinicians already re-authenticate frequently for unrelated reasons (badge-tap SSO renewals); a lock during dictation is perceived as "one more annoying re-login," not as a distinct, expected safety behavior". | Uses the raw's wording. |

X1–X6 weren't in the original audit. X1–X3 repeat P2's record or the P6–P8
claims in other records; X4–X6 were noticed in the records phase 3b edited.

### Evidence basis line

The three Meridian design deliverables changed here (the physician
persona, the care-coordinator mental model and the session-lock user flow)
now open their first section with:

`**Evidence basis:** <Observed | Inferred | Illustrative | mixed>. <the raw path(s) and lines>.`

### Skipped

P24–P40 (17 items) sit in Fernway records that RR-161 removes:
`journey-maps/example-journey-map.md` (P24–P29),
`storyboards/example-storyboard.md` (P30–P34),
`personas/dana-overwhelmed-new-admin.md` (P35–P38) and
`mental-models/example-mental-model.md` (P39–P40). They aren't fixed.

### Deferred

Evidence basis lines for the other 10 non-Fernway design deliverables,
which haven't been audited yet: `mindsets/skeptical-verifier.md`,
`journey-maps/longitudinal-physician-ambient-scribe.md`,
`thumbnails/medication-flag-placement-explorations.md`,
`wireframes/ambient-scribe-medication-flag.md`,
`wireflows/alert-triage-override-reason-capture.md`,
`storyboards/ed-intake-peak-hour-interruption.md`,
`mockups/confidence-highlighted-draft-review.md`,
`prototypes/ambient-scribe-ga-candidate-clickthrough.md`,
`service-topology/prior-auth-drafting-v2.md` and
`design-system/v4-1-status-indicator-component.md`. **Audited 2026-10-15
(RR-165):** all ten are now claim-checked (see "RR-165 (v0.5.46)" below).
The thumbnails, mockup, prototype and v4-1 records now have Evidence basis
lines. The other six have suggested labels, recorded for their owner and
not applied.

### Noted, out of scope

- **P31 is two different people.** `raw/2025-05-20-interview-it-security-sso-mfa-modernization/session-notes.md:36,39`
  labels P31 "IT Security Engineer"; `raw/2026-02-17-session-lock-during-dictation/session-notes.md:56`
  labels P31 "Physician, Family Medicine". Like P17, this needs an
  append-only correction file. Not created here. **Made 2026-10-13:**
  `raw/2026-02-17-session-lock-during-dictation/correction-2026-10-13.md`
  gives that physician the ID P119.

## RR-165 (v0.5.46): claim check of the ten remaining Meridian design deliverables

### Scope and method

The ten records listed under Phase 3b's "Deferred". As in Method, every
factual claim was checked against the raw session lines it depends on. The
verdicts are the ones defined in Method, with one narrower meaning: STALE
here means the claim was qualified by later evidence, not that its author
got it wrong. So the fix for a STALE claim is an added "as of" note, not a
rewrite.

The audit ran at `main` `28098e4` and was applied in RR-165 parts 1–4.
Line numbers are the records' lines as at `28098e4`. The four records
changed in part 4 have since shifted. `raw/<date>…:<line>` means that
date's session folder, `session-notes.md`, unless another file is named.
Raw files haven't changed since `28098e4`; part 1 only added correction
files.

### Totals

| Record | Claims | Supported | Overreach | Unsupported | Stale | Labeled inference |
|---|---|---|---|---|---|---|
| `mindsets/skeptical-verifier.md` | 8 | 2 | 1 | 1 | 2 | 2 |
| `journey-maps/longitudinal-physician-ambient-scribe.md` | 10 | 7 | 3 | 0 | 0 | 0 |
| `thumbnails/medication-flag-placement-explorations.md` | 4 | 2 | 1 | 1 | 0 | 0 |
| `wireframes/ambient-scribe-medication-flag.md` | 6 | 4 | 2 | 0 | 0 | 0 |
| `wireflows/alert-triage-override-reason-capture.md` | 8 | 5 | 0 | 0 | 3 | 0 |
| `storyboards/ed-intake-peak-hour-interruption.md` | 9 | 4 | 1 | 2 | 0 | 2 |
| `mockups/confidence-highlighted-draft-review.md` | 6 | 3 | 1 | 1 | 1 | 0 |
| `prototypes/ambient-scribe-ga-candidate-clickthrough.md` | 1 | 0 | 0 | 1 | 0 | 0 |
| `service-topology/prior-auth-drafting-v2.md` | 7 | 2 | 1 | 3 | 1 | 0 |
| `design-system/v4-1-status-indicator-component.md` | 3 | 1 | 1 | 1 | 0 | 0 |
| **Total** | **62** | **30** | **11** | **10** | **7** | **4** |

32 claims are not SUPPORTED. 8 have been applied (part 4) and 24 are
pending for their owners.

### Claim ledger

R1–R62. Status is blank where no fix is needed.

**`mindsets/skeptical-verifier.md`**

| # | Line | Claim | Verdict | Raw evidence | Status |
|---|---|---|---|---|---|
| R1 | :13 | A segment that recurs across physicians, nurses and HIM coders | LABELED INFERENCE | `raw/2025-02-25…:31` — "4 of 5 participants read every line"; `raw/2025-04-08…:34` — "Show me where it got that info."; `raw/2025-07-29…:37` — "If you can't, I don't trust it." Three sessions; the cross-role segment is the designer's synthesis. | pending |
| R2 | :13-14 | "regardless of department or identity" | OVERREACH | No session compares departments or identities; "regardless" was never tested. | pending |
| R3 | :14-15 | "first named explicitly as a pattern in `him-coding-and-billing.md`" | UNSUPPORTED | Raised earlier, in prior-auth v1: `raw/2025-04-08…:31` — "'show your work' was mentioned unprompted by 3 of 4". | pending |
| R4 | :18-20 | Wants citations or a human-decision boundary for prior-auth and coding drafts | SUPPORTED | `raw/2025-04-08…:31`; `raw/2025-07-29…:28` | |
| R5 | :19-20 | Wants "confidence signals" | LABELED INFERENCE | `raw/2025-09-23…:43` is a recommendation — "explore an explicit confidence indicator per line"; `raw/2026-01-13…:36` — "it showed me exactly where to look instead." | pending |
| R6 | :18-20 | "Doesn't want AI output … auto-applied" | STALE | `raw/2026-06-23…:31` — "the suggested code would probably be accepted as shown unless something jumped out", tied "to the quota, not to trust in the tool"; `:33` — the citation is opened "only when a suggestion looks off". | pending |
| R7 | :20-21 | Default to visible, checkable provenance rather than accuracy alone | STALE | Later interviews describe errors the confidence underline doesn't mark: `raw/2026-03-19…:32` — incidental content "is not underlined"; `raw/2026-06-30…:31` and `raw/2026-07-28…:29` — "usually not underlined"; `raw/2026-09-22…:31` — "Those lines are usually not underlined". | pending |
| R8 | :21-23 | Accuracy improvements alone didn't change reading behavior | SUPPORTED | `raw/2025-09-23…:32` | |

**`journey-maps/longitudinal-physician-ambient-scribe.md`**

| # | Line | Claim | Verdict | Raw evidence | Status |
|---|---|---|---|---|---|
| R9 | :14-15 | Modeled on P09 in the three test rounds | SUPPORTED | `raw/2025-02-25…:37`, `raw/2025-09-23…:37`, `raw/2026-01-13…:37` | |
| R10 | :15-16 | Post-GA stage "inferred from other participants" in 2026-02-10 | OVERREACH (minor) | `raw/2026-02-10…/participants.md:27` — "Drawn from the existing GA-candidate cohort (2026-01-13) plus 2 new participants". P09 was in that cohort; whether P09 took part isn't recorded (data gap 8), so "other" is not established. | pending |
| R11 | :19-20 | v0.1: reads every line; P09's quote | SUPPORTED | `raw/2025-02-25…:36` | |
| R12 | :20-21 | Dosages missed or garbled in 3 of 5, disqualifying | SUPPORTED | `raw/2025-02-25…:30` | |
| R13 | :22-24 | v0.2: errors drop, still reads every line; P09's quote | SUPPORTED | `raw/2025-09-23…:31-32,:36` | |
| R14 | :25-26 | GA candidate: begins skimming high-confidence lines | SUPPORTED | `raw/2026-01-13…:36` | |
| R15 | :26-27 | Sound-alike names "a known, monitored gap" | OVERREACH | `raw/2026-01-13…:48` — "Set up post-GA monitoring dashboard" (a follow-up); `raw/2026-02-10…:71-72` — "once the post-GA monitoring dashboard (recommended 2026-01-13) has real error-rate data". Monitoring was recommended, not recorded as running. | pending |
| R16 | :28-29 | The medication flag "reads as more actionable" than generic highlighting | OVERREACH | `raw/2026-02-10…:36-39` — 5 of 6 identified it as "different from the usual low-confidence thing". Recognition, not actionability, was tested. | pending |
| R17 | :29-30 | Only if unflagged lines aren't over-trusted | SUPPORTED | `raw/2026-02-10…:40-42` | |
| R18 | :30-32 | Session lock: clinicians assumed the draft was lost | SUPPORTED | `raw/2026-02-17…:38-41,:54`; `correction-2026-09-27.md:41-43`; `correction-2026-10-13.md:33` | |

**`thumbnails/medication-flag-placement-explorations.md`**

| # | Line | Claim | Verdict | Raw evidence | Status |
|---|---|---|---|---|---|
| R19 | :18-19 | Inline pill won 5:1; participants didn't want to look away | SUPPORTED | `raw/2026-02-10…:44-45` | |
| R20 | :20 | Margin badge tested and lost | SUPPORTED | `raw/2026-02-10…:43-44` | |
| R21 | :20-21 | The margin badge "required a separate glance that broke reading flow" | OVERREACH (minor) | `raw/2026-02-10…:44-45` — "participants didn't want to look away from the text to check a flag". A stated preference, not an observed break in reading. | applied, PR #39 |
| R22 | :22-23 | A modal interrupt was "dropped before testing" | UNSUPPORTED | No file in `raw/2026-02-10…/` mentions a modal. | applied, PR #39 |

**`wireframes/ambient-scribe-medication-flag.md`**

| # | Line | Claim | Verdict | Raw evidence | Status |
|---|---|---|---|---|---|
| R23 | :21-22 | The flag was "validated in the 2026-02-10 concept test" | OVERREACH | `raw/2026-02-10…:70` — "Needs a larger-N validation pass before this moves from concept test to build-ready spec." | pending |
| R24 | :24 | Reads as "check this drug name" | SUPPORTED | `raw/2026-02-10…:51-52` | |
| R25 | :27-28 | Inline placement, 5:1 | SUPPORTED | `raw/2026-02-10…:44` | |
| R26 | :29-30 | Amber pill badge, distinct from the underline | SUPPORTED | `raw/2026-02-10…:37` | |
| R27 | :33-35 | Tip countering over-trust of unflagged lines (2 of 6) | SUPPORTED | `raw/2026-02-10…:62-64` | |
| R28 | :36-38 | False-positive testing suggests the threshold "can run looser than strict-precision defaults" | OVERREACH | `raw/2026-02-10…:46-48` — "One deliberately-seeded false positive … was accepted by all 6 participants"; "suggests some over-flagging is tolerable if the badge is visually light". | pending |

**`wireflows/alert-triage-override-reason-capture.md`**

| # | Line | Claim | Verdict | Raw evidence | Status |
|---|---|---|---|---|---|
| R29 | :13-14 | Overrides lose the "why" | SUPPORTED | `raw/2025-08-26…:29` | |
| R30 | :14-16 | The study recommended capture for the model and for agency | SUPPORTED | `raw/2025-08-26…:41` | |
| R31 | :16-17 | Supervisor's rubber-stamping concern | SUPPORTED | `raw/2025-08-26…:31` | |
| R32 | :21-22 | Patient-history risk and recency as reasons | SUPPORTED | `raw/2025-08-26…:37,:28` | |
| R33 | :24-26 | Skip-reason branch | SUPPORTED | `raw/2026-07-07…:31` — expected "they would skip the modal rather than type". | |
| R34 | :21-22 | The reason list as complete | STALE | `raw/2026-07-07…:30` — the most common reason, what the patient or family said on the phone, "isn't in the list"; `raw/2026-04-16…:32` — for discharge alerts, "time since discharge *is* the clinical risk". | pending |
| R35 | :22 | "other + free text" | STALE | `raw/2026-07-07…:31` — "They would not type free text on every override". | pending |
| R36 | :23 | Reasons logged for model tuning, "not surfaced to other coordinators" | STALE | `raw/2026-05-05…:31` — a supervisor "would also use override reasons for coaching" and the design "doesn't say whether supervisors see them"; `raw/2026-07-07…:32` — without seeing an effect "they would stop giving them". | pending |

**`storyboards/ed-intake-peak-hour-interruption.md`**

| # | Line | Claim | Verdict | Raw evidence | Status |
|---|---|---|---|---|---|
| R37 | :13 | Peak-hour ED shift | SUPPORTED | `raw/2025-04-22…:24` | |
| R38 | :13-14 | Interruptions every 2–4 minutes | SUPPORTED | `raw/2025-04-22…:29` | |
| R39 | :14 | Call lights, ambulance radio, a physician question | UNSUPPORTED | `raw/2025-04-22…:29` records "paged, walked up to, or called over". | pending |
| R40 | :17 | Panel 1: interrupted by a bedside alarm two questions in | LABELED INFERENCE | An invented scene; no session records it. | pending |
| R41 | :18-19 | Panel 2: "has lost track of where she was" | LABELED INFERENCE | An invented scene; no pronoun is recorded ("she" at :18). | pending |
| R42 | :20-21 | Panel 3: card photo, "pre-fill happens instantly" | UNSUPPORTED | `raw/2026-04-14…:49` — "Whether the insurance-card photo pre-fill … has been piloted is not recorded". | pending |
| R43 | :22-23 | Panel 4: the interruption rate, not AI quality | SUPPORTED | `raw/2025-04-22…:35` | |
| R44 | :24-25 | Carve out insurance-card pre-fill | SUPPORTED | `raw/2025-04-22…:47` | |
| R45 | :25 | "leave ED intake nursing out of near-term rollout" | OVERREACH | `raw/2025-04-22…:42` — "Deprioritize any AI feature aimed at ED intake nurses specifically during peak hours"; `raw/2026-05-19…:30` — the boundary "covers intake during peak, not the ED at every hour". | pending |

**`mockups/confidence-highlighted-draft-review.md`**

| # | Line | Claim | Verdict | Raw evidence | Status |
|---|---|---|---|---|---|
| R46 | :14-15 | Built for the Jan 2026 GA-candidate round | SUPPORTED | `raw/2026-01-13…:22` | |
| R47 | :15-17 | "the program's clearest trust-calibration result to date (visible uncertainty, not raw accuracy, changed reviewing behavior)" | OVERREACH | `raw/2026-01-13…:30` — "4 of 6 participants said it let them skim"; `:43` — the concept "appears to be the trust-building lever". | applied, PR #39 |
| R48 | :15-16 | The same result, read as current | STALE | `raw/2026-03-19…:32`, `raw/2026-06-30…:31`, `raw/2026-07-28…:29`, `raw/2026-09-22…:31` — errors that are "usually not underlined". | applied, PR #39 |
| R49 | :20-21 | High-confidence lines unmarked; low-confidence underlined | SUPPORTED | `raw/2026-01-13…:30` | |
| R50 | :21-22 | "an on-hover explanation"; "no separate medium-confidence tier" | UNSUPPORTED | `raw/2026-01-13…/` records neither a hover explanation nor tiers; `:30` describes only "a subtle underline". | applied, PR #39 |
| R51 | :23-24 | Avoids colour-only signaling | SUPPORTED | `raw/2025-03-10…:31` | |

**`prototypes/ambient-scribe-ga-candidate-clickthrough.md`**

| # | Line | Claim | Verdict | Raw evidence | Status |
|---|---|---|---|---|---|
| R52 | :17 | "Used for the Jan 13, 2026 usability round" | UNSUPPORTED | `raw/2026-01-13…:25` — "Moderated usability test, simulated + 2 real (consented) low-acuity encounters"; no prototype or build is named. | applied, PR #39 |

**`service-topology/prior-auth-drafting-v2.md`**

| # | Line | Claim | Verdict | Raw evidence | Status |
|---|---|---|---|---|---|
| R53 | :14-16 | v2 showed citations used, not ignored as friction | SUPPORTED | `raw/2025-11-04…:30` | |
| R54 | :19-22 | The backend chain (Chart-Data Service … Submission Service) | UNSUPPORTED | No raw session describes the backend. | pending |
| R55 | :20-22 | Payer-Rules Lookup "the fix that closed the v1 data-freshness bug" | UNSUPPORTED | `raw/2025-04-08…:46` — "confirm whether the outdated-code issue is a data-freshness bug or a model retrieval issue"; `raw/2025-11-04…:29` — the issue "did not recur". No session records the cause or the fix. | pending |
| R56 | :23-24 | Span-level citations are "why nurses could meaningfully check" one | OVERREACH | `raw/2025-11-04…:30` — "3 of 4 participants clicked into at least one citation"; no cause recorded. | pending |
| R57 | :22-24 | Nurse accepts/edits/rejects; checks a citation before accepting | STALE | `raw/2026-06-16…:30` — partway through a case "they stop using the draft and finish the case by hand"; `raw/2026-09-17…:30` — the v2 measure "records that a citation was opened, not what the nurse checked". | pending |
| R58 | :26-27 | Supports the pilot-expansion recommendation | SUPPORTED | `raw/2025-11-04…:39` | |
| R59 | :27-28 | The data-freshness fix "is now a tracked backend dependency" | UNSUPPORTED | Not in raw. | pending |

**`design-system/v4-1-status-indicator-component.md`**

| # | Line | Claim | Verdict | Raw evidence | Status |
|---|---|---|---|---|---|
| R60 | :16-17 | Replaces colour-only dots in `care-gap-badge` and `alert-triage-queue` | SUPPORTED | `accessibility-screenings/status-indicator-remediation-screening.md:22`; `raw/2025-11-18…:32` | |
| R61 | :18-19 | "the shared root behind the color-only pattern found in all three 2025 accessibility audits" | OVERREACH | The screening (`:22`, `:25`) covers two components. `raw/2025-11-18…:44` — "now found in 3 separate audits"; `:47` — "Confirm whether the color-only status issue has a single shared root component". `raw/2025-07-01…:29-32` records no colour-only finding. | applied, PR #39 |
| R62 | :24-25 | "satisfying 1.4.1" | UNSUPPORTED | No re-screen is recorded. | applied, PR #39 |

### What RR-165 changed

- **Part 1** — PR #36, merge `54ba503`. Three `correction-2026-10-15.md`
  files withdraw false "Synthesized into" lines: 2026-03-17 (P138) `:51`
  and 2026-09-15 (P143) `:51`, both for
  `ambient-scribe-post-ga-refinements.md`, and 2026-10-06 (P129) `:53` for
  `prior-authorization.md`. Also the count in `docs/README.md`.
- **Part 2** — PR #37, merge `131d882`. `--participants` became
  quote-aware; `docs/participants.md` wording and a label note; the
  Evidence basis definition and label definitions in
  `docs/deliverable-types.md`.
- **Part 3** — PR #38, merge `cbad3c7`. A 2026-02-10 Evidence Trail row in
  `ambient-scribe.md`; `rollout-and-change-management.md:69` dated to its
  October and December 2025 sources; in
  `scope-boundaries-and-workflow-fit.md`, the IT Security timeout now
  cites `raw/2026-02-17…:49-50` directly, plus a 2026-02-17 row.
- **Part 4** — PR #39, merge `c334cf6`. Thumbnails, mockup, prototype and
  v4-1: 8 claims fixed (R21, R22, R47, R48, R50, R52, R61, R62), and an
  Evidence basis line in each, all Mixed.

### Pending for owners

24 claims, not edited. The six records are do-not-edit or in review, so
the fixes below are suggestions for their designer, Sam Okafor, who
designed all six. Jordan Lee is the owner for
`ambient-scribe-post-ga-refinements.md`. Suggested Evidence basis labels
use only the four defined labels.

- **Mindset** (R1–R3, R5–R7). Suggested label: Inferred.
  - R1: label the cross-role segment as the designer's synthesis of three sessions.
  - R2: drop "regardless of department or identity"; name the roles seen.
  - R3: say the pattern was first raised in prior-auth v1 (`raw/2025-04-08…:31`).
  - R5: label confidence signals as inferred from the 2025-09-23 recommendation and the 2026-01-13 result.
  - R6: add an "as of" note on quota-driven acceptance (`raw/2026-06-23…:31,:33`).
  - R7: add an "as of" note that later interviews report errors the underline doesn't mark.
- **Journey map** (R10, R15, R16). Suggested label: Mixed.
  - R10: say P09's attendance at 2026-02-10 isn't recorded, rather than "other participants".
  - R15: "monitoring was recommended" instead of "monitored".
  - R16: "recognized as different from generic highlighting (5 of 6)" instead of "more actionable".
- **Wireframe** (R23, R28). Suggested label: Mixed.
  - R23: "tested in a 6-person concept test"; note the raw's call for a larger-N pass.
  - R28: state the single seeded false positive accepted by all 6, not a threshold conclusion.
- **Wireflow** (R34–R36). Suggested label: Mixed.
  - R34: "as of" note on the missing phone/family reason and on discharge alerts.
  - R35: "as of" note that free text may be skipped on busy days.
  - R36: "as of" note on supervisor visibility and coordinator feedback, both unsettled.
- **Storyboard** (R39–R42, R45). Suggested label: Mixed, with the scenario panels Illustrative.
  - R39: use the raw's "paged, walked up to, or called over".
  - R40, R41: label panels 1–2 as illustrative; "she" to "they".
  - R42: label panel 3 as illustrative; the pre-fill isn't recorded as piloted.
  - R45: "deprioritize during peak hours", per `raw/2025-04-22…:42`.
- **Topology** (R54–R57, R59). Suggested label: Mixed, with the backend chain Illustrative.
  - R54: label the backend chain as the designer's illustration.
  - R55: drop "the fix that closed"; the cause isn't recorded.
  - R56: state the v2 observation without "which is why".
  - R57: "as of" note on mid-case switches to manual and on what citation-opening measures.
  - R59: drop "now a tracked backend dependency", or source it.

### Decisions and known inconsistencies

- **Frontmatter `date` wasn't bumped by these edits.** This follows
  earlier audit edits: the persona, mental model and session-lock flow
  were revised 2026-10-08 to 2026-10-14 without a date change. Mismatches
  that remain:
  - Mindset: dated 2025-12-01, but `related_findings` links the post-GA finding dated 2026-02-17.
  - Thumbnails: dated 2026-02-08, reports the 2026-02-10 test.
  - Mockup: dated 2026-01-05, refers to the 2026-01-13 round.
  - Prototype: dated 2025-12-10, refers to the Jan 13 round.
  - v4-1: dated 2026-01-22, but `:28` describes `style-guide/foundations-v3.md`, dated 2026-02-28.
- **v4-1 `:27-29` untouched.** `docs/deliverable-types.md` classes
  `style-guide/foundations-v3.md` as Fernway, so `:28` becomes false if
  RR-161 removes it. It's plain text, so `build_index.py --check` wouldn't
  catch it.
- **Existing Evidence basis lines to revisit with their owners.**
  `user-flows/ambient-scribe-session-lock-recovery.md:23` is labelled
  Observed but says "The flow itself is a design response and hasn't been
  tested" (it could be Mixed). `personas/physician-longitudinal-scribe-user.md:25`
  is mixed in practice but opens with "Observed".
- **The screening's "three".**
  `accessibility-screenings/status-indicator-remediation-screening.md:25`
  says "one shared root cause, not three independent bugs", though the
  screening covers two components. And `raw/2025-11-18…:44` counts the
  pattern in three audits, while `raw/2025-07-01…:29-32` records no
  colour-only finding. This may need a raw correction; the corpus can't say
  which is wrong.

### Newer evidence not reflected in the pending six

- **Mindset.** `raw/2026-06-23…:31,:33,:36` (P125) partly contradicts it:
  "The quota wins. It always wins." `raw/2026-10-06…:32-33,:40` (P129),
  `raw/2026-09-17…:30,:34` (P144) and `raw/2026-10-13…:30,:37` (P145)
  support it. `raw/2026-05-28…:30,:37` (P140) qualifies it: acceptance from
  fatigue ("At hour twelve, if it hands me a paragraph, I'm going to sign
  it."). `raw/2026-03-17…:32` (P138) is a counter-pattern for readers of
  the note, who "assume the provider read it all".
  `raw/2026-03-24…:32-33` (P147) checks every medication change in the
  plan. `raw/2026-09-22…:34` (P09) trusts the scribe by section. Together
  these suggest a separate "reader" stance; the owner decides.
- **Journey map.** `raw/2026-09-22…:31-34` (P09's own post-GA account);
  `raw/2026-05-26…:32-33`; `raw/2026-04-28…:31-32`.
- **Wireframe.** `raw/2026-03-24…:32,:50`; `raw/2026-06-30…:31,:33,:50`.
  Whether the flag stays visible after signing is undecided and rests only
  on 2026-09-15 (P143), which is raw-only. Word it as an open design
  question and cite nothing new.
- **Wireflow.** `raw/2026-07-07…`, `raw/2026-05-05…`,
  `raw/2026-04-16…:32`, `raw/2026-08-04…:30`, `raw/2026-04-07…:33`,
  `raw/2026-09-01…:31`, `raw/2026-08-20…:32`.
- **Storyboard.** `raw/2026-04-14…:31-33`; `raw/2026-05-19…:30-31`.
- **Topology.** `raw/2026-06-16…:30-32,:43`;
  `raw/2026-09-17…:30-31,:43,:47`; `raw/2026-10-06…:45`.

### Impact on published answers (for RR-152)

Parts 1–4 changed no text that `answers.json` cites:
`capture-static-answers.js verify` reports the same 9 of 23 sources not
matching before and after. When the pending fixes land:

- **Journey map** (`all-scribe-draft-trust [1]`, checked span `:19-27`,
  stages 1–3; already a MISS). R15 at `:26-27` falls inside the span. R16
  at `:28-29` is stage 4, just after it.
- **Widget Notes `:31`** (`scribe-draft-retention [3]`,
  `component:ambient-scribe-widget#5`, currently matching). Changing
  "showed" to "suggested" would turn it into a MISS. The widget text is
  do-not-edit; the owner decides.
- **Mindset, wireframe, wireflow, storyboard, topology.** No answer cites
  `deliverable:mindsets/skeptical-verifier`,
  `deliverable:wireframes/ambient-scribe-medication-flag`,
  `deliverable:wireflows/alert-triage-override-reason-capture`,
  `deliverable:storyboards/ed-intake-peak-hour-interruption` or
  `deliverable:service-topology/prior-auth-drafting-v2`. No impact.

### Not in RR-165, still open

- Missing Evidence Trail rows for 2026-03-17 and 2026-09-15 in
  `ambient-scribe-post-ga-refinements.md` (do-not-edit; Jordan Lee).
- No 2026-02-17 rows in `ambient-scribe.md` or `governance-and-phi.md`,
  because no body claim comes from that session.
- Widget Notes `:31`: "showed" should read "suggested"
  (`raw/2025-09-23…:32` — "suggesting trust doesn't shift from accuracy
  improvements alone").
- `design-tokens/components/coding-suggestion-panel.md:21` is a generated
  line; fix it at the source, outside RR-165.
- Research deliverables (toplines, readouts, the heuristic evaluation, the
  accessibility screening) have no Evidence basis lines, by decision:
  RR-165 covers design deliverables only, and the GA adoption topline is
  do-not-edit.

## Not a corpus problem

- **Static answers.** Seven answers in the CRUD UI's `answers.json` cite
  text changed here and need a recapture. `capture-static-answers.js verify`
  reports 9 of 23 cited sources no longer matching, across:
  all-scribe-draft-trust, scribe-medication-flag, onboarding-calendar-step,
  scribe-draft-retention, all-documentation-burden, prior-auth-time-savings
  and all-coders-billing-suggestions. The last one is only the HIM
  finding's "she" changing to "they".
- **The session-lock correction file isn't shown anywhere** (the ticket for making correction files visible to retrieval).
  - The raw loader reads only `session-notes.md` and `participants.md`,
    so `search.html`, the CRUD UI record view, `export_records.py` and
    Ask all show the uncorrected "4 of 5 clinicians".
  - The finding's link to the correction is a plain relative href in both
    UIs.

## RR-195 (v0.5.47): Fernway audit items retired

### What was removed

RR-195 deletes the Fernway onboarding sample thread: 23 records in 24
files (the raw session is one record in two files). It was sample content
for a different product, added on 2026-09-14 in `2e29d87` ("Add
feature-002 deliverable folder scaffolding, tooling, and sample content"),
and never research. See `decisions.md` section 21 for the decision and
the `research/raw/` exception.

The 23 removed record IDs:

- `finding:onboarding`
- `analytics:onboarding-funnel-dropoff`
- `raw:2026-01-19-onboarding-usability-test`
- `deliverable:research-plans/onboarding-usability-study-q1`
- `deliverable:facilitation-guides/onboarding-usability-guide`
- `deliverable:topline-summaries/example-topline-summary`
- `deliverable:research-readouts/onboarding-flow-q1-readout`
- `deliverable:heuristic-evaluations/example-heuristic-evaluation`
- `deliverable:accessibility-screenings/example-accessibility-screening`
- `deliverable:service-topology/example-service-topology`
- `deliverable:personas/dana-overwhelmed-new-admin`
- `deliverable:mental-models/example-mental-model`
- `deliverable:mindsets/example-mindset`
- `deliverable:journey-maps/example-journey-map`
- `deliverable:thumbnails/example-thumbnail`
- `deliverable:wireframes/workspace-setup-step4-invite-team`
- `deliverable:user-flows/onboarding-flow`
- `deliverable:wireflows/example-wireflow`
- `deliverable:storyboards/example-storyboard`
- `deliverable:mockups/example-mockups`
- `deliverable:prototypes/example-prototype`
- `deliverable:style-guide/foundations-v3`
- `deliverable:design-system/example-design-system`

### Items retired

Every item below points at one of the removed files, so it is closed by
the removal, not fixed. Line numbers are the ones quoted earlier in this
file.

| Items | Count | Section | Points at |
|---|---|---|---|
| A7–A9 | 3 | Fixed, cited | `topline-summaries/example-topline-summary.md` |
| A10–A11 | 2 | Fixed, cited | `research/findings/onboarding.md` |
| A12–A13 | 2 | Fixed, cited | `research-readouts/onboarding-flow-q1-readout.md` (A13 also names `analytics/summaries/onboarding-funnel-dropoff.md`) |
| B1–B2 | 2 | Fixed, not cited | `research/findings/onboarding.md` |
| B3–B5 | 3 | Fixed, not cited | `research-readouts/onboarding-flow-q1-readout.md` |
| Link fix for the example topline | 1 | Link fixes | `topline-summaries/example-topline-summary.md` |
| Data gaps 1–5 | 5 | Data gaps | the removed raw session, topline, readout and funnel summary (gap 4 is the funnel export the removed summary described) |
| Data gap 6 | 1 | Data gaps | `facilitation-guides/onboarding-usability-guide.md` |
| Data gap 7 | 1 | Data gaps | `personas/dana-overwhelmed-new-admin.md` |
| Audit items P24–P29 | 6 | Phase 3b, Skipped | `journey-maps/example-journey-map.md` |
| Audit items P30–P34 | 5 | Phase 3b, Skipped | `storyboards/example-storyboard.md` |
| Audit items P35–P38 | 4 | Phase 3b, Skipped | `personas/dana-overwhelmed-new-admin.md` |
| Audit items P39–P40 | 2 | Phase 3b, Skipped | `mental-models/example-mental-model.md` |

Totals: A7–A13 (7), B1–B5 (5), data gaps 1–7 (7), audit items P24–P40
(17) and the one link-fix row. Audit items P24–P40 are this file's Phase
3b claim IDs. They are unrelated to participants P24 and P33 in
`research/participants.yml`, which stay registered.

B2, B4, B5 and the link-fix row were not in RR-195's list. They point at
removed records too, so they are retired here.

"Logged, not changed", Design deliverables:

- "Onboarding journey map" and "Onboarding storyboard" point only at
  removed records (they became P24–P29 and P30–P34). Retired.
- "Both mental models" and "Both personas" are mixed. The Fernway half of
  each (P39–P40, P35–P38) is retired. The Meridian half
  (`mental-models/care-coordinator-alert-ranking.md`, P19–P23, and
  `personas/physician-longitudinal-scribe-user.md`, P12–P18) was handled
  in Phase 3b and is unaffected.

The RR-165 note that `design-system/v4-1-status-indicator-component.md`
`:28` described `style-guide/foundations-v3.md` was resolved before this
removal: RR-194 part 3 rewrote that note and pointed `related_style_guide`
at `style-guide/meridian-token-basics.md`.

### What remains

The Meridian corpus still has at least one record of every deliverable
type the removed records demonstrated. The onboarding study (RR-191 to
RR-194) covers 12 of the 20 types; other Meridian projects cover the other
8: heuristic evaluations, accessibility screenings, service topology,
thumbnails, mockups, prototypes, design system and style guide. The chain
the removed records were the only example of is now:

- research plan: `research-plans/compass-ai-practice-setup-study-q1.md`
- facilitation guide:
  `facilitation-guides/compass-ai-practice-setup-usability-guide.md`
- readout: `research-readouts/compass-ai-practice-setup-q1-readout.md`
- style guide: `style-guide/meridian-token-basics.md`
- analytics summary: `analytics/summaries/compass-ai-practice-setup-funnel.md`

These were written from their own raw sessions and are not rewrites of
the removed records, so none of the retired items carries over to them.
