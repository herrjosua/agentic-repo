# Decision Log

One entry per project decision: when it was made, whether it still holds, what was decided, and
why. Entries are numbered in the order they were logged, not by date, and are never renumbered.
When a decision changes, mark the old entry **Superseded** with a pointer to the entry that
replaces it, and add the new one at the end.

Where a date or a rationale was never written down, the entry says "not recorded" rather than
reconstructing it. **(unconfirmed)** marks a date or rationale that was inferred or drafted after
the fact and hasn't been confirmed by the project owner.

This log is about the repo and its tooling. Decisions about the product the corpus studies live
as decision records in [`../decisions/`](../decisions/_index.md) (see
[Decision records](deliverable-types.md#decision-records-decisions)).

Seeded on 2026-09-30 from §9 ("Decisions locked in") of
[`agentic-ux-research-repo-plan.md`](agentic-ux-research-repo-plan.md) and the project's earlier
decision log, whose decisions and rationales are copied here in their recorded wording.

| # | Decision | Date | Status |
|---|---|---|---|
| 1 | [Design tokens live in the same repo](#1-design-tokens-live-in-the-same-repo) | by 2026-09-13 | Active |
| 2 | [Repo shape mirrors the existing work layout](#2-repo-shape-mirrors-the-existing-work-layout) | by 2026-09-13 | Active |
| 3 | [Tags are explicit and validated against a glossary](#3-tags-are-explicit-and-validated-against-a-glossary) | by 2026-09-13 | Active |
| 4 | [`AGENTS.md` is the single source of agent instructions](#4-agentsmd-is-the-single-source-of-agent-instructions) | by 2026-09-13 | Active |
| 5 | [Analytics gets its own top-level folder](#5-analytics-gets-its-own-top-level-folder) | by 2026-09-13 | Active |
| 6 | [Every deliverable type gets its own top-level folder](#6-every-deliverable-type-gets-its-own-top-level-folder) | 2026-09-14 | Active |
| 7 | [External-tool artifacts are stubs; prototypes share one folder](#7-external-tool-artifacts-are-stubs-prototypes-share-one-folder) | 2026-09-14 | Active |
| 8 | [Fictional sample content is checked against real repo conventions](#8-fictional-sample-content-is-checked-against-real-repo-conventions) | 2026-09-14 | Active |
| 9 | [Windows setup docs are general-purpose only](#9-windows-setup-docs-are-general-purpose-only) | 2026-09-14 | Active |
| 10 | [Corpus changes are authored in this repo only, on a branch](#10-corpus-changes-are-authored-in-this-repo-only-on-a-branch) | 2026-09-22 (unconfirmed) | Active |
| 11 | [Demo isolation: a separate repo and a scoped sync workflow](#11-demo-isolation-a-separate-repo-and-a-scoped-sync-workflow) | 2026-09-16 | Active |
| 12 | [MIT license and technical-only READMEs](#12-mit-license-and-technical-only-readmes) | not recorded | Active |
| 13 | [Decisions are tracked outside the repo](#13-decisions-are-tracked-outside-the-repo) | 2026-09-14 | Superseded by 15 |
| 14 | [Retrieval is two paths over one source of truth](#14-retrieval-is-two-paths-over-one-source-of-truth) | 2026-09-30 | Active |
| 15 | [The repos are the source of truth and hold enough to build](#15-the-repos-are-the-source-of-truth-and-hold-enough-to-build) | 2026-09-30 | Active |
| 16 | [Participant IDs live in one central registry](#16-participant-ids-live-in-one-central-registry) | 2026-10-13 | Active |
| 17 | [Participant IDs follow allocation order, not session date](#17-participant-ids-follow-allocation-order-not-session-date) | 2026-10-14 | Active |
| 18 | [Who counts as a nurse in the RR-124 interviews](#18-who-counts-as-a-nurse-in-the-rr-124-interviews) | 2026-10-14 | Active |
| 19 | [Who counts as a physician, NP or PA in the RR-124 interviews](#19-who-counts-as-a-physician-np-or-pa-in-the-rr-124-interviews) | 2026-10-15 | Active |
| 20 | [Release tags go on merge commits and are pushed alone](#20-release-tags-go-on-merge-commits-and-are-pushed-alone) | 2026-10-15 | Active |
| 21 | [The Fernway onboarding sample thread is retired](#21-the-fernway-onboarding-sample-thread-is-retired) | 2026-10-16 | Active |
| 22 | [Product decisions are their own record kind](#22-product-decisions-are-their-own-record-kind) | 2026-10-04 | Active |

---

## 1. Design tokens live in the same repo

- **Date:** by 2026-09-13 (present in the plan snapshot of that date)
- **Status:** Active
- **Decision:** Design tokens live in the same repo as research, in their own top-level
  `design-tokens/` folder next to `research/`, not in a separate repo.
- **Why:** Different update cadence and source of truth (Figma vs. research notes), but keeping
  one repo lets a finding reference a component file by relative path without crossing repo
  boundaries. Matches the work repo's existing root layout.

## 2. Repo shape mirrors the existing work layout

- **Date:** by 2026-09-13 (present in the plan snapshot of that date)
- **Status:** Active
- **Decision:** The repo keeps a root `docs/`, a `research/` folder (raw + findings + scripts),
  and sibling top-level folders for other content types.
- **Why:** Matches the shape already in use on the work repo (plan §3; see also entry 1). No
  further rationale is recorded.

## 3. Tags are explicit and validated against a glossary

- **Date:** by 2026-09-13 (present in the plan snapshot of that date)
- **Status:** Active
- **Decision:** Every file carries frontmatter tags, and every tag must exist in the canonical
  glossary, `research/findings/tags.md`. `build_index.py --check` fails on an undefined tag.
- **Why:** Without a glossary, tags drift into near-duplicates (`onboarding` vs. `first-run` vs.
  `first-time-user`) over months of use (plan §3).

## 4. `AGENTS.md` is the single source of agent instructions

- **Date:** by 2026-09-13 (present in the plan snapshot of that date)
- **Status:** Active
- **Decision:** `AGENTS.md` at the repo root is the canonical agent-instruction file; `CLAUDE.md`
  is a one-line import of it (`@AGENTS.md`). No `.github/copilot-instructions.md` until a GitHub
  Copilot seat exists.
- **Why:** `AGENTS.md` is the broadest-compatibility format; Claude Code is the holdout that only
  reads `CLAUDE.md`. An Office 365 subscription provides Microsoft 365 Copilot, which doesn't read
  repo instruction files, so only Claude Code reads this repo for now.

## 5. Analytics gets its own top-level folder

- **Date:** by 2026-09-13 (present in the plan snapshot of that date)
- **Status:** Active
- **Decision:** Analytics/quant data goes in a top-level `analytics/` folder (`raw/`,
  `summaries/`, `_index.md`, `scripts/`), not in a `type: analytics` finding. Findings and
  analytics summaries cross-link via `related_analytics` / `related_findings` frontmatter.
  (`analytics` remains a valid `type` for a raw research session; see
  [`docs/README.md`](README.md).)
- **Why:** Same rationale as `design-tokens/`: different cadence (pulled from a platform, not
  written after a session) and a different source of truth (the platform). `analytics` was
  dropped from the finding `type` enum because it described a data source, not a research method.

## 6. Every deliverable type gets its own top-level folder

- **Date:** 2026-09-14
- **Status:** Active
- **Decision:** Each notional deliverable type (research and design) gets its own top-level
  folder, rather than grouping several types under one folder.
- **Why:** Keeps each artifact type independently queryable and filterable, and matches the
  existing pattern of sibling top-level folders (`design-tokens/`, `analytics/`) that have
  different cadences and sources of truth than `research/`.

## 7. External-tool artifacts are stubs; prototypes share one folder

- **Date:** 2026-09-14
- **Status:** Active
- **Decision:**
  - For artifact types whose real content lives in an external tool (Figma click-through
    prototypes, GitHub-hosted coded prototypes, and eventually Confluence or Word content), the
    repo folder holds a lightweight Markdown stub (frontmatter with `source_type` and a link,
    plus a short description) instead of duplicating the full artifact.
  - Click-through (Figma) and coded (GitHub) prototypes share one `prototypes/` folder, with a
    `type` frontmatter field distinguishing them, instead of two separate top-level folders.
- **Why:**
  - Stubs: keeps folders small and queryable without becoming an unmanageable pile of full design
    files, based on direct past-project experience with a huge, hard-to-manage design-file
    folder.
  - One prototypes folder: both reduce to the same shape (a thin stub pointing at an external
    tool, with no real duplicated content), so filtering works via metadata rather than folder
    path; a separate folder wasn't adding anything.

## 8. Fictional sample content is checked against real repo conventions

- **Date:** 2026-09-14
- **Status:** Active
- **Decision:** Before treating fictional sample content as finished, check it against the
  repo's actual conventions and existing dataset, not just internal self-consistency:
  (1) reference values (`related_findings`, `related_analytics`) must match real filenames, not
  invented IDs; (2) tags must respect the canonical glossary's own guidance (for example,
  `tags.md` warns against onboarding/first-run drift); (3) fictional entity and product names
  must be grepped against the full dataset for collisions before use (the original name for the
  Fernway scenario collided with the existing Meridian Health Network dataset and was renamed
  after confirming no collisions, including near-misses).
- **Why:** The first pass of the Fernway sample content made three separate mistakes of this kind
  (invented reference IDs, a tag pairing the glossary calls out as drift, and a product name
  colliding with an existing fictional entity), and none were caught until the build and
  validation pass surfaced them one at a time. A standing checklist stops the next person
  repeating them.

## 9. Windows setup docs are general-purpose only

- **Date:** 2026-09-14
- **Status:** Active
- **Decision:** `SETUP.md` documents standard, general-purpose Windows setup (venv activation,
  `python` vs `python3`, PowerShell execution policy, `.gitattributes` for line endings), not
  tailored to any specific company or client IT environment. Git Bash and the standard Python
  installer are the assumed baseline tools.
- **Why:** A generic Windows setup guide is broadly useful and correct for a typical unrestricted
  machine; pre-documenting every possible company or client IT restriction (admin rights,
  software catalogs, proxy/VPN blocks, locked-down execution policy) without having hit them would
  be guessing.
- **Note:** Written 2026-09-30 as [`SETUP.md`](SETUP.md); the Windows section is untested.

## 10. Corpus changes are authored in this repo only, on a branch

- **Date:** 2026-09-22 (unconfirmed; inferred: the CRUD UI's decision log records an incident on
  that date that led to a push-disabled dev clone)
- **Status:** Active
- **Decision:** Every corpus change is authored in the real agentic-repo checkout, on a branch,
  with its checks run before merge. The `agentic-repo-dev` clone is a push-disabled read-only
  copy used by the CRUD UI backend, the evaluation harness and the capture script; never edit
  content there.
- **Why:** The dev clone exists so other tools read a stable corpus baseline; the harness refuses
  to run if it isn't clean and records its commit in every result. Editing content there would
  let it diverge from the source of truth.

## 11. Demo isolation: a separate repo and a scoped sync workflow

- **Date:** 2026-09-16
- **Status:** Active
- **Decision:** The public demo runs against a dedicated, isolated demo repo, never the real
  agentic-repo. An hourly job on the demo server fetches tags, hard-resets the demo checkout to
  the baseline tag and rebuilds the index, restoring content between visitors; the demo server
  holds only a fetch-only credential for the demo repo (no write access, no access to the real
  repo at all). Content is synced from the real repo to the demo repo by a GitHub Actions
  workflow (scheduled, plus manual dispatch) that lives in the real repo: it checks out the real
  repo with the default token, pushes curated content to the demo repo using a fine-grained token
  scoped only to the demo repo (contents read and write, with expiration, stored as an Actions
  secret), then moves the baseline tag. The demo user account (separate database) is untouched by
  the reset. See [`demo-deploy.md`](demo-deploy.md) and `AGENTS.md` → "Demo repo sync".
- **Why:** Since research content lives in git, a public demo visitor could delete or vandalize
  real records and break the demo for everyone after them. Resetting a clone of the real repo
  directly would also mean the public demo server needs read (or worse, write) credentials to the
  real repo, and a credential leak there could expose or endanger real content. A fully separate
  demo repo means the demo server's credentials can never reach the real repo even in a worst
  case, and gives a natural point to redact anything not meant for public eyes before it's
  synced.

## 12. MIT license and technical-only READMEs

- **Date:** not recorded
- **Status:** Active
- **Decision:** Both the agentic-repo and CRUD UI repos are MIT licensed
  ([`LICENSE`](../LICENSE)), with an AI-assisted-development disclosure in each README. READMEs
  and docs cover only how the project is configured, built, run and deployed; deployment info
  stays general (not host-specific) and includes no protected data such as SSH keys.
- **Why:** Both are portfolio pieces built with Claude, so the disclosure is stated openly;
  keeping docs technical and generic avoids leaking host details or secrets.

## 13. Decisions are tracked outside the repo

- **Date:** 2026-09-14
- **Status:** Superseded by [15](#15-the-repos-are-the-source-of-truth-and-hold-enough-to-build)
  (2026-09-30)
- **Decision:** Project decisions were tracked in a private log outside the repo.
- **Why (as recorded then):** Kept the repo's own docs purely operational (how to run things)
  rather than mixing in rationale.

## 14. Retrieval is two paths over one source of truth

- **Date:** 2026-09-30
- **Status:** Active
- **Decision:** An agent working in the repo searches `findings/` and the index first (grep/glob +
  frontmatter tags), and goes to `raw/` only to verify or quote. Separately, the CRUD UI's Ask the
  Repo answers researchers' questions through a local model with embeddings. The repo stays the
  only source of truth for both.
- **Why (drafted 2026-09-30 from the plan and the Ask the Repo evaluation; unconfirmed):** The
  original plan expected keyword and index search to be enough at this scale and reserved
  embeddings for a real scaling problem. Ask the Repo was added as a separate app. Measuring it on
  a 17-question gold set showed most failures were retrieval's (the needed evidence never reached
  the prompt) and that larger local models did not help, so the stance is to keep the repo simple
  and put the retrieval work in the app.

## 15. The repos are the source of truth and hold enough to build

- **Date:** 2026-09-30
- **Status:** Active
- **Decision:** The repos are the source of truth and must contain enough for someone to build the
  project from them alone. Private specifics (server addresses and access details, account
  details, credentials) stay out of the repos. The public demo's URL is public. Supersedes
  [13](#13-decisions-are-tracked-outside-the-repo).
- **Why (drafted 2026-09-30 from the documentation baseline; unconfirmed):** Documents kept in
  several places drifted apart (the plan existed in two copies, ticket statuses contradicted the
  code). One canonical place per fact removes the question of which copy to trust.

## 16. Participant IDs live in one central registry

- **Date:** 2026-10-13
- **Status:** Active
- **Decision:** Participant IDs (P01, P02, ...) are one global sequence, one ID per person, and
  are recorded in one central file, `research/participants.yml`, modeled on
  `research/projects.yml`. Each entry lists the person's role class and every session they
  appear in. `build_index.py --check` validates it against the attribution lines in
  `raw/*/session-notes.md`. A `participants.yml` sidecar inside each raw session folder was
  considered and rejected. See [`participants.md`](participants.md).
- **Why:** `raw/` is append-only. A sidecar would mean adding a file to all 30 existing session
  folders, and every correction would then live in two places in `raw/`. A central file, like
  `projects.yml`, holds the metadata the raw files can't carry, so no raw file has to change. It
  also gives one place to allocate the next free ID, which stops an ID being reused for a
  different person. P17 and P31 both went wrong this way (RR-124), and both were fixed by
  correction files on 2026-10-13. The RR-155 ticket called IDs "session-scoped", but in practice
  they are global.

## 17. Participant IDs follow allocation order, not session date

- **Date:** 2026-10-14
- **Status:** Active
- **Decision:** From P130 on, participant IDs follow the order `new_research_session.py
  --participants` allocates them, not the order of session dates. A session can be dated earlier
  than one with a lower ID: a session dated 2026-03-03 can carry P130 while one dated 2026-03-10
  carries P120. Each RR-124 phase allocates its IDs as one contiguous block. `note:
  unverified-sequence` stays only for the four pre-registry participants (P22, P24, P33, P41) and
  is never used for an ID allocated from P130 on. `sequence_baseline` is unchanged; it is a floor,
  not an ordering rule. See [`participants.md`](participants.md#id-order).
- **Why:** The RR-124 phases cover the same March to October 2026 window one user type at a time,
  so keeping IDs in date order would force each phase's IDs to be interleaved with the others'.
  `build_index.py` never checked date order: its sequence checks cover only the
  `unverified-sequence` note and the `sequence_baseline` floor, so a backdated P130 raises
  nothing. For IDs allocated from the registry, the git history of `participants.yml` records the
  allocation order, which the four legacy IDs don't have.

## 18. Who counts as a nurse in the RR-124 interviews

- **Date:** 2026-10-14
- **Status:** Active
- **Decision:** A participant in the RR-124 nurse interviews (Phase 3) is a licensed RN whose main
  job is direct nursing care on a unit or in a clinic (inpatient, ED, ICU, ambulatory, infusion),
  frontline nursing leadership of that care (charge nurse, nurse manager), or nurse-specific
  clinical review (utilization review). Their role class is `nurse`. Excluded: RN case managers,
  transitions or discharge nurses, nurse navigators and social workers, whose work is
  coordination; nurse practitioners and physician assistants, who are `app` and belong to Phase 4;
  LPNs and LVNs; and nurse informatics. See [`participants.md`](participants.md#role-classes).
- **Why:** The phases interview one user type at a time, so the line between nurses and care
  coordinators has to be drawn once and written down. Phase 2 (care coordinators) already left
  out RN case managers and social workers, but that exclusion was previously recorded only in the
  RR-124 ticket, not in this repo. The `nursing` tag means the registered nurse population
  specifically, which rules out LPNs and LVNs. Nurse informatics staff configure the tools rather
  than use them in patient care, which makes them stakeholders rather than end users.

## 19. Who counts as a physician, NP or PA in the RR-124 interviews

- **Date:** 2026-10-15
- **Status:** Active
- **Decision:** A participant in the RR-124 physician, NP and PA interviews (Phase 4) is a licensed
  physician, nurse practitioner or physician assistant in direct patient care who signs their own
  notes. Physicians are role class `physician`; NPs and PAs are `app`, and each is labelled by their
  own role. Residents and fellows count, labelled as residents or fellows. Hospitalists and ED
  physicians are in the class too. An RN who is training as an NP, or an NP working in an RN job,
  is classed by the job they do: `nurse`, under decision 18. Excluded: locum clinicians; medical
  directors, CMIOs, CMOs and physician informaticists, who are stakeholders (`executive`, covered
  in `governance-and-phi.md`); pharmacists; human medical scribes; behavioral health clinicians,
  including psychiatrists, because behavioral health is excluded from the ambient scribe rollout
  (`scope-boundaries-and-workflow-fit.md`); and CRNAs and nurse-midwives. Separately, Phase 4's
  sampling is ambulatory only: there are no inpatient, ED or behavioral health sessions, and those
  settings stay honest gaps. See [`participants.md`](participants.md#role-classes).
- **Why:** The phases interview one user type at a time, so the line has to be drawn once and
  written down, as decision 18 did for nurses. The ambient scribe drafts visit notes for physicians,
  NPs and PAs, so the people who review and sign those drafts are the users this phase is about.
  The 2026-01-27 dashboard review found residents opting in less than attendings and asked for a
  qualitative follow-up, so residents can't be left out. Directors and informaticists configure or
  govern the tools rather than sign notes with them. Whether the scribe is used in inpatient or ED
  settings isn't recorded, so sessions there would have to invent it; they stay gaps rather than
  being sampled.

## 20. Release tags go on merge commits and are pushed alone

- **Date:** 2026-10-15
- **Status:** Active
- **Decision:** Version labels (vX.Y.Z) are ticket labels on the project board, and a release tag
  is an annotated tag on the merge commit that completes the work or phase, with the ticket key
  and a one-line summary. Each tag is created and pushed alone (`git push origin
  refs/tags/vX.Y.Z`, never `--tags`), only when Josh says, with no backfill of earlier versions
  and no CHANGELOG. The first tag is `v0.5.44`, on `1f41a67`. See
  [Versions and tags](../README.md#versions-and-tags).
- **Why:** The convention was recorded only outside the repo, and decision 15 puts it here. Tag
  side effects were verified before the first tag was pushed: `ci.yml` does not run on a tag push,
  because its push trigger is limited to `main`; `sync-demo.yml` has no push or release trigger
  and does not read tags. The `demo-baseline` tag it moves lives in `research-repo-demo` and is
  unrelated.

## 21. The Fernway onboarding sample thread is retired

- **Date:** 2026-10-16
- **Status:** Active
- **Decision:** The Fernway onboarding sample thread (23 records in 24 files: the `onboarding`
  finding, the `onboarding-funnel-dropoff` analytics summary, the raw session
  `2026-01-19-onboarding-usability-test`, and 20 deliverables including the persona
  `dana-overwhelmed-new-admin`, the `foundations-v3` style guide and the `example-*` files) is
  removed in RR-195 and must not be re-created. No deliverable folder is required to hold a
  record, and no sample, placeholder or invented-product record is created to fill one (see
  [`deliverable-types.md`](deliverable-types.md)). This is an exception to the append-only rule
  for `research/raw/`, covering only the Fernway raw session
  `research/raw/2026-01-19-onboarding-usability-test/`, approved by Josh on 2026-10-13: it was
  sample content added with the deliverable scaffolding, never research, so deleting it is not an
  edit to evidence. Every other raw folder stays append-only. Decision 8 stays in force: its
  name-collision grep still runs before new names are used. `tests/test_retired_names.py` fails
  if a retired name or path comes back.
- **Why:** RR-190 found that an earlier removal was undone. On 2026-09-13, `c6e6352` ("Code
  cleanup. Removing files that Claude mistakenly created.") deleted the first onboarding finding
  and analytics summary, and `0582525` (`05825257155ed845594139db12bcdad71ca3d5a8`, "Remove
  contamination: orphaned onboarding/ambient-scribe dummy data") removed the references left
  behind. On 2026-09-14, `2e29d87` (`2e29d87d8511eeda36b8d5546088788f1eabc04e`, "Add feature-002
  deliverable folder scaffolding, tooling, and sample content") added the thread back, because a
  spec said every deliverable folder needs a sample. The thread was about a different product,
  yet search, Ask and the gold set treated it as Meridian research. The Meridian corpus still has
  at least one record of every deliverable type the thread demonstrated: the onboarding study
  (RR-191 to RR-194) covers 12 of the 20 types, and other Meridian projects cover the other 8
  (heuristic evaluations, accessibility screenings, service topology, thumbnails, mockups,
  prototypes, design system and style guide). The spec text is
  rewritten in RR-195 and the guard test stops a repeat. The removal and the audit items it
  retires are recorded in [`synthesis-audit-2026-09-29.md`](synthesis-audit-2026-09-29.md).

## 22. Product decisions are their own record kind

- **Date:** 2026-10-04; schema approved 2026-10-23 (RR-157)
- **Status:** Active
- **Decision:** Decisions about the product live as decision records in a top-level `decisions/`
  folder, as their own record kind (`decision:<slug>`), not as a deliverable folder or a section
  inside findings. Each record carries a document `status` and a separate `decision_status`
  (proposed, accepted, shipped, reversed, superseded, not-decided). Every field is either sourced
  from a named record's lines or written as "not recorded". Evidence cites raw sessions directly.
  The schema and its checks are in
  [Decision records](deliverable-types.md#decision-records-decisions). Not to be confused with this
  log, which covers the repo itself.
- **Why:** The RR-153 corpus audit traced 8 decisions and found none recorded an owner, a decision
  date or a status, so Ask could give a rationale but never say what wasn't recorded. A record
  kind with explicit "not recorded" fields lets it. RR-153 decision 4 chose a record kind over a
  section inside findings. Raw evidence is linked directly because the CRUD UI's provenance links
  are read from a record's html and don't follow a finding to its raw sessions.
