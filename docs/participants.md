# Participant IDs

Every research participant has one participant ID (`P01`, `P02`, ... `P132`). IDs come from one
global sequence across every raw session. They are **not** session-scoped, and an ID is never
reused for a different person. A participant who takes part in a later session keeps their ID.

The participants and researchers in this corpus are fictional. IDs stand in for names, so no real
patient or staff identity is ever recorded.

## The registry

The machine-readable source is [`research/participants.yml`](../research/participants.yml). It
lives under `research/` so `sync-demo.yml` copies it to the demo repo. It has one entry per person,
keyed by their ID:

```yaml
next_id: P120
participants:
  P09:
    role_class: physician
    appearances:
      - session: 2025-02-25-usability-test-ambient-scribe-v01
        role: Physician, Internal Medicine
      - session: 2025-09-23-usability-test-ambient-scribe-v02
        role: Physician, Internal Medicine
        returning: true
```

| Field | Where | Meaning |
|---|---|---|
| `next_id` | top level | The next ID to allocate. Every ID in the registry is below it, so an ID is never handed out twice. |
| `sequence_baseline` | top level | `date` and `first_id`: an ID first used in a session dated after `date` should be `first_id` or higher (a warning, not an error). |
| `role_classes` | top level | The controlled vocabulary below. |
| `role_class` | entry | The person's role class. One per person. |
| `note` | entry | Optional. `unverified-sequence`: a new participant (no returning marker) whose ID is out of chronological order. There is no source in the repo to verify it. |
| `appearances` | entry | One item per raw session folder the person appears in. |
| `session` | appearance | The raw session folder name. |
| `role` | appearance | The role label, exactly as the attribution line in that session's `session-notes.md` writes it (or the corrected label, see below). |
| `returning` | appearance | `true` if this person took part in an earlier session. |
| `reserved` | appearance | `true` if `new_research_session.py --participants` allocated it. A reserved appearance doesn't have to be quoted. |
| `raw_id` / `raw_role` | appearance | What `session-notes.md` says, when a correction file changed it. |
| `corrected_by` | appearance | The `correction-*.md` file in that session folder that made the change. Required with `raw_id` or `raw_role`. |

IDs that were never quoted in any raw session (`P04`, `P06`, ...) aren't in the registry: nothing
records who they were, and the registry doesn't invent it. `next_id` alone stops them being reused.

Survey respondent IDs (`P07`, `P41`, `P44`, `P58`, `P84`, `P91`, `P112`) are recorded the same way
as any other quoted ID. How future surveys number their respondents is out of scope for now.

## Role classes

A role class is a coarse grouping, used to tell a returning participant from a different person
who happens to share an ID. The free-text `role` stays alongside it, because the class alone is too
coarse ("Chief Privacy Officer" and "Chief Information Officer" are both `executive`).

| Class | Covers (labels in use) |
|---|---|
| `physician` | Physician; Physician, Internal Medicine; Physician, Family Medicine |
| `app` | Advanced practice providers: Nurse Practitioner, Physician Assistant |
| `nurse` | Registered Nurse; ED Intake Nurse; Utilization Review Nurse (± supervisor); Behavioral Health Unit Charge Nurse |
| `care-coordinator` | Care Coordinator (± float pool; ± transitions of care); Care Coordinator Supervisor |
| `him-coder` | HIM Specialist (± Release of Information); HIM Supervisor; Medical Coder (± certified; ± senior); Coding Auditor; Clinical Documentation Integrity Specialist; Revenue Cycle Analyst (Billing) |
| `behavioral-health` | Behavioral Health Clinician |
| `patient` | Patient; Patient portal user |
| `executive` | Chief Information / Medical Information / Privacy Officer; VP Clinical Informatics; Director of Clinical Training & Education |
| `it` | IT Security Engineer; IT Security; IT Admin |
| `accessibility` | Accessibility Specialist |
| `admin-staff` | ED Registration Clerk; non-clinical/administrative staff |
| `clinician` | Clinician, role not specified |
| `mixed-staff` | Survey buckets spanning several roles ("Clinical staff (various)") |

Nurse practitioners and physician assistants are `app`, not `physician`. Most ambient-scribe
sessions mix physicians and NPs, and a physician's ID reused for an NP is exactly the collision the
check should catch.

`him-coder` covers the whole HIM coding side, including CDI specialists and revenue-cycle analysts.

The class belongs to the participant, never to the session. A session with several roles needs
nothing extra: its classes are just the classes of the people in it.

## Quotes and returning participants

A quote in `session-notes.md` is attributed on its own line:

```
> "Quote."
> — Physician, Internal Medicine, P09 (returning from v0.1)
```

That is: `> — <role>, <ID>`, then an optional note in parentheses. A note starting with
"returning" marks a returning participant. New sessions write it as `(returning from <session
folder>)`. Older sessions use free text ("returning from January", "returning from v0.1"); the
registry's `appearances` list records which sessions those are.

A quote with no "returning" note is a new participant. That is how the P31 correction read it:
`raw/2026-02-17-session-lock-during-dictation/correction-2026-10-13.md`.

## Corrections

`raw/` is append-only, so a wrong ID or role is fixed with a `correction-YYYY-MM-DD.md` file in
the session folder (see `AGENTS.md`). The correction file stays the authority. The registry mirrors
it:

- **Wrong role (P17):** `role` holds the corrected label, `raw_role` what `session-notes.md`
  says, and `corrected_by` names the correction file.
- **Wrong ID (P31 → P119):** the entry is keyed by the corrected ID, `raw_id` holds the ID
  `session-notes.md` uses, and `corrected_by` names the correction file.

`build_index.py` never parses correction files: they quote the wrong attribution they correct, so
parsing them would bring the error back.

## What `build_index.py` checks

`build_index.py` reads every attribution line in `raw/*/session-notes.md` and compares it with the
registry. If `research/participants.yml` doesn't exist, none of this runs.

**Errors** fail any run, not just `--check`:

- The registry's shape: unknown keys, duplicate keys, an ID that isn't `P` plus digits, a role
  class outside the vocabulary, an ID at or above `next_id`, a session folder that doesn't exist, a
  session listed twice under one ID, `raw_id`/`raw_role` without `corrected_by`, or a
  `corrected_by` that isn't a `correction-*.md` file in that folder.
- A quote whose role doesn't match the registry, or whose returning marker disagrees with it (the
  registry can say `returning: true` without a raw marker only when a correction added it, so
  `corrected_by` is required).
- An appearance with no quote in its session, unless it's `reserved: true`.
- The collision rules:

| Case | Result |
|---|---|
| Same ID, same session, different roles | Error |
| Later session, different role, no returning marker | Error (two people share the ID) |
| Later session, returning marker, different role class | Error |
| Returning marker on the ID's earliest session | Error |
| Later session, returning marker, same class, different label | Warning |
| Later session, same role, no returning marker | Warning |

**Warnings** never fail:

- An entry with `note: unverified-sequence`. These are P22, P24 (2026-02-10), P33 (2026-02-17) and
  P41 (2025-02-11). Each is treated as a new participant, because no returning marker means new,
  and is recorded as `unverified-sequence` because its ID is out of chronological order. There is
  no source in the repo to verify them, so they stay warnings.
- An ID first used after `sequence_baseline.date` but below its `first_id`.

**A quote whose ID isn't registered** warns on a normal run (what the CRUD UI reruns after each
edit) and fails under `--check`, the same way an unmapped project does.

## Adding participants to a new session

One raw folder per session (one per interview, for interview studies). Let
`new_research_session.py` allocate the IDs:

```bash
python research/scripts/new_research_session.py --title "Coder interview 1" --type interview \
  --topic-slug coder-interview-01 --tags him --related-findings him-coding-and-billing.md \
  --participants "Medical Coder=him-coder, Care Coordinator, P17"
```

- `Label=class` gives a new participant the next free ID.
- A bare label that's already in the registry under one class reuses that class. A label the
  registry hasn't seen needs `=class`.
- An existing ID is a returning participant. They keep their class and the role from their latest
  appearance.
- Labels can't contain commas. Use parentheses instead: `Physician (Internal Medicine)=physician`.
  The flag can be repeated.
- Every entry is checked before anything is written. An unknown label, class or ID exits with an
  error and creates nothing.

The script then:

- adds a `reserved: true` appearance for each participant and bumps `next_id`, inserting lines
  rather than rewriting the file, so comments survive;
- lists the IDs in the new `participants.md` roster;
- pre-fills one quote stub per participant in `session-notes.md`, with `(returning from <folder>)`
  for a returning participant.

Change the role on a quote line only if you change the registry entry to match. Delete the stubs
you don't use; a reserved appearance needs no quote.

Not using the script? Add the entries to `participants.yml` by hand: take IDs from `next_id` and
bump it. `build_index.py --check` fails until every quoted ID is registered.

## Superseded wording

The participants.md files created before RR-155 say IDs are "session-scoped". That was never true
in practice, and this page supersedes it. Those files are in `raw/` and stay as they are; nothing
rewrites them. New sessions get the corrected wording from `new_research_session.py`.
