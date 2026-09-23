"""
build_index.py — the CRUD UI backend (and research/scripts/reset_demo.sh) reruns this after
writes to refresh research/_index.md, analytics/_index.md, and each deliverable folder's
_index.md. --check is the CI gate.
"""
import re
import shutil

import pytest

from conftest import RAW_SESSION, write_file

INDEXES = [
    "research/_index.md",
    "analytics/_index.md",
    "personas/_index.md",
    "journey-maps/_index.md",
]


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def build(run_script, *args):
    return run_script("build_index.py", *args)


def edit(path, old, new):
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{old!r} not in {path}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def add_raw_session(root, folder, date_line, related_finding):
    write_file(root, f"research/raw/{folder}/session-notes.md", f"""\
        ---
        title: {folder}
        {date_line}
        type: interview
        status: raw
        tags: [onboarding]
        related_components: []
        related_findings:
          - ../../findings/{related_finding}
        ---

        # {folder}
        """)


# --- clean corpus ------------------------------------------------------------------------------

def test_clean_corpus_writes_all_indexes_and_exits_0(run_script, fake_repo):
    result = build(run_script)
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    for rel in INDEXES:
        assert (fake_repo / rel).is_file(), rel
    # Deliverable folders that don't exist in the checkout are not created.
    assert not (fake_repo / "wireframes").exists()


def test_research_index_row(run_script, fake_repo):
    build(run_script)
    text = (fake_repo / "research/_index.md").read_text(encoding="utf-8")
    assert (
        "| [Onboarding](findings/onboarding.md) | onboarding, usability | cta-primary "
        f"| onboarding-funnel.md | 2026-01-20 | raw/{RAW_SESSION}/ |"
    ) in text


def test_analytics_index_row(run_script, fake_repo):
    build(run_script)
    text = (fake_repo / "analytics/_index.md").read_text(encoding="utf-8")
    assert (
        "| [Onboarding funnel](summaries/onboarding-funnel.md) | amplitude | onboarding "
        "| ../research/findings/onboarding.md | 2026-01-21 |"
    ) in text


def test_deliverable_index_row(run_script, fake_repo):
    build(run_script)
    text = (fake_repo / "personas/_index.md").read_text(encoding="utf-8")
    assert text.startswith("# Personas Index\n")
    assert (
        "| [New User](new-user.md) | draft | onboarding | native | 2026-01-22 "
        "| ../research/findings/onboarding.md |"
    ) in text
    assert "_index" not in text.split("|---|")[-1]  # _index.md never indexes itself


def test_second_run_is_idempotent(run_script, fake_repo):
    build(run_script)
    mtimes = {rel: (fake_repo / rel).stat().st_mtime_ns for rel in INDEXES}
    result = build(run_script)
    assert result.returncode == 0
    assert result.stdout.count("already up to date") == len(INDEXES)
    assert {rel: (fake_repo / rel).stat().st_mtime_ns for rel in INDEXES} == mtimes


def test_raw_sessions_backing_a_finding_sorted_by_date(run_script, fake_repo):
    add_raw_session(fake_repo, "2025-12-01-early-interview", "date: 2025-12-01", "onboarding.md")
    build(run_script)
    text = (fake_repo / "research/_index.md").read_text(encoding="utf-8")
    assert f"raw/2025-12-01-early-interview/, raw/{RAW_SESSION}/" in text


def test_rows_sorted_by_date(run_script, fake_repo):
    write_file(fake_repo, "research/findings/checkout.md", """\
        ---
        title: Checkout
        date: 2025-06-01
        tags: [usability]
        ---
        """)
    add_raw_session(fake_repo, "2025-05-01-checkout", "date: 2025-05-01", "checkout.md")
    result = build(run_script)
    assert result.returncode == 0, result.stderr
    text = (fake_repo / "research/_index.md").read_text(encoding="utf-8")
    assert text.index("[Checkout]") < text.index("[Onboarding]")


# --- --check -----------------------------------------------------------------------------------

def test_check_on_stale_repo_exits_1_and_writes_nothing(run_script, fake_repo):
    before = snapshot(fake_repo)
    result = build(run_script, "--check")
    assert result.returncode == 1
    for rel in INDEXES:
        assert f"{rel} is out of date" in result.stderr
    assert snapshot(fake_repo) == before


def test_check_on_fresh_repo_exits_0(run_script, fake_repo):
    build(run_script)
    before = snapshot(fake_repo)
    result = build(run_script, "--check")
    assert result.returncode == 0, result.stderr
    assert snapshot(fake_repo) == before


def test_check_detects_drift_after_edit(run_script, fake_repo):
    build(run_script)
    edit(fake_repo / "research/findings/onboarding.md", "title: Onboarding", "title: Onboarding v2")
    result = build(run_script, "--check")
    assert result.returncode == 1
    assert "research/_index.md is out of date" in result.stderr


# --- validators --------------------------------------------------------------------------------

def _unknown_tag(root):
    edit(root / "research/findings/onboarding.md", "  - usability\n", "  - usability\n  - not-a-tag\n")


def _unknown_tag_in_deliverable(root):
    edit(root / "personas/new-user.md", "tags: [onboarding]", "tags: [onboarding, not-a-tag]")


def _dangling_raw_related_findings(root):
    add_raw_session(root, "2026-02-01-dangling", "date: 2026-02-01", "nope.md")


def _unbacked_finding(root):
    write_file(root, "research/findings/orphan.md", "---\ntitle: Orphan\ndate: 2026-01-01\ntags: []\n---\n")


def _missing_related_analytics(root):
    edit(root / "research/findings/onboarding.md", "  - onboarding-funnel.md", "  - onboarding-funnel.md\n  - gone.md")


def _analytics_dangling_finding(root):
    edit(root / "analytics/summaries/onboarding-funnel.md",
         "  - ../../research/findings/onboarding.md", "  - ../../research/findings/nope.md")


def _missing_component(root):
    edit(root / "research/findings/onboarding.md", "  - cta-primary\nrelated_findings", "  - no-such-component\nrelated_findings")


def _missing_component_in_raw(root):
    edit(root / f"research/raw/{RAW_SESSION}/session-notes.md", "  - cta-primary", "  - no-such-component")


def _deliverable_dangling_finding(root):
    edit(root / "personas/new-user.md", "../research/findings/onboarding.md", "../research/findings/nope.md")


def _deliverable_dangling_cross_link(root):
    edit(root / "journey-maps/new-user-journey.md", "persona_ref: ../personas/new-user.md", "persona_ref: ../personas/ghost.md")


@pytest.mark.parametrize("mutate, message", [
    (_unknown_tag, "not-a-tag"),
    (_unknown_tag_in_deliverable, "not-a-tag"),
    (_dangling_raw_related_findings, "related_findings points at missing findings/nope.md"),
    (_unbacked_finding, "findings/orphan.md: no raw session lists this in related_findings"),
    (_missing_related_analytics, "related_analytics points at missing analytics/summaries/gone.md"),
    (_analytics_dangling_finding, "related_findings points at missing findings/nope.md"),
    (_missing_component, "missing design-tokens/components/no-such-component.md"),
    (_missing_component_in_raw, "missing design-tokens/components/no-such-component.md"),
    (_deliverable_dangling_finding, "related_findings points at missing findings/nope.md"),
    (_deliverable_dangling_cross_link, "persona_ref references missing '../personas/ghost.md'"),
])
@pytest.mark.parametrize("check", [False, True], ids=["write", "check"])
def test_validation_problem_exits_1(run_script, fake_repo, mutate, message, check):
    build(run_script)  # start from fresh indexes so --check fails only on the validator
    mutate(fake_repo)
    result = build(run_script, *(["--check"] if check else []))
    assert result.returncode == 1
    assert message in result.stderr
    assert "Traceback" not in result.stderr


def test_validation_problems_still_write_indexes(run_script, fake_repo):
    _unbacked_finding(fake_repo)
    result = build(run_script)
    assert result.returncode == 1
    assert "[Orphan](findings/orphan.md)" in (fake_repo / "research/_index.md").read_text(encoding="utf-8")


def test_empty_cross_link_fields_are_ignored(run_script, fake_repo):
    edit(fake_repo / "journey-maps/new-user-journey.md", "persona_ref: ../personas/new-user.md", 'persona_ref: ""')
    assert build(run_script).returncode == 0


# --- optional folders --------------------------------------------------------------------------

def test_missing_components_folder_skips_component_validation(run_script, fake_repo):
    shutil.rmtree(fake_repo / "design-tokens")
    result = build(run_script)
    assert result.returncode == 0, result.stderr


def test_missing_analytics_folder_is_skipped(run_script, fake_repo):
    shutil.rmtree(fake_repo / "analytics")
    edit(fake_repo / "research/findings/onboarding.md", "related_analytics:\n  - onboarding-funnel.md", "related_analytics: []")
    result = build(run_script)
    assert result.returncode == 0, result.stderr
    assert "skipping analytics/_index.md" in result.stdout
    assert not (fake_repo / "analytics").exists()


def test_no_tags_file_flags_every_tag(run_script, fake_repo):
    (fake_repo / "research/findings/tags.md").unlink()
    result = build(run_script)
    assert result.returncode == 1
    assert "onboarding" in result.stderr


# --- dates -------------------------------------------------------------------------------------

def test_mixed_date_types_in_backing_raw_sessions(run_script, fake_repo):
    """normalize_date: gray-matter (CRUD UI PUT) can write an ISO timestamp string where PyYAML
    would otherwise load a date — sorting a finding's backing sessions must not crash."""
    add_raw_session(fake_repo, "2026-02-01-string-date", 'date: "2026-02-01T09:30:00.000Z"', "onboarding.md")
    add_raw_session(fake_repo, "2026-02-02-no-date", "", "onboarding.md")
    result = build(run_script)
    assert "Traceback" not in result.stderr
    assert result.returncode == 0, result.stderr
    text = (fake_repo / "research/_index.md").read_text(encoding="utf-8")
    assert re.search(
        rf"raw/2026-02-02-no-date/, raw/{RAW_SESSION}/, raw/2026-02-01-string-date/", text)


def _finding_with_string_date(root):
    write_file(root, "research/findings/checkout.md",
               '---\ntitle: Checkout\ndate: "2026-02-01T09:30:00.000Z"\ntags: []\n---\n')
    add_raw_session(root, "2026-02-01-checkout", "date: 2026-02-01", "checkout.md")


def _finding_without_date(root):
    write_file(root, "research/findings/checkout.md", "---\ntitle: Checkout\ntags: []\n---\n")
    add_raw_session(root, "2026-02-01-checkout", "date: 2026-02-01", "checkout.md")


def _finding_with_empty_date(root):
    write_file(root, "research/findings/checkout.md", "---\ntitle: Checkout\ndate:\ntags: []\n---\n")
    add_raw_session(root, "2026-02-01-checkout", "date: 2026-02-01", "checkout.md")


def _finding_with_unquoted_timestamp(root):
    write_file(root, "research/findings/checkout.md",
               "---\ntitle: Checkout\ndate: 2026-02-01T09:30:00Z\ntags: []\n---\n")
    add_raw_session(root, "2026-02-01-checkout", "date: 2026-02-01", "checkout.md")


def _analytics_with_string_date(root):
    write_file(root, "analytics/summaries/retention.md",
               '---\ntitle: Retention\ndate: "2026-02-01T09:30:00.000Z"\ntags: []\nrelated_findings: []\n---\n')


def _deliverable_with_string_date(root):
    write_file(root, "personas/returning-user.md",
               '---\ntitle: Returning User\ndate: "2026-02-01T09:30:00.000Z"\nstatus: draft\n'
               'tags: []\nrelated_findings: []\nsource_type: native\n---\n')


@pytest.mark.parametrize("mutate", [
    _finding_with_string_date,
    _finding_without_date,
    _finding_with_empty_date,
    _finding_with_unquoted_timestamp,
    _analytics_with_string_date,
    _deliverable_with_string_date,
])
def test_mixed_date_types_across_rows(run_script, fake_repo, mutate):
    mutate(fake_repo)
    result = build(run_script)
    assert "Traceback" not in result.stderr, result.stderr
    assert result.returncode == 0, result.stderr


# --- direct ------------------------------------------------------------------------------------

def test_load_tag_glossary(patch_roots):
    import build_index

    assert build_index.load_tag_glossary() == {"onboarding", "usability", "mobile"}


def test_deliverable_folders_match_new_research_session_schemas():
    import build_index
    import new_research_session

    assert sorted(build_index.DELIVERABLE_FOLDERS) == sorted(new_research_session.DELIVERABLE_SCHEMAS)
