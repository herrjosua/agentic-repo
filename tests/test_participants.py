"""
Participant registry (docs/participants.md, RR-155): research/participants.yml records one entry
per person, keyed by a global participant ID. build_index.py validates it against every
"> — <role>, P<nn>" attribution line in raw/*/session-notes.md and fails when one ID is attributed
to two different people; new_research_session.py --participants allocates IDs from it. Without
participants.yml the feature is off entirely.
"""
import os
import subprocess

import frontmatter
import pytest
import yaml
from conftest import PYTHON, REAL_REPO_ROOT, write_file

SESSION_A = "2026-01-05-session-a"
SESSION_B = "2026-02-05-session-b"
SESSION_C = "2026-03-05-session-c"
NEW_SESSION = "2026-04-01-login-interview"

REGISTRY = f"""\
    # Registry comment that must survive edits.
    next_id: P04

    role_classes:
      - physician
      - app
      - care-coordinator
      - it

    participants:
      P01:
        role_class: care-coordinator
        appearances:
          - session: {SESSION_A}
            role: Care Coordinator
      P02:
        role_class: physician
        appearances:
          - session: {SESSION_A}
            role: Physician, Internal Medicine
          - session: {SESSION_B}
            role: Physician, Internal Medicine
            returning: true
      # P03 comment, kept above its entry.
      P03:
        role_class: app
        appearances:
          - session: {SESSION_B}
            role: Nurse Practitioner
    """


def session_notes(folder, *quotes):
    body = "\n\n".join(f'> "Quote."\n{q}' for q in quotes)
    return f"""\
---
title: {folder}
date: {folder[:10]}
type: interview
status: raw
tags: [onboarding]
related_components: []
related_findings:
  - ../../findings/onboarding.md
---

# {folder}

## Representative Quotes
{body}
"""


def add_session(root, folder, *quotes):
    path = root / "research/raw" / folder / "session-notes.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(session_notes(folder, *quotes), encoding="utf-8")


def append_quote(root, folder, quote):
    with open(root / "research/raw" / folder / "session-notes.md", "a", encoding="utf-8") as f:
        f.write(f'\n> "Another quote."\n{quote}\n')


def edit(path, old, new):
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{old!r} not in {path}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def registry(root):
    return root / "research/participants.yml"


def append_registry(root, text):
    with open(registry(root), "a", encoding="utf-8") as f:
        f.write(text)


@pytest.fixture
def participants_repo(fake_repo, run_script):
    """fake_repo with two quoted sessions and a registry that matches them, indexes fresh."""
    add_session(fake_repo, SESSION_A, "> — Care Coordinator, P01", "> — Physician, Internal Medicine, P02")
    add_session(fake_repo, SESSION_B, "> — Physician, Internal Medicine, P02 (returning from session A)",
                "> — Nurse Practitioner, P03 (new participant)")
    write_file(fake_repo, "research/participants.yml", REGISTRY)
    result = run_script("build_index.py")
    assert result.returncode == 0, result.stderr
    return fake_repo


def build(run_script, *args):
    result = run_script("build_index.py", *args)
    assert "Traceback" not in result.stderr
    return result


# --- clean and optional -----------------------------------------------------------------------

def test_clean_registry_passes_silently(run_script, participants_repo):
    for args in ([], ["--check"]):
        result = build(run_script, *args)
        assert result.returncode == 0, result.stderr
        assert result.stderr == ""


def test_without_registry_nothing_is_checked(run_script, fake_repo):
    # Two different people on one ID, but no participants.yml: the feature is off.
    add_session(fake_repo, SESSION_A, "> — Care Coordinator, P01")
    add_session(fake_repo, SESSION_B, "> — IT Security Engineer, P01")
    build(run_script)
    result = build(run_script, "--check")
    assert result.returncode == 0, result.stderr
    assert "articipant" not in result.stderr


# --- errors -----------------------------------------------------------------------------------

def _two_people_one_id(root):
    # The P31 case: an ID reused for a different person, with no returning marker.
    append_quote(root, SESSION_B, "> — IT Security Engineer, P01")


def _returning_different_class(root):
    add_session(root, SESSION_C, "> — Nurse Practitioner, P02 (returning from session A)")


def _same_session_two_roles(root):
    add_session(root, SESSION_C, "> — Nurse Practitioner, P09", "> — Physician, Internal Medicine, P09")


def _returning_in_earliest_session(root):
    edit(registry(root), "        role: Nurse Practitioner\n",
         "        role: Nurse Practitioner\n        returning: true\n")
    edit(root / f"research/raw/{SESSION_B}/session-notes.md", "P03 (new participant)", "P03 (returning from v1)")


def _registered_role_differs(root):
    edit(root / f"research/raw/{SESSION_A}/session-notes.md", "> — Care Coordinator, P01",
         "> — Care Coordinator Supervisor, P01")


def _raw_marker_not_in_registry(root):
    edit(root / f"research/raw/{SESSION_B}/session-notes.md", "P03 (new participant)", "P03 (returning)")


def _registry_returning_without_raw_marker(root):
    edit(root / f"research/raw/{SESSION_B}/session-notes.md", "P02 (returning from session A)", "P02")


def _unquoted_appearance(root):
    edit(registry(root), "  P03:", f"""  P01b:
    role_class: app
    appearances:
      - session: {SESSION_B}
        role: Nurse Practitioner
  P03:""")


def _unquoted_appearance_valid_id(root):
    edit(registry(root), "next_id: P04", "next_id: P05")
    append_registry(root, f"""  P04:
    role_class: app
    appearances:
      - session: {SESSION_B}
        role: Physician Assistant
""")


def _stale_session(root):
    edit(registry(root), f"      - session: {SESSION_A}\n        role: Care Coordinator",
         "      - session: 2026-09-09-gone\n        role: Care Coordinator")


def _corrected_by_missing(root):
    edit(registry(root), "        role: Care Coordinator\n",
         "        role: Care Coordinator\n        raw_role: Care Coordinator\n"
         "        corrected_by: correction-2026-01-06.md\n")


def _raw_id_without_corrected_by(root):
    edit(registry(root), "        role: Care Coordinator\n",
         "        role: Care Coordinator\n        raw_id: P01\n")


def _duplicate_key(root):
    append_registry(root, f"""  P01:
    role_class: it
    appearances:
      - session: {SESSION_C}
        role: IT Security Engineer
""")


def _unknown_role_class(root):
    edit(registry(root), "role_class: app", "role_class: wizard")


def _next_id_too_low(root):
    edit(registry(root), "next_id: P04", "next_id: P03")


def _unknown_key(root):
    edit(registry(root), "role_class: app", "role_class: app\n    rank: 3")


def _unparseable(root):
    edit(registry(root), "next_id: P04", "next_id: [P04")


@pytest.mark.parametrize("mutate, message", [
    (_two_people_one_id, "different role and no returning marker"),
    (_returning_different_class, "marked returning, but role class physician vs app"),
    (_same_session_two_roles, "attributed to different roles in one session"),
    (_returning_in_earliest_session, "this is its earliest session"),
    (_registered_role_differs, "P01 is 'Care Coordinator Supervisor' here but 'Care Coordinator'"),
    (_raw_marker_not_in_registry, "P03 is marked returning here but not in participants.yml"),
    (_registry_returning_without_raw_marker, "has no \"(returning from ...)\" marker here"),
    (_unquoted_appearance, "'P01b' isn't a participant ID"),
    (_unquoted_appearance_valid_id, "P04 in 2026-02-05-session-b has no attribution line"),
    (_stale_session, "session '2026-09-09-gone' isn't a raw session folder"),
    (_corrected_by_missing, "corrected_by 'correction-2026-01-06.md' isn't a correction-*.md file"),
    (_raw_id_without_corrected_by, "raw_id/raw_role needs corrected_by"),
    (_duplicate_key, "duplicate key"),
    (_unknown_role_class, "role_class 'wizard' isn't in role_classes"),
    (_next_id_too_low, "P03: is at or above next_id P03"),
    (_unknown_key, "unknown key 'rank'"),
    (_unparseable, "participants.yml: unparseable"),
])
@pytest.mark.parametrize("check", [False, True], ids=["write", "check"])
def test_registry_problem_exits_1(run_script, participants_repo, mutate, message, check):
    mutate(participants_repo)
    result = build(run_script, *(["--check"] if check else []))
    assert result.returncode == 1
    assert message in result.stderr


# --- warnings ---------------------------------------------------------------------------------

def _returning_new_label(root):
    add_session(root, SESSION_C, "> — Physician, Family Medicine, P02 (returning from session A)")
    edit(registry(root), "        returning: true\n", f"""        returning: true
      - session: {SESSION_C}
        role: Physician, Family Medicine
        returning: true
""")


def _later_same_role_unmarked(root):
    add_session(root, SESSION_C, "> — Nurse Practitioner, P03")
    append_registry(root, f"""\
      - session: {SESSION_C}
        role: Nurse Practitioner
""")


def _unverified_sequence(root):
    edit(registry(root), "role_class: app", "role_class: app\n    note: unverified-sequence")


def _below_baseline(root):
    edit(registry(root), "next_id: P04", "next_id: P04\nsequence_baseline:\n  date: 2026-01-31\n  first_id: P04")


@pytest.mark.parametrize("mutate, message", [
    (_returning_new_label, "returning, same role class, different role label"),
    (_later_same_role_unmarked, "same role in a later session with no returning marker"),
    (_unverified_sequence, "P03 is out of chronological sequence (note: unverified-sequence)"),
    (_below_baseline, "P03 first appears after 2026-01-31 but is below the baseline's first_id P04"),
])
def test_warning_never_fails(run_script, participants_repo, mutate, message):
    mutate(participants_repo)
    build(run_script)  # a new session C changes the index
    result = build(run_script, "--check")
    assert result.returncode == 0, result.stderr
    assert "Participant ID warnings" in result.stderr
    assert message in result.stderr


def test_registry_append_helpers_land_under_the_right_entry(participants_repo):
    """The warning helpers append to P03's list (the last entry) and P02's; make sure the YAML
    the warning tests rely on parses the way they assume."""
    _later_same_role_unmarked(participants_repo)
    data = yaml.safe_load(registry(participants_repo).read_text(encoding="utf-8"))
    assert [a["session"] for a in data["participants"]["P03"]["appearances"]] == [SESSION_B, SESSION_C]
    _returning_new_label(participants_repo)
    data = yaml.safe_load(registry(participants_repo).read_text(encoding="utf-8"))
    assert [a["session"] for a in data["participants"]["P02"]["appearances"]] == [SESSION_A, SESSION_B, SESSION_C]


# --- unregistered attributions ----------------------------------------------------------------

def test_unregistered_attribution_warns_then_check_fails(run_script, participants_repo):
    append_quote(participants_repo, SESSION_B, "> — Patient, P05")
    message = f"research/raw/{SESSION_B}/session-notes.md:"
    result = build(run_script)
    assert result.returncode == 0, result.stderr
    assert "Participant IDs not in research/participants.yml" in result.stderr
    assert message in result.stderr and "P05 (Patient)" in result.stderr
    result = build(run_script, "--check")
    assert result.returncode == 1
    assert "P05 (Patient)" in result.stderr
    assert "out of date" not in result.stderr


# --- corrections ------------------------------------------------------------------------------

CORRECTION = """\
---
title: Correction
date: 2026-02-06
type: interview
status: raw
tags: [onboarding]
related_components: []
related_findings: []
---

`session-notes.md` says:

> "Quote."
> — Physician, Family Medicine, P01

**Correct ID:** Physician, Family Medicine, P04.
"""


def test_raw_id_correction_is_honored(run_script, participants_repo):
    """The P31 -> P119 case: session-notes.md reuses P01 for a different person; a correction file
    gives them P04, and the registry mirrors it. The correction file quotes the wrong line, which
    must not be parsed."""
    append_quote(participants_repo, SESSION_B, "> — Physician, Family Medicine, P01")
    result = build(run_script)
    assert result.returncode == 1
    assert "different role and no returning marker" in result.stderr

    write_file(participants_repo, f"research/raw/{SESSION_B}/correction-2026-02-06.md", CORRECTION)
    edit(registry(participants_repo), "next_id: P04", "next_id: P05")
    append_registry(participants_repo, f"""  P04:
    role_class: physician
    appearances:
      - session: {SESSION_B}
        role: Physician, Family Medicine
        raw_id: P01
        corrected_by: correction-2026-02-06.md
""")
    for args in ([], ["--check"]):
        result = build(run_script, *args)
        assert result.returncode == 0, result.stderr
        assert result.stderr == ""


def test_raw_role_correction_is_honored(run_script, participants_repo):
    """The P17 case: session-notes.md drops part of the role; the registry holds the corrected
    role, with raw_role matching what the raw line says."""
    edit(participants_repo / f"research/raw/{SESSION_A}/session-notes.md", "> — Care Coordinator, P01",
         "> — Coordinator, P01")
    assert build(run_script).returncode == 1
    write_file(participants_repo, f"research/raw/{SESSION_A}/correction-2026-01-06.md",
               CORRECTION.replace("2026-02-06", "2026-01-06"))
    edit(registry(participants_repo), "        role: Care Coordinator\n",
         "        role: Care Coordinator\n        raw_role: Coordinator\n"
         "        corrected_by: correction-2026-01-06.md\n")
    result = build(run_script, "--check")
    assert result.returncode == 0, result.stderr


# --- new_research_session.py --participants ----------------------------------------------------

def new_session(run_script, *args):
    return run_script("new_research_session.py", "--title", "Login interview", "--type", "interview",
                      "--topic-slug", "login-interview", "--date", "2026-04-01", "--tags", "onboarding",
                      "--related-findings", "onboarding.md", *args)


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_participants_allocates_ids_and_build_index_is_clean(run_script, participants_repo):
    result = new_session(run_script, "--participants", "Medical Coder=it, Care Coordinator",
                         "--participants", "P02")
    assert result.returncode == 0, result.stderr
    assert "Participant IDs: P04, P05, P02 (returning from 2026-02-05-session-b)" in result.stdout

    data = yaml.safe_load(registry(participants_repo).read_text(encoding="utf-8"))
    assert data["next_id"] == "P06"
    assert data["participants"]["P04"] == {"role_class": "it", "appearances": [
        {"session": NEW_SESSION, "role": "Medical Coder", "reserved": True}]}
    assert data["participants"]["P05"] == {"role_class": "care-coordinator", "appearances": [
        {"session": NEW_SESSION, "role": "Care Coordinator", "reserved": True}]}
    assert data["participants"]["P02"]["appearances"][-1] == {
        "session": NEW_SESSION, "role": "Physician, Internal Medicine", "returning": True, "reserved": True}

    folder = participants_repo / "research/raw" / NEW_SESSION
    roster = frontmatter.load(folder / "participants.md").content
    assert "**Count:** 3" in roster
    assert "- P04 — Medical Coder (it)\n- P05 — Care Coordinator (care-coordinator)\n" in roster
    assert "- P02 — Physician, Internal Medicine (physician), returning from 2026-02-05-session-b" in roster
    notes = frontmatter.load(folder / "session-notes.md").content
    assert "> — Medical Coder, P04\n" in notes
    assert "> — Physician, Internal Medicine, P02 (returning from 2026-02-05-session-b)" in notes

    assert build(run_script).returncode == 0
    result = build(run_script, "--check")
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""


def test_participants_keeps_registry_comments_and_layout(run_script, participants_repo):
    before = registry(participants_repo).read_text(encoding="utf-8")
    assert new_session(run_script, "--participants", "P01, Nurse Practitioner").returncode == 0
    after = registry(participants_repo).read_text(encoding="utf-8")
    assert "# Registry comment that must survive edits.\n" in after
    # P01's new appearance goes inside P01's entry, above P02 — not after the next entry's comment.
    assert after.index(NEW_SESSION) < after.index("\n  P02:") < after.index("  # P03 comment")
    # Every original line is still there, in order.
    remaining = iter(after.splitlines())
    assert all(any(line == other for other in remaining) for line in before.replace("next_id: P04", "next_id: P05").splitlines())


@pytest.mark.parametrize("spec, message", [
    ("Medical Coder", "'Medical Coder' isn't in the registry yet; give it as Medical Coder=<class>"),
    ("Medical Coder=wizard", "'wizard' isn't a role class"),
    ("P77", "P77 isn't in research/participants.yml"),
    ("P01, P01", "P01 is listed twice"),
    ("=it", "needs a role label"),
    ("Physician P12=physician", "needs a role label with no participant ID in it"),
])
def test_bad_participants_writes_nothing(run_script, participants_repo, spec, message):
    before = snapshot(participants_repo)
    result = new_session(run_script, "--participants", spec)
    assert result.returncode == 1
    assert message in result.stderr
    assert "Traceback" not in result.stderr
    assert snapshot(participants_repo) == before


def test_participants_without_registry_writes_nothing(run_script, fake_repo):
    before = snapshot(fake_repo)
    result = new_session(run_script, "--participants", "Nurse=nurse")
    assert result.returncode == 1
    assert "research/participants.yml doesn't exist" in result.stderr
    assert snapshot(fake_repo) == before


def test_participants_and_participants_roles_are_exclusive(run_script, participants_repo):
    before = snapshot(participants_repo)
    result = new_session(run_script, "--participants", "P01", "--participants-roles", "Nurse")
    assert result.returncode == 1
    assert snapshot(participants_repo) == before


def test_template_uses_global_ids(run_script, fake_repo):
    assert new_session(run_script).returncode == 0
    folder = fake_repo / "research/raw" / NEW_SESSION
    roster = (folder / "participants.md").read_text(encoding="utf-8")
    assert "session-scoped" not in roster
    assert "research/participants.yml" in roster and "never reused for a different person" in roster
    notes = (folder / "session-notes.md").read_text(encoding="utf-8")
    assert "> — Role, participant ID (a global ID from research/participants.yml" in notes


# --- the real corpus --------------------------------------------------------------------------

def test_real_repo_passes_check_with_only_the_known_sequence_warnings():
    """Read-only: --check never writes. The four out-of-sequence IDs (P22, P24, P33, P41) are
    treated as new participants and recorded as unverified-sequence; there is no source in the
    repo to verify them, so they stay warnings."""
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"}
    result = subprocess.run([PYTHON, str(REAL_REPO_ROOT / "research/scripts/build_index.py"), "--check"],
                            cwd=REAL_REPO_ROOT, env=env, capture_output=True, text=True, timeout=120,
                            stdin=subprocess.DEVNULL)
    assert result.returncode == 0, result.stderr
    assert "Participant registry issues" not in result.stderr
    assert "not in research/participants.yml" not in result.stderr
    warnings = [line.strip() for line in result.stderr.splitlines() if "out of chronological sequence" in line]
    assert [w.split()[1] for w in warnings] == ["P22", "P24", "P33", "P41"]
    assert result.stderr.count("\n   ") == 4


def test_real_registry_covers_every_attribution():
    import build_index
    data = build_index.load_participants()
    attributions = build_index.load_attributions()
    assert len(attributions) == 63
    assert len(data["participants"]) == 48
    assert data["next_id"] == "P127"
    p119 = data["participants"]["P119"]["appearances"][0]
    assert (p119["raw_id"], p119["corrected_by"]) == ("P31", "correction-2026-10-13.md")
    p17 = data["participants"]["P17"]["appearances"][0]
    assert (p17["raw_role"], p17["corrected_by"]) == ("Utilization Review Nurse", "correction-2026-10-13.md")
