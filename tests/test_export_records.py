"""
export_records.py — the CRUD UI backend shells out to this (child_process.execFile) for
GET /api/records and GET /api/records/:id, so its JSON shape is the contract under test.
"""
import json
import shutil
from datetime import UTC

import pytest
from conftest import RAW_SESSION

EXPECTED_KEYS = {
    "id", "kind", "title", "date", "type", "status", "tags", "related_components", "severity",
    "last_edited_by", "last_edited_at",
    "researcher", "designer", "evaluator", "reviewed_by",
    "path", "html", "searchText",
}

EXPECTED_IDS = {
    f"raw:{RAW_SESSION}",
    "finding:onboarding",
    "component:cta-primary",
    "analytics:onboarding-funnel",
    "deliverable:personas/new-user",
    "deliverable:journey-maps/new-user-journey",
}

# One source file per record kind, and the id export_records assigns it.
FILE_BY_KIND = {
    "raw": (f"research/raw/{RAW_SESSION}/session-notes.md", f"raw:{RAW_SESSION}"),
    "finding": ("research/findings/onboarding.md", "finding:onboarding"),
    "component": ("design-tokens/components/cta-primary.md", "component:cta-primary"),
    "analytics": ("analytics/summaries/onboarding-funnel.md", "analytics:onboarding-funnel"),
    "deliverable": ("personas/new-user.md", "deliverable:personas/new-user"),
}


def export(run_script, *args):
    result = run_script("export_records.py", *args)
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def add_frontmatter(path, *lines):
    """Insert extra frontmatter lines right after the opening ---."""
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    path.write_text("---\n" + "".join(f"{line}\n" for line in lines) + text[4:], encoding="utf-8")


# --- shape ------------------------------------------------------------------------------------

def test_exports_every_record_with_stable_shape(run_script):
    records = export(run_script)
    assert {r["id"] for r in records} == EXPECTED_IDS
    for r in records:
        assert set(r) == EXPECTED_KEYS, r["id"]


def test_record_paths_resolve_relative_to_research_root(run_script, fake_repo):
    for r in export(run_script):
        assert (fake_repo / "research" / r["path"]).resolve().is_file(), r["path"]


def test_dates_are_strings(run_script):
    for r in export(run_script):
        if r["kind"] != "component":
            assert isinstance(r["date"], str), r["id"]


def test_raw_record_includes_participants_html(run_script):
    (raw,) = export(run_script, "--kind", "raw")
    assert "<h2>Participants</h2>" in raw["html"]


def test_deliverable_type_is_folder_name(run_script):
    types = {r["id"]: r["type"] for r in export(run_script, "--kind", "deliverable")}
    assert types == {
        "deliverable:personas/new-user": "personas",
        "deliverable:journey-maps/new-user-journey": "journey-maps",
    }


# --- flags ------------------------------------------------------------------------------------

@pytest.mark.parametrize("kind", sorted(FILE_BY_KIND))
def test_kind_filter(run_script, kind):
    records = export(run_script, "--kind", kind)
    assert records
    assert {r["kind"] for r in records} == {kind}


def test_invalid_kind_is_rejected(run_script):
    result = run_script("export_records.py", "--kind", "bogus")
    assert result.returncode == 2
    assert result.stdout == ""


def test_summary_strips_html_and_search_text(run_script):
    for r in export(run_script, "--summary"):
        assert set(r) == EXPECTED_KEYS - {"html", "searchText"}


def test_id_returns_single_record_with_raw_content(run_script):
    record = export(run_script, "--id", "finding:onboarding")
    assert isinstance(record, dict)
    assert record["id"] == "finding:onboarding"
    assert record["rawContent"] == "# Onboarding\n\nUsers struggle to find the primary CTA."
    assert "---" not in record["rawContent"]  # body only, no frontmatter


def test_id_for_deliverable_resolves_outside_research(run_script):
    record = export(run_script, "--id", "deliverable:personas/new-user")
    assert record["rawContent"].startswith("# New User")


def test_summary_has_no_effect_with_id(run_script):
    record = export(run_script, "--id", "finding:onboarding", "--summary")
    assert "html" in record and "searchText" in record and "rawContent" in record


def test_unknown_id_exits_1(run_script):
    result = run_script("export_records.py", "--id", "finding:does-not-exist")
    assert result.returncode == 1
    assert result.stdout == ""
    assert "does-not-exist" in result.stderr


def test_id_combined_with_wrong_kind_is_not_found(run_script):
    result = run_script("export_records.py", "--kind", "raw", "--id", "finding:onboarding")
    assert result.returncode == 1


def test_optional_folders_missing(run_script, fake_repo):
    shutil.rmtree(fake_repo / "analytics")
    shutil.rmtree(fake_repo / "design-tokens")
    shutil.rmtree(fake_repo / "journey-maps")
    kinds = {r["kind"] for r in export(run_script)}
    assert kinds == {"raw", "finding", "deliverable"}


def test_empty_corpus_exports_empty_array(run_script, fake_repo):
    for d in ("research/raw", "research/findings", "analytics", "design-tokens", "personas", "journey-maps"):
        shutil.rmtree(fake_repo / d)
    assert export(run_script) == []


# --- regression v0.5.8: last_edited_by / last_edited_at ---------------------------------------

def test_edit_fields_default_to_null_for_every_kind(run_script):
    records = export(run_script)
    assert {r["kind"] for r in records} == set(FILE_BY_KIND)
    for r in records:
        assert r["last_edited_by"] is None, r["id"]
        assert r["last_edited_at"] is None, r["id"]


@pytest.mark.parametrize("kind", sorted(FILE_BY_KIND))
def test_edit_fields_quoted_string_passthrough(run_script, fake_repo, kind):
    rel, record_id = FILE_BY_KIND[kind]
    add_frontmatter(fake_repo / rel,
                    "last_edited_by: Dana Reyes",
                    'last_edited_at: "2026-09-18T10:16:26.123Z"')
    record = export(run_script, "--id", record_id)
    assert record["last_edited_by"] == "Dana Reyes"
    assert record["last_edited_at"] == "2026-09-18T10:16:26.123Z"


@pytest.mark.parametrize("kind", sorted(FILE_BY_KIND))
def test_edit_fields_unquoted_timestamp_normalized_and_export_survives(run_script, fake_repo, kind):
    """A hand-edited, unquoted timestamp parses to a datetime in PyYAML; before v0.5.8 that
    made json.dumps fail the *entire* export, not just this record."""
    rel, record_id = FILE_BY_KIND[kind]
    add_frontmatter(fake_repo / rel, "last_edited_at: 2026-09-18T10:16:26.123Z")

    records = export(run_script)  # whole export must still succeed
    assert {r["id"] for r in records} == EXPECTED_IDS
    record = next(r for r in records if r["id"] == record_id)
    assert record["last_edited_at"] == "2026-09-18T10:16:26.123Z"
    assert record["last_edited_by"] is None


def test_edit_fields_non_string_by_is_stringified(run_script, fake_repo):
    add_frontmatter(fake_repo / "research/findings/onboarding.md", "last_edited_by: 42")
    assert export(run_script, "--id", "finding:onboarding")["last_edited_by"] == "42"


def test_edit_fields_helper_direct():
    from datetime import datetime

    from build_search_ui import _edit_fields

    assert _edit_fields({}) == {"last_edited_by": None, "last_edited_at": None}
    at = datetime(2026, 9, 18, 10, 16, 26, 123000, tzinfo=UTC)
    assert _edit_fields({"last_edited_at": at})["last_edited_at"] == "2026-09-18T10:16:26.123Z"


# --- attribution fields -----------------------------------------------------------------------

def test_attribution_fields_null_when_absent_and_populated_when_present(run_script):
    by_id = {r["id"]: r for r in export(run_script)}
    assert by_id["finding:onboarding"]["researcher"] == "J. Alvarez"
    assert by_id["deliverable:personas/new-user"]["designer"] == "Sam Okafor"
    # Raw sessions created before --researcher existed carry no researcher frontmatter -> null, not missing.
    raw = by_id[f"raw:{RAW_SESSION}"]
    assert raw["researcher"] is None
    for r in by_id.values():
        assert r["evaluator"] is None and r["reviewed_by"] is None


# --- regression v0.5.7: XSS through the backend's html field ----------------------------------

def test_exported_html_is_sanitized(run_script, fake_repo):
    path = fake_repo / "research/findings/onboarding.md"
    path.write_text(
        path.read_text(encoding="utf-8")
        + "\n[click](javascript:alert(1))\n\n"
        + '[hover](http://x.test/" onmouseover="alert(1))\n\n'
        + "<script>alert(1)</script>\n",
        encoding="utf-8",
    )
    html = export(run_script, "--id", "finding:onboarding")["html"]
    assert 'href="javascript:' not in html
    assert '" onmouseover="' not in html
    assert "<script>" not in html
    assert "&lt;script&gt;" in html


# --- one bad record doesn't break the rest (v0.5.22) ---------------------------------------------

BAD_FRONTMATTER = {
    "unparseable": ("title: [unclosed", "unparseable frontmatter"),
    "duplicate-key": ("title: A\ntitle: B", "duplicate key 'title'"),
    "components-int": ("title: C\nrelated_components: 5", "related_components must be a list of strings"),
    "findings-dict": ('title: D\nrelated_findings: [{"a": 1}]', "related_findings must be a list of strings"),
}


def add_bad_finding(root, trigger):
    frontmatter_text, _ = BAD_FRONTMATTER[trigger]
    path = root / "research/findings" / f"bad-{trigger}.md"
    path.write_text(f"---\n{frontmatter_text}\n---\n\nBody.\n", encoding="utf-8")
    return path


@pytest.mark.parametrize("trigger", sorted(BAD_FRONTMATTER))
def test_summary_skips_bad_record_and_keeps_the_rest(run_script, fake_repo, trigger):
    add_bad_finding(fake_repo, trigger)
    result = run_script("export_records.py", "--summary")
    assert result.returncode == 0, result.stderr
    assert {r["id"] for r in json.loads(result.stdout)} == EXPECTED_IDS
    warnings = result.stderr.strip().splitlines()
    assert len(warnings) == 1
    assert f"research/findings/bad-{trigger}.md" in warnings[0]
    assert BAD_FRONTMATTER[trigger][1] in warnings[0]


@pytest.mark.parametrize("trigger", ["unparseable", "components-int"])
def test_id_returns_valid_target_despite_broken_sibling(run_script, fake_repo, trigger):
    add_bad_finding(fake_repo, trigger)
    result = run_script("export_records.py", "--id", "finding:onboarding")
    assert result.returncode == 0, result.stderr
    record = json.loads(result.stdout)
    assert record["id"] == "finding:onboarding"
    assert record["rawContent"]


@pytest.mark.parametrize("trigger", ["duplicate-key", "findings-dict"])
def test_id_of_bad_record_exits_1_with_reason(run_script, fake_repo, trigger):
    add_bad_finding(fake_repo, trigger)
    result = run_script("export_records.py", "--id", f"finding:bad-{trigger}")
    assert result.returncode == 1
    assert result.stdout == ""
    assert f"Record 'finding:bad-{trigger}' is invalid" in result.stderr
    assert BAD_FRONTMATTER[trigger][1] in result.stderr


def test_null_list_fields_are_accepted_as_empty(run_script, fake_repo):
    path = fake_repo / "research/findings/nulls.md"
    path.write_text("---\ntitle: Nulls\ntags:\nrelated_components: null\n---\n\nBody.\n", encoding="utf-8")
    result = run_script("export_records.py", "--id", "finding:nulls")
    assert result.returncode == 0, result.stderr
    record = json.loads(result.stdout)
    assert record["tags"] == [] and record["related_components"] == []
