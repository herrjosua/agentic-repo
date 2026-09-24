"""
new_research_session.py — the CRUD UI backend shells out to this to create raw sessions and
feature-002 deliverables. The script validates --slug and --topic-slug with the same
^[a-z0-9-]+$ rule as the Node backend's SAFE_SLUG_RE (records.js) — see slug validation below.
"""
import datetime

import frontmatter
import pytest
import yaml

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


def test_raw_session_bad_date_exits_1(run_script, fake_repo):
    result = run_script("new_research_session.py", "--title", "T", "--type", "interview",
                        "--topic-slug", "s", "--date", "03/01/2026")
    assert result.returncode == 1
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
        '---\na: x\nb: []\nc:\n  - "1"\n  - "2"\nd:\n  s: \n  e: z\n---'
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


# --- slug validation -------------------------------------------------------------------------
# Same ^[a-z0-9-]+$ rule as the backend's SAFE_SLUG_RE. Payloads stay inside tmp_path.

def test_deliverable_slug_traversal_is_rejected(run_script, fake_repo, tmp_path):
    result = new_deliverable(run_script, "personas", slug="../../escaped")
    assert not (tmp_path / "escaped.md").exists()
    assert result.returncode != 0


def test_raw_topic_slug_traversal_is_rejected(run_script, fake_repo):
    result = new_raw(run_script, slug="x/../../../escaped-raw")
    assert not (fake_repo / "escaped-raw").exists()
    assert result.returncode != 0


def all_paths(root):
    """Files *and* directories, so a stray empty folder (e.g. raw/<date>-x/) counts as created."""
    return {str(p.relative_to(root)) for p in root.rglob("*")}


BAD_SLUGS = pytest.mark.parametrize("slug", [
    "Onboarding",
    "login_interview",
    "ABSOLUTE",  # placeholder: replaced with an absolute path inside tmp_path
    "a/b",
    "..",
    "abc\n",
], ids=["uppercase", "underscore", "absolute", "slash", "dotdot", "trailing-newline"])


def _resolve(slug, tmp_path):
    return str(tmp_path / "abs-escape") if slug == "ABSOLUTE" else slug


@BAD_SLUGS
def test_deliverable_bad_slug_is_rejected(run_script, fake_repo, tmp_path, slug):
    before = all_paths(tmp_path)
    result = new_deliverable(run_script, "personas", slug=_resolve(slug, tmp_path))
    assert result.returncode == 1
    assert "--slug" in result.stderr
    assert all_paths(tmp_path) == before


@BAD_SLUGS
def test_raw_bad_topic_slug_is_rejected(run_script, fake_repo, tmp_path, slug):
    before = all_paths(tmp_path)
    result = new_raw(run_script, slug=_resolve(slug, tmp_path))
    assert result.returncode == 1
    assert "--topic-slug" in result.stderr
    assert all_paths(tmp_path) == before


@pytest.mark.parametrize("title", ["Onboarding: flow test", "Onboarding #2"])
def test_participants_title_round_trips(run_script, fake_repo, title):
    assert new_raw(run_script, title=title).returncode == 0
    meta = load(fake_repo / "research/raw/2026-03-01-login-interview/participants.md").metadata
    assert meta["title"] == f"Participants — {title}"


def test_session_with_colon_title_does_not_break_export(run_script, fake_repo):
    assert new_raw(run_script, title="Onboarding: flow test").returncode == 0
    result = run_script("export_records.py", "--summary")
    assert result.returncode == 0, result.stderr


# --- frontmatter escaping (v0.5.21) --------------------------------------------------------------
# Any user value that loaded as a non-string, a dict, or not at all used to make
# export_records.py (and so GET /records) fail for every user. Each run below puts one problem
# input into every user-supplied field at once and asserts each field loads back exactly.

INJECTION = "ok\nresearcher: Someone Else"

PROBLEM_INPUTS = [
    "[draft", "@home", "- dash", "* star", 'C:\\path "x"',
    "2024", "Yes", "null", "~", "on", "2024-01-01",
    "phase: 1", "a #b", "'quoted'", "end:", INJECTION,
]
PROMPTABLE_INPUTS = [s for s in PROBLEM_INPUTS if "\n" not in s]  # input() reads one line


def assert_exports(run_script):
    result = run_script("export_records.py", "--summary")
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize("value", PROBLEM_INPUTS)
def test_raw_fields_round_trip(run_script, fake_repo, value):
    result = new_raw(run_script, "--tags", value, "--related-components", value,
                     "--related-findings", value, "--researcher", value, title=value)
    assert result.returncode == 0, result.stderr
    folder = fake_repo / "research/raw/2026-03-01-login-interview"
    notes = load(folder / "session-notes.md").metadata
    assert notes["title"] == value
    assert notes["researcher"] == value
    assert notes["tags"] == [value]
    assert notes["related_components"] == [value]
    assert notes["related_findings"] == [f"../../findings/{value}"]
    participants = load(folder / "participants.md").metadata
    assert participants["title"] == f"Participants — {value}"
    assert participants["researcher"] == value
    assert participants["tags"] == [value]
    assert participants["related_findings"] == [f"../../findings/{value}"]
    assert_exports(run_script)


@pytest.mark.parametrize("value", PROBLEM_INPUTS)
def test_deliverable_fields_round_trip(run_script, fake_repo, value):
    result = new_deliverable(run_script, "wireframes", "--tags", value, "--related-findings", value,
                             "--source-type", value, "--designer", value, title=value)
    assert result.returncode == 0, result.stderr
    meta = load(fake_repo / "wireframes/thing.md").metadata
    assert meta["title"] == value
    assert meta["designer"] == value
    assert meta["tags"] == [value]
    assert meta["related_findings"] == [f"../research/findings/{value}"]
    assert meta["source_type"] == value
    assert_exports(run_script)


@pytest.mark.parametrize("value", PROBLEM_INPUTS)
def test_heuristic_evaluator_round_trips(run_script, fake_repo, value):
    result = new_deliverable(run_script, "heuristic-evaluations", "--evaluator", value, title=value)
    assert result.returncode == 0, result.stderr
    meta = load(fake_repo / "heuristic-evaluations/thing.md").metadata
    assert meta["title"] == value
    assert meta["evaluator"] == value
    assert_exports(run_script)


@pytest.mark.parametrize("value", PROMPTABLE_INPUTS)
def test_prompted_fields_round_trip(run_script, fake_repo, value):
    # research-plans: method, study_dates.start, study_dates.end, related_guide (str + dict subfields)
    result = new_deliverable(run_script, "research-plans", prompt=True, input=f"{value}\n" * 4)
    assert result.returncode == 0, result.stderr
    # personas: segment, based_on (str + list)
    result = new_deliverable(run_script, "personas", prompt=True, input=f"{value}\n" * 2)
    assert result.returncode == 0, result.stderr
    plan = load(fake_repo / "research-plans/thing.md").metadata
    assert plan["method"] == value
    assert plan["study_dates"] == {"start": value, "end": value}
    assert plan["related_guide"] == value
    persona = load(fake_repo / "personas/thing.md").metadata
    assert persona["segment"] == value
    assert persona["based_on"] == [value]
    assert_exports(run_script)


@pytest.mark.parametrize("value", PROBLEM_INPUTS + ["a\x85b", "a\u2028b", "del\x7f", "x\r\ny", " padded "])
def test_fm_block_round_trips(value):
    block = nrs.fm_block({"v": value, "l": [value], "d": {"s": value}})
    assert yaml.safe_load(block.strip("-\n")) == {"v": value, "l": [value], "d": {"s": value}}


@pytest.mark.parametrize("value", [
    "onboarding", "../../findings/onboarding.md", "Participants — Login interview",
    "https://figma.com/proto/example", "6-step onboarding wizard", "42-cfr-part-2",
])
def test_plain_values_stay_unquoted(value):
    assert nrs.yaml_str(value) == value


def test_raw_newline_cannot_inject_keys(run_script, fake_repo):
    result = new_raw(run_script, "--tags", INJECTION, "--related-components", INJECTION,
                     "--related-findings", INJECTION, "--researcher", "Original")
    assert result.returncode == 0, result.stderr
    for name in ("session-notes.md", "participants.md"):
        meta = load(fake_repo / "research/raw/2026-03-01-login-interview" / name).metadata
        assert set(meta) == {"title", "date", "type", "status", "researcher", "tags",
                             "related_components", "related_findings"}
        assert meta["researcher"] == "Original"


def test_deliverable_newline_cannot_inject_keys(run_script, fake_repo):
    injection = "ok\ndesigner: Someone Else"
    result = new_deliverable(run_script, "wireframes", "--tags", injection, "--related-findings", injection,
                             "--source-type", injection, "--designer", "Original")
    assert result.returncode == 0, result.stderr
    meta = load(fake_repo / "wireframes/thing.md").metadata
    assert set(meta) == {"title", "date", "status", "designer", "tags", "related_findings",
                         "source_type", "fidelity", "flow_ref"}
    assert meta["designer"] == "Original"


def test_raw_empty_list_items_are_dropped(run_script, fake_repo):
    result = new_raw(run_script, "--tags", "onboarding, ,usability,", "--related-components", "a, ,b,")
    assert result.returncode == 0, result.stderr
    meta = load(fake_repo / "research/raw/2026-03-01-login-interview/session-notes.md").metadata
    assert meta["tags"] == ["onboarding", "usability"]
    assert meta["related_components"] == ["a", "b"]
    assert_exports(run_script)


def test_deliverable_empty_list_items_are_dropped(run_script, fake_repo):
    result = new_deliverable(run_script, "wireframes", "--tags", "onboarding, ,usability,")
    assert result.returncode == 0, result.stderr
    assert load(fake_repo / "wireframes/thing.md").metadata["tags"] == ["onboarding", "usability"]
    assert_exports(run_script)


BAD_DATES = pytest.mark.parametrize("bad_date", [
    "20240101", "2024-W01-1", "2024-02-30", "2024-1-5", "２０２４-01-01", "2024-01-01\n", "2024-01-01T00:00",
])


@BAD_DATES
def test_raw_rejects_bad_date(run_script, fake_repo, bad_date):
    before = snapshot(fake_repo)
    result = run_script("new_research_session.py", "--title", "T", "--type", "interview",
                        "--topic-slug", "s", "--date", bad_date)
    assert result.returncode == 1
    assert "YYYY-MM-DD" in result.stderr
    assert snapshot(fake_repo) == before


@BAD_DATES
def test_deliverable_rejects_bad_date(run_script, fake_repo, bad_date):
    result = run_script("new_research_session.py", "--type", "personas", "--title", "T",
                        "--slug", "s", "--no-prompt", "--date", bad_date)
    assert result.returncode == 1
    assert "YYYY-MM-DD" in result.stderr
    assert not (fake_repo / "personas/s.md").exists()


def test_lone_surrogate_is_rejected(run_script, fake_repo):
    before = snapshot(fake_repo)
    result = new_raw(run_script, title="bad \udc80 byte")
    assert result.returncode == 1
    assert "--title" in result.stderr
    assert snapshot(fake_repo) == before
