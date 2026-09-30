# Decision Log

One entry per project decision: when it was made, whether it still holds, what was decided, and
why. Entries are numbered in the order they were logged, not by date, and are never renumbered.
When a decision changes, mark the old entry **Superseded** with a pointer to the entry that
replaces it, and add the new one at the end.

Where a date or a rationale was never written down, the entry says "not recorded" rather than
reconstructing it. **(unconfirmed)** marks a date or rationale that was inferred or drafted after
the fact and hasn't been confirmed by the project owner.

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
