"""
RR-157 decision records (decisions/*.md): build_index.py validates them and writes
decisions/_index.md; build_search_ui.py / export_records.py emit them as kind "decision" with a
`decision` key and a generated block at the top of their html, which is what the CRUD UI's Ask
the Repo retrieves and its provenance links read.
"""
import json
import re
import sys

import pytest
from conftest import RAW_SESSION, REAL_REPO_ROOT, write_file

RAW_NOTES = f"research/raw/{RAW_SESSION}/session-notes.md"
DECISION = "decisions/example-decision.md"
DECISION_ID = "decision:example-decision"

# The synthetic corpus's raw session-notes.md has 18 lines (its Key Findings bullet is line 18);
# findings/onboarding.md has 19 (its one body line is line 19).
VALID = f"""\
    ---
    title: Example decision
    date: 2026-10-23
    status: draft
    decision_status: proposed
    decision_status_source:
      - {RAW_NOTES}:18
    date_decided: not recorded
    decided_by: not recorded
    superseded_by: ""
    evidence:
      - source: {RAW_NOTES}
        lines: "17-18"
      - source: research/findings/onboarding.md
        lines: "19"
    tags: [onboarding]
    related_findings: [onboarding.md]
    related_components: [cta-primary]
    ---

    # Example decision

    ## Decision
    Make the primary CTA easier to find (`{RAW_NOTES}:18`).

    ## Alternatives considered
    not recorded

    ## Rationale
    **Evidence basis:** Observed. Participants missed it (same file, `:18`).

    ## Conditions to revisit
    not recorded

    ## Not recorded
    - Who decided: not recorded.
    """


def add_decision(root, text=VALID):
    write_file(root, DECISION, text)
    return root / DECISION


def replace(path, old, new):
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{old!r} not in {path}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def export(run_script, *args):
    result = run_script("export_records.py", *args)
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


# --- build_index.py ---------------------------------------------------------------------------

def test_valid_decision_writes_index_and_passes_check(run_script, fake_repo):
    add_decision(fake_repo)
    result = run_script("build_index.py")
    assert result.returncode == 0, result.stderr
    index = (fake_repo / "decisions/_index.md").read_text(encoding="utf-8")
    assert "| [Example decision](example-decision.md) | proposed | not recorded | not recorded |" in index
    assert "docs/decisions.md" in index
    assert run_script("build_index.py", "--check").returncode == 0


def test_no_decisions_folder_writes_no_index(run_script, fake_repo):
    assert run_script("build_index.py").returncode == 0
    assert not (fake_repo / "decisions").exists()


def test_check_fails_on_stale_decisions_index(run_script, fake_repo):
    path = add_decision(fake_repo)
    assert run_script("build_index.py").returncode == 0
    replace(path, "decision_status: proposed", "decision_status: accepted")
    result = run_script("build_index.py", "--check")
    assert result.returncode == 1
    assert "decisions/_index.md is out of date" in result.stderr


def test_a_decision_date_is_accepted(run_script, fake_repo):
    path = add_decision(fake_repo)
    replace(path, "date_decided: not recorded", "date_decided: 2026-01-05")
    result = run_script("build_index.py")
    assert result.returncode == 0, result.stderr
    assert "| 2026-01-05 |" in (fake_repo / "decisions/_index.md").read_text(encoding="utf-8")


@pytest.mark.parametrize("old, new, message", [
    ("decided_by: not recorded\n", "", "missing required field 'decided_by'"),
    ("status: draft", "status: shipped", "status 'shipped' isn't one of draft, in-review"),
    ("decision_status: proposed", "decision_status: decided", "decision_status 'decided' isn't one of"),
    ("decided_by: not recorded", "decided_by: Not recorded", "write exactly 'not recorded'"),
    ("decided_by: not recorded", "decided_by: unknown", "write exactly 'not recorded'"),
    ("date_decided: not recorded", "date_decided: TBD", "write exactly 'not recorded'"),
    ("date_decided: not recorded", "date_decided: early 2026", "isn't YYYY-MM-DD or 'not recorded'"),
    ("decision_status: proposed", "decision_status: superseded", "superseded_by is empty"),
    ('superseded_by: ""', "superseded_by: other.md", "superseded_by is set but decision_status isn't superseded"),
    (f"  - {RAW_NOTES}:18\n", f"  - {RAW_NOTES}:99\n", "cites past the end of the file"),
    (f"  - {RAW_NOTES}:18\n", "  - docs/notes.md:1\n", "decision_status_source: 'docs/notes.md' isn't a"),
    ('lines: "17-18"', 'lines: "17-40"', "evidence[0]: research/raw/"),
    ('lines: "17-18"', 'lines: "nineteen"', "isn't like '31', '28-29' or '31,42'"),
    (f"source: {RAW_NOTES}", "source: research/raw/2099-01-01-missing/session-notes.md", "doesn't exist"),
    (f"source: {RAW_NOTES}", "source: personas/new-user.md", "isn't a raw / finding record file"),
    (f'source: {RAW_NOTES}\n    lines: "17-18"\n',
     'source: research/findings/onboarding.md\n    lines: "18"\n',
     "evidence must cite at least one raw session directly"),
    ('lines: "17-18"', 'lines: "17-18"\n    n: 5', "must have exactly the keys source and lines"),
    ("(same file, `:18`)", "(same file, `:25`)", "body citation"),
    (f"(`{RAW_NOTES}:18`)", "(`:19`)", "has no earlier full `path:lines` citation"),
    ("## Conditions to revisit\nnot recorded\n", "", "missing the '## Conditions to revisit' section"),
    ("## Alternatives considered\nnot recorded\n", "## Alternatives considered\n", "'## Alternatives considered' is empty"),
    ("**Evidence basis:** Observed.", "Participants said so.", "must start with '**Evidence basis:**"),
    ("**Evidence basis:** Observed.", "**Evidence basis:** Anecdotal.", "must start with '**Evidence basis:**"),
    ("tags: [onboarding]", "tags: [onboarding, not-a-tag]", "not-a-tag"),
    ("related_findings: [onboarding.md]", "related_findings: [missing.md]", "related_findings points at missing findings/missing.md"),
    ("related_components: [cta-primary]", "related_components: [nope]", "missing design-tokens/components/nope.md"),
])
@pytest.mark.parametrize("check", [False, True], ids=["write", "check"])
def test_invalid_decision_exits_1(run_script, fake_repo, old, new, message, check):
    path = add_decision(fake_repo)
    replace(path, old, new)
    result = run_script("build_index.py", *(["--check"] if check else []))
    assert result.returncode == 1
    assert message in result.stderr


def test_superseded_by_must_resolve(run_script, fake_repo):
    path = add_decision(fake_repo)
    replace(path, "decision_status: proposed", "decision_status: superseded")
    replace(path, 'superseded_by: ""', "superseded_by: decisions/newer.md")
    result = run_script("build_index.py")
    assert result.returncode == 1
    assert "superseded_by references missing decisions/newer.md" in result.stderr
    write_file(fake_repo, "decisions/newer.md", VALID.replace("Example decision", "Newer"))
    result = run_script("build_index.py")
    assert result.returncode == 0, result.stderr


def test_project_tag_rules_apply_to_decisions(run_script, fake_repo):
    write_file(fake_repo, "research/findings/tags.md", """\
        # Tag Glossary

        - **`onboarding`** — first-run experience
        - **`usability`** — usability testing
        - **`mobile`** — mobile surfaces
        - **`project-cross-cutting`** — cross-cutting
        """)
    write_file(fake_repo, "research/projects.yml", f"""\
        projects:
          - id: project-cross-cutting
            label: Cross-cutting
        raw:
          {RAW_SESSION}: project-cross-cutting
        components:
          cta-primary: project-cross-cutting
        """)
    add_decision(fake_repo)
    result = run_script("build_index.py")
    assert result.returncode == 1
    # The other synthetic records lack a project tag too; this checks decisions are included.
    assert re.search(r"decisions/example-decision\.md: needs exactly one project-\* tag", result.stderr)


# --- export_records.py / build_search_ui.py ----------------------------------------------------

def test_decision_is_exported_with_decision_key_and_generated_block(run_script, fake_repo):
    add_decision(fake_repo)
    (record,) = export(run_script, "--kind", "decision")
    assert record["id"] == DECISION_ID
    assert record["kind"] == "decision"
    assert record["type"] == "decision"
    assert record["status"] == "draft"
    assert record["path"] == "../decisions/example-decision.md"
    assert (fake_repo / "research" / record["path"]).resolve().is_file()
    decision = record["decision"]
    assert decision["decision_status"] == "proposed"
    assert decision["date_decided"] == "not recorded"
    assert decision["decided_by"] == "not recorded"
    raw, finding = decision["evidence"]
    assert raw == dict(kind="raw", source=RAW_NOTES, lines="17-18", record=f"raw:{RAW_SESSION}",
                       title="Onboarding usability test", method="usability-test", n="5", date="2026-01-19")
    assert finding["record"] == "finding:onboarding" and finding["n"] is None
    html = record["html"]
    assert html.index("<h1>") < html.index("<h2>Decision record</h2>") < html.index("<h2>Decision</h2>")
    assert "<strong>Decided by:</strong> not recorded.</li>" in html
    assert "(usability-test, n=5, 2026-01-19)" in html
    assert "not recorded" in record["searchText"]


def test_generated_block_names_raw_sessions_the_way_crud_ui_provenance_reads_them(run_script, fake_repo):
    # Mirrors RAW_PATH_RE in the CRUD UI's backend/ask/provenance.js, which reads html only.
    add_decision(fake_repo)
    (record,) = export(run_script, "--kind", "decision")
    linked = set(re.findall(r"\braw/(\d{4}-\d{2}-\d{2}-[a-z0-9-]+)", record["html"]))
    assert linked == {RAW_SESSION}


def test_not_decided_status_reads_as_words(run_script, fake_repo):
    path = add_decision(fake_repo)
    replace(path, "decision_status: proposed", "decision_status: not-decided")
    (record,) = export(run_script, "--kind", "decision")
    assert "<strong>Decision status:</strong> not decided.</li>" in record["html"]
    assert record["decision"]["decision_status"] == "not-decided"


def test_other_kinds_have_null_decision(run_script, fake_repo):
    add_decision(fake_repo)
    records = export(run_script)
    assert {r["id"] for r in records if r["decision"] is not None} == {DECISION_ID}


def test_id_returns_file_body_without_generated_block(run_script, fake_repo):
    add_decision(fake_repo)
    record = export(run_script, "--id", DECISION_ID)
    assert record["rawContent"].startswith("# Example decision")
    assert "Decision record" not in record["rawContent"]


def test_decision_with_broken_evidence_is_skipped_not_fatal(run_script, fake_repo):
    path = add_decision(fake_repo)
    replace(path, 'lines: "17-18"', 'lines: "17-40"')
    records = export(run_script)
    assert DECISION_ID not in {r["id"] for r in records}
    result = run_script("export_records.py", "--id", DECISION_ID)
    assert result.returncode == 1
    assert "is invalid" in result.stderr


def test_search_html_includes_decisions(run_script, fake_repo):
    add_decision(fake_repo)
    result = run_script("build_search_ui.py")
    assert result.returncode == 0, result.stderr
    assert "1 decisions)" in result.stdout
    html = (fake_repo / "research/search.html").read_text(encoding="utf-8")
    assert '"id": "decision:example-decision"' in html
    assert "decision: 'Decisions'" in html


# --- the real seeds (read-only) ----------------------------------------------------------------

SEEDS = {
    "prior-auth-inline-source-citations": ("shipped", "Observed"),
    "sso-reauthentication-15-minutes-vs-4-hours": ("not-decided", "Mixed"),
    "session-lock-paused-draft-preserved-state": ("proposed", "Observed"),
    "override-reason-capture-on-alert-ranking": ("proposed", "Observed"),
    "scope-exclusions-behavioral-health-and-complex-prior-auth": ("accepted", "Observed"),
    "patient-chatbot-scheduling-only-scope": ("proposed", "Observed"),
    "ambient-scribe-ga-release": ("shipped", "Observed"),
    "compass-ai-setup-calendar-step-required": ("shipped", "Mixed"),
}


@pytest.fixture
def real_build_index():
    """The real build_index module, pointed at the real repo (other tests monkeypatch roots)."""
    import importlib
    sys.path.insert(0, str(REAL_REPO_ROOT / "research" / "scripts"))
    import build_index
    return importlib.reload(build_index)


def test_real_seeds_are_the_eight_and_valid(real_build_index):
    b = real_build_index
    decisions = b.load_decisions()
    assert set(decisions) == set(SEEDS)
    assert b.validate_decisions(decisions, b.load_findings(), b.load_components()) == []


@pytest.mark.parametrize("stem", sorted(SEEDS))
def test_real_seed_fields(real_build_index, stem):
    b = real_build_index
    data = b.load_decisions()[stem]
    meta, content = data["meta"], data["content"]
    decision_status, basis = SEEDS[stem]
    assert meta["status"] == "draft"
    assert meta["decision_status"] == decision_status
    # No seed has a recorded decider or decision date (RR-153 Part H); nothing may invent one.
    assert meta["date_decided"] == b.NOT_RECORDED
    assert meta["decided_by"] == b.NOT_RECORDED
    assert b.EVIDENCE_BASIS_RE.match(b.body_sections(content)["Rationale"]).group("label") == basis
    # Wording rules from the RR-157 seed review: no alternative is called "rejected" (no record
    # says so), and the session-lock draft-loss figure is the corrected "all 4 clinicians".
    assert "rejected" not in content.lower()
    if stem == "session-lock-paused-draft-preserved-state":
        assert "4 of 5" not in content
        assert "all 4 clinicians" in content
