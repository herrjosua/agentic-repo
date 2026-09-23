"""
new_research_session.py — the CRUD UI backend shells out to this to create raw sessions and
feature-002 deliverables. Slug validation lives only in the Node backend (SAFE_SLUG_RE in
records.js); the script itself has none — see the Bug 1 xfails below.
"""
import datetime

import frontmatter
import pytest

import new_research_session as nrs

TODAY_ARGS = ["--date", "2026-03-01"]


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def new_raw(run_script, *args, slug="login-interview", title="Login interview", **kw):
    return run_script("new_research_session.py", "--title", title, "--type", "interview",
                      "--topic-slug", slug, *TODAY_ARGS, *args, **kw)


def new_deliverable(run_script, folder, *args, slug="thing", title="A Thing", prompt=False, **kw):
    return run_script("new_research_session.py", "--type", folder, "--title", title,
                      "--slug", slug, *TODAY_ARGS, *([] if prompt else ["--no-prompt"]), *args, **kw)


def load(path):
    return frontmatter.load(path)


# --- raw session mode --------------------------------------------------------------------------

def test_raw_session_creates_both_files(run_script, fake_repo):
    result = new_raw(run_script, "--tags", "onboarding,usability",
                     "--related-findings", "onboarding.md", "--related-components", "cta-primary",
                     "--researcher", "J. Alvarez")
    assert result.returncode == 0, result.stderr
    folder = fake_repo / "research/raw/2026-03-01-login-interview"
    assert sorted(p.name for p in folder.iterdir()) == ["participants.md", "session-notes.md"]

    notes = load(folder / "session-notes.md")
    assert notes.metadata == {
        "title": "Login interview",
        "date": datetime.date(2026, 3, 1),
        "type": "interview",
        "status": "raw",
        "researcher": "J. Alvarez",
        "tags": ["onboarding", "usability"],
        "related_components": ["cta-primary"],
        "related_findings": ["../../findings/onboarding.md"],
    }
    assert "- **Researcher:** J. Alvarez" in notes.content
    assert "[onboarding.md](../../findings/onboarding.md)" in notes.content

    participants = load(folder / "participants.md")
    assert participants.metadata["title"] == "Participants — Login interview"
    assert participants.metadata["researcher"] == "J. Alvarez"
    assert "**Researcher:** J. Alvarez" in participants.content


def test_raw_session_is_indexable_and_exportable(run_script, fake_repo):
    """A freshly scaffolded session must not break the scripts the backend runs next."""
    assert new_raw(run_script, "--tags", "onboarding", "--related-findings", "onboarding.md").returncode == 0
    assert run_script("export_records.py", "--id", "raw:2026-03-01-login-interview").returncode == 0
    result = run_script("build_index.py")
    assert result.returncode == 0, result.stderr


def test_raw_session_without_researcher(run_script, fake_repo):
    new_raw(run_script)
    notes = load(fake_repo / "research/raw/2026-03-01-login-interview/session-notes.md")
    assert notes.metadata["researcher"] is None
    assert "- **Researcher:** TODO" in notes.content


def test_raw_session_participants_count_and_roles(run_script, fake_repo):
    new_raw(run_script, "--participants-count", "6", "--participants-roles", "Nurse, Physician")
    body = load(fake_repo / "research/raw/2026-03-01-login-interview/participants.md").content
    assert "**Count:** 6" in body
    assert "- Nurse\n- Physician" in body


def test_raw_session_keeps_prefixed_related_findings(run_script, fake_repo):
    new_raw(run_script, "--related-findings", "../../findings/onboarding.md")
    meta = load(fake_repo / "research/raw/2026-03-01-login-interview/session-notes.md").metadata
    assert meta["related_findings"] == ["../../findings/onboarding.md"]


@pytest.mark.parametrize("title", ['Quoted "title"', "  padded  ", "Plain title"])
def test_raw_session_title_round_trips_in_session_notes(run_script, fake_repo, title):
    assert new_raw(run_script, title=title).returncode == 0
    meta = load(fake_repo / "research/raw/2026-03-01-login-interview/session-notes.md").metadata
    assert meta["title"] == title


def test_raw_session_refuses_existing_folder_and_leaves_it_untouched(run_script, fake_repo):
    """research/raw/ is append-only (AGENTS.md)."""
    assert new_raw(run_script).returncode == 0
    folder = fake_repo / "research/raw/2026-03-01-login-interview"
    (folder / "session-notes.md").write_text("real notes in progress", encoding="utf-8")
    before = snapshot(folder)

    result = new_raw(run_script, title="Different title")
    assert result.returncode == 1
    assert "already exists" in result.stderr
    assert snapshot(folder) == before


@pytest.mark.parametrize("missing", ["--title", "--type", "--topic-slug"])
def test_raw_session_missing_required_arg_exits_2(run_script, fake_repo, missing):
    args = {"--title": "T", "--type": "interview", "--topic-slug": "s"}
    del args[missing]
    before = snapshot(fake_repo)
    result = run_script("new_research_session.py", *[x for kv in args.items() for x in kv])
    assert result.returncode == 2
    assert missing in result.stderr
    assert snapshot(fake_repo) == before


def test_raw_session_bad_date_exits_2(run_script, fake_repo):
    result = run_script("new_research_session.py", "--title", "T", "--type", "interview",
                        "--topic-slug", "s", "--date", "03/01/2026")
    assert result.returncode == 2
    assert "YYYY-MM-DD" in result.stderr


def test_invalid_type_exits_2(run_script):
    result = run_script("new_research_session.py", "--title", "T", "--type", "synthesis", "--topic-slug", "s")
    assert result.returncode == 2


def test_raw_session_warns_but_does_not_block(run_script, fake_repo):
    result = new_raw(run_script, "--tags", "onboarding,brand-new-tag")
    assert result.returncode == 0
    assert "brand-new-tag" in result.stderr
    assert "onboarding," not in result.stderr
    assert "No --related-findings given" in result.stderr


# --- deliverable mode --------------------------------------------------------------------------

def test_persona_deliverable(run_script, fake_repo):
    result = new_deliverable(run_script, "personas", "--tags", "onboarding",
                             "--related-findings", "onboarding.md", "--designer", "Sam Okafor",
                             slug="frontline-nurse", title="Frontline Nurse — Ambient Scribe")
    assert result.returncode == 0, result.stderr
    post = load(fake_repo / "personas/frontline-nurse.md")
    assert post.metadata == {
        "title": "Frontline Nurse — Ambient Scribe",
        "date": datetime.date(2026, 3, 1),
        "status": "draft",
        "designer": "Sam Okafor",
        "tags": ["onboarding"],
        "related_findings": ["../research/findings/onboarding.md"],
        "source_type": "native",
        "segment": None,
        "based_on": [],
    }
    assert "## Description" in post.content


@pytest.mark.parametrize("folder", sorted(set(nrs.DELIVERABLE_SCHEMAS) - {"prototypes"}))
def test_every_deliverable_folder_no_prompt(run_script, fake_repo, folder):
    result = new_deliverable(run_script, folder)
    assert result.returncode == 0, result.stderr
    meta = load(fake_repo / folder / "thing.md").metadata
    for field, _default in nrs.DELIVERABLE_SCHEMAS[folder]:
        assert field in meta, field
    assert ("designer" in meta) == (folder != "heuristic-evaluations")


def test_new_deliverable_is_indexable_and_exportable(run_script, fake_repo):
    assert new_deliverable(run_script, "wireframes", "--tags", "onboarding").returncode == 0
    assert run_script("export_records.py", "--id", "deliverable:wireframes/thing").returncode == 0
    result = run_script("build_index.py")
    assert result.returncode == 0, result.stderr
    assert (fake_repo / "wireframes/_index.md").is_file()


def test_status_and_description(run_script, fake_repo):
    new_deliverable(run_script, "mockups", "--status", "in-review", "--description", "Hi-fi checkout.")
    post = load(fake_repo / "mockups/thing.md")
    assert post.metadata["status"] == "in-review"
    assert post.metadata["fidelity"] == "hi-fi"
    assert "Hi-fi checkout." in post.content


def test_non_native_source_type_gets_stub_body(run_script, fake_repo):
    new_deliverable(run_script, "personas", "--source-type", "figma-link")
    post = load(fake_repo / "personas/thing.md")
    assert post.metadata["source_type"] == "figma-link"
    assert "## Description" not in post.content


# attribution

def test_heuristic_evaluation_evaluator_and_no_designer(run_script, fake_repo):
    result = new_deliverable(run_script, "heuristic-evaluations",
                             "--evaluator", "Jordan Lee", "--designer", "Sam Okafor")
    assert result.returncode == 0
    assert "--designer is ignored" in result.stderr
    meta = load(fake_repo / "heuristic-evaluations/thing.md").metadata
    assert meta["evaluator"] == "Jordan Lee"
    assert "designer" not in meta


def test_evaluator_ignored_outside_heuristic_evaluations(run_script, fake_repo):
    result = new_deliverable(run_script, "personas", "--evaluator", "Jordan Lee")
    assert result.returncode == 0
    assert "--evaluator is ignored" in result.stderr
    assert "evaluator" not in load(fake_repo / "personas/thing.md").metadata


# prototypes

@pytest.mark.parametrize("proto_type, source_type", [("clickthrough", "figma-link"), ("coded", "github-link")])
def test_prototype_proto_type(run_script, fake_repo, proto_type, source_type):
    result = new_deliverable(run_script, "prototypes", "--proto-type", proto_type)
    assert result.returncode == 0, result.stderr
    post = load(fake_repo / "prototypes/thing.md")
    assert post.metadata["type"] == proto_type
    assert post.metadata["source_type"] == source_type
    assert "## Description" not in post.content  # stub-only


def test_prototype_requires_proto_type(run_script, fake_repo):
    result = new_deliverable(run_script, "prototypes")
    assert result.returncode == 1
    assert "--proto-type" in result.stderr
    assert not (fake_repo / "prototypes").exists()


def test_prototype_rejects_native_source_type(run_script, fake_repo):
    result = new_deliverable(run_script, "prototypes", "--proto-type", "coded", "--source-type", "native")
    assert result.returncode == 1
    assert "stub-only" in result.stderr
    assert not (fake_repo / "prototypes/thing.md").exists()


# validation / overwrite

def test_deliverable_requires_slug(run_script, fake_repo):
    result = run_script("new_research_session.py", "--type", "personas", "--title", "T", "--no-prompt")
    assert result.returncode == 1
    assert "--slug is required" in result.stderr


def test_deliverable_requires_title(run_script, fake_repo):
    result = run_script("new_research_session.py", "--type", "personas", "--slug", "s", "--no-prompt")
    assert result.returncode == 1
    assert "--title is required" in result.stderr


def test_deliverable_bad_date_exits_1(run_script, fake_repo):
    result = run_script("new_research_session.py", "--type", "personas", "--title", "T",
                        "--slug", "s", "--no-prompt", "--date", "2026-13-01")
    assert result.returncode == 1
    assert not (fake_repo / "personas/s.md").exists()


def test_deliverable_refuses_overwrite(run_script, fake_repo):
    before = (fake_repo / "personas/new-user.md").read_bytes()
    result = new_deliverable(run_script, "personas", slug="new-user")
    assert result.returncode == 1
    assert "already exists" in result.stderr
    assert (fake_repo / "personas/new-user.md").read_bytes() == before


def test_overwrite_check_runs_before_prompting(run_script, fake_repo):
    """Without --no-prompt and with stdin closed, a clobber must be rejected before any
    input() call (which would raise EOFError)."""
    result = new_deliverable(run_script, "personas", slug="new-user", prompt=True)
    assert result.returncode == 1
    assert "already exists" in result.stderr
    assert "EOFError" not in result.stderr


def test_force_overwrites(run_script, fake_repo):
    result = new_deliverable(run_script, "personas", "--force", slug="new-user", title="Replaced")
    assert result.returncode == 0
    assert load(fake_repo / "personas/new-user.md").metadata["title"] == "Replaced"


# interactive prompting

def test_interactive_prompts_fill_extra_fields(run_script, fake_repo):
    result = new_deliverable(run_script, "personas", prompt=True,
                             input="clinical staff\nonboarding.md, , other.md\n")
    assert result.returncode == 0, result.stderr
    meta = load(fake_repo / "personas/thing.md").metadata
    assert meta["segment"] == "clinical staff"
    assert meta["based_on"] == ["onboarding.md", "other.md"]


def test_interactive_dict_and_int_fields(run_script, fake_repo):
    result = new_deliverable(run_script, "research-plans", prompt=True,
                             input="survey\n2026-03-01\n2026-03-15\n\n")
    assert result.returncode == 0, result.stderr
    meta = load(fake_repo / "research-plans/thing.md").metadata
    assert meta["method"] == "survey"
    assert str(meta["study_dates"]["start"]) == "2026-03-01"
    assert str(meta["study_dates"]["end"]) == "2026-03-15"


def test_interactive_bad_int_falls_back_to_0(run_script, fake_repo):
    result = new_deliverable(run_script, "accessibility-screenings", prompt=True, input="AA\ncheckout\nlots\n")
    assert result.returncode == 0
    assert "must be an integer" in result.stderr
    assert load(fake_repo / "accessibility-screenings/thing.md").metadata["issues_found"] == 0


def test_no_prompt_never_reads_stdin(run_script, fake_repo):
    # run_script closes stdin by default; any input() call would raise EOFError.
    result = new_deliverable(run_script, "research-plans")
    assert result.returncode == 0, result.stderr


# --- --check-tags-only -------------------------------------------------------------------------

@pytest.mark.parametrize("tags, code", [("onboarding,mobile", 0), ("onboarding,nope", 1), ("", 0)])
def test_check_tags_only(run_script, fake_repo, tags, code):
    before = snapshot(fake_repo)
    result = run_script("new_research_session.py", "--check-tags-only", tags)
    assert result.returncode == code
    assert snapshot(fake_repo) == before


# --- direct ------------------------------------------------------------------------------------

def test_fm_block():
    assert nrs.fm_block({"a": "x", "b": [], "c": ["1", "2"], "d": {"s": "", "e": "z"}}) == (
        "---\na: x\nb: []\nc:\n  - 1\n  - 2\nd:\n  s: \n  e: z\n---"
    )


@pytest.mark.parametrize("raw, out", [
    ("plain", "plain"),
    ("a: b", '"a: b"'),
    ("a # b", '"a # b"'),
    ('say "hi"', '"say \\"hi\\""'),
    (" padded", '" padded"'),
])
def test_yaml_str(raw, out):
    assert nrs.yaml_str(raw) == out


def test_check_tags_returns_unknown(capsys):
    assert nrs.check_tags(["a", "b"], {"a"}) == ["b"]
    assert "b" in capsys.readouterr().err


# --- Bug 1: no slug validation in the script (reported in Phase 1, deliberately not fixed) ----
# The Node backend rejects these via SAFE_SLUG_RE before ever calling the script, but the
# script itself happily writes outside its target folder. Payloads stay inside tmp_path.

BUG1 = pytest.mark.xfail(strict=True, reason="Bug 1: new_research_session.py has no slug validation (path traversal)")


@BUG1
def test_deliverable_slug_traversal_is_rejected(run_script, fake_repo, tmp_path):
    result = new_deliverable(run_script, "personas", slug="../../escaped")
    assert not (tmp_path / "escaped.md").exists()
    assert result.returncode != 0


@BUG1
def test_raw_topic_slug_traversal_is_rejected(run_script, fake_repo):
    result = new_raw(run_script, slug="x/../../../escaped-raw")
    assert not (fake_repo / "escaped-raw").exists()
    assert result.returncode != 0


@pytest.mark.parametrize("title", ["Onboarding: flow test", "Onboarding #2"])
def test_participants_title_round_trips(run_script, fake_repo, title):
    assert new_raw(run_script, title=title).returncode == 0
    meta = load(fake_repo / "research/raw/2026-03-01-login-interview/participants.md").metadata
    assert meta["title"] == f"Participants — {title}"


def test_session_with_colon_title_does_not_break_export(run_script, fake_repo):
    assert new_raw(run_script, title="Onboarding: flow test").returncode == 0
    result = run_script("export_records.py", "--summary")
    assert result.returncode == 0, result.stderr
