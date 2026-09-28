"""
Project tagging (docs/projects.md): research/projects.yml assigns raw sessions and components a
project-* tag at load time, falling back to project-cross-cutting with a warning;
new_research_session.py maps each new raw session; build_index.py warns about unmapped entries
and fails on them only under --check, but fails on every other project problem in any mode.
Without projects.yml the feature is off entirely.
"""
import json
import re

import pytest
from conftest import RAW_SESSION, write_file

PROJECTS_YML = f"""\
    projects:
      - id: project-onboarding
        label: Onboarding
      - id: project-cross-cutting
        label: Cross-cutting
    raw:
      {RAW_SESSION}: project-onboarding
    components:
      cta-primary: project-onboarding
    """

TAGGED_FILES = [
    "analytics/summaries/onboarding-funnel.md",
    "personas/new-user.md",
    "journey-maps/new-user-journey.md",
]


def edit(path, old, new):
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{old!r} not in {path}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


@pytest.fixture
def projects_repo(fake_repo):
    """fake_repo with projects.yml, glossary entries, and a project tag on every taggable record,
    so build_index.py passes clean on it."""
    write_file(fake_repo, "research/projects.yml", PROJECTS_YML)
    with open(fake_repo / "research/findings/tags.md", "a", encoding="utf-8") as f:
        f.write("- **`project-onboarding`** — Onboarding\n- **`project-cross-cutting`** — Cross-cutting\n")
    edit(fake_repo / "research/findings/onboarding.md",
         "  - usability\nrelated_components", "  - usability\n  - project-onboarding\nrelated_components")
    for rel in TAGGED_FILES:
        edit(fake_repo / rel, "tags: [onboarding]", "tags: [onboarding, project-onboarding]")
    return fake_repo


def export(run_script):
    result = run_script("export_records.py", "--summary")
    assert result.returncode == 0, result.stderr
    return {r["id"]: r for r in json.loads(result.stdout)}, result.stderr


def project_of(record):
    tags = [t for t in record["tags"] if t.startswith("project-")]
    assert len(tags) == 1, record["tags"]
    return tags[0]


def test_without_projects_yml_nothing_is_added(run_script):
    records, stderr = export(run_script)
    assert stderr == ""
    assert records["component:cta-primary"]["tags"] == []
    assert records[f"raw:{RAW_SESSION}"]["tags"] == ["onboarding", "usability"]


def test_every_record_gets_exactly_one_project_and_check_passes(run_script, projects_repo):
    records, stderr = export(run_script)
    assert stderr == ""
    assert {project_of(r) for r in records.values()} == {"project-onboarding"}
    assert records["component:cta-primary"]["tags"] == ["project-onboarding"]
    assert run_script("build_index.py").returncode == 0
    result = run_script("build_index.py", "--check")
    assert result.returncode == 0, result.stderr


def test_unmapped_raw_session_falls_back_to_cross_cutting(run_script, projects_repo):
    write_file(projects_repo, "research/raw/2026-03-01-new-session/session-notes.md", """\
        ---
        title: New session
        date: 2026-03-01
        type: interview
        status: raw
        tags: [onboarding]
        related_findings:
          - ../../findings/onboarding.md
        ---

        # New session
        """)
    records, stderr = export(run_script)
    assert project_of(records["raw:2026-03-01-new-session"]) == "project-cross-cutting"
    assert "raw '2026-03-01-new-session' has no known project" in stderr
    assert_unmapped_warns_then_check_fails(run_script, "raw entry '2026-03-01-new-session' has no project")


def test_unmapped_component_falls_back_to_cross_cutting(run_script, projects_repo):
    write_file(projects_repo, "design-tokens/components/new-widget.md", "---\ntitle: New Widget\n---\n\n# New Widget\n")
    records, stderr = export(run_script)
    assert records["component:new-widget"]["tags"] == ["project-cross-cutting"]
    assert "components 'new-widget' has no known project" in stderr
    assert_unmapped_warns_then_check_fails(run_script, "components entry 'new-widget' has no project")


def assert_unmapped_warns_then_check_fails(run_script, message):
    # A normal run is what the CRUD UI reruns after every edit: warn, don't fail.
    result = run_script("build_index.py")
    assert result.returncode == 0, result.stderr
    assert message in result.stderr
    # --check (CI) stays strict. The normal run just refreshed the indexes, so this is the only failure.
    result = run_script("build_index.py", "--check")
    assert result.returncode == 1
    assert message in result.stderr
    assert "out of date" not in result.stderr


# --- new_research_session.py maps new raw sessions --------------------------------------------

NEW_SESSION = "2026-03-01-login-interview"


def new_session(run_script):
    return run_script("new_research_session.py", "--title", "Login interview", "--type", "interview",
                      "--topic-slug", "login-interview", "--date", "2026-03-01",
                      "--tags", "onboarding", "--related-findings", "onboarding.md")


def test_new_session_is_mapped_so_build_index_is_clean(run_script, projects_repo):
    path = projects_repo / "research/projects.yml"
    # Comments and a blank line inside raw:, and a section after it, must all survive untouched.
    edit(path, "raw:\n", "# Raw sessions:\nraw:  # folder -> project\n")
    edit(path, "components:\n", "  # (newest last)\n\ncomponents:\n")
    before = path.read_text(encoding="utf-8")

    result = new_session(run_script)
    assert result.returncode == 0, result.stderr
    after = path.read_text(encoding="utf-8")
    entry = f"  {RAW_SESSION}: project-onboarding\n"
    assert after == before.replace(entry, entry + f"  {NEW_SESSION}: project-cross-cutting\n", 1)

    records, stderr = export(run_script)
    assert stderr == ""
    assert project_of(records[f"raw:{NEW_SESSION}"]) == "project-cross-cutting"
    result = run_script("build_index.py")
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    result = run_script("build_index.py", "--check")
    assert result.returncode == 0, result.stderr


def test_new_session_adds_raw_section_when_missing(run_script, projects_repo):
    path = projects_repo / "research/projects.yml"
    edit(path, f"raw:\n  {RAW_SESSION}: project-onboarding\n", "")
    assert new_session(run_script).returncode == 0
    assert path.read_text(encoding="utf-8").endswith(f"\nraw:\n  {NEW_SESSION}: project-cross-cutting\n")


def test_new_session_leaves_unusable_projects_yml_alone(run_script, projects_repo):
    path = projects_repo / "research/projects.yml"
    edit(path, "components:\n", "raw_again: [\ncomponents:\n")
    before = path.read_text(encoding="utf-8")
    result = new_session(run_script)
    assert result.returncode == 0, result.stderr
    assert (projects_repo / f"research/raw/{NEW_SESSION}/session-notes.md").is_file()
    assert "Didn't add 2026-03-01-login-interview to research/projects.yml" in result.stderr
    assert path.read_text(encoding="utf-8") == before


@pytest.mark.parametrize("with_projects", [False, True])
def test_new_session_backend_contract_unchanged(run_script, fake_repo, with_projects):
    """What the CRUD UI backend's POST /sessions relies on (records.js): exit 0, and the first
    '✅ Created <path>' line in stdout names the session folder it then commits. Identical with or
    without projects.yml; projects.yml is the only other file touched, and only when it exists."""
    projects = fake_repo / "research/projects.yml"
    if with_projects:
        write_file(fake_repo, "research/projects.yml", PROJECTS_YML)
    before = {p for p in fake_repo.rglob("*") if p.is_file()}

    result = new_session(run_script)
    assert result.returncode == 0, result.stderr
    folder = fake_repo / f"research/raw/{NEW_SESSION}"
    assert result.stdout == (
        f"✅ Created {folder}/\n"
        "   - session-notes.md\n"
        "   - participants.md\n"
        "Next: fill in the TODOs, then synthesize into research/findings/<topic>.md and run build_index.py.\n"
    )
    assert re.search(r"✅ Created (.+?)(?:\n|$)", result.stdout).group(1).strip() == f"{folder}/"
    created = {p for p in fake_repo.rglob("*") if p.is_file()} - before
    assert created == {folder / "session-notes.md", folder / "participants.md"}
    assert projects.exists() == with_projects


def test_deliverable_does_not_touch_projects_yml(run_script, projects_repo):
    path = projects_repo / "research/projects.yml"
    before = path.read_text(encoding="utf-8")
    result = run_script("new_research_session.py", "--type", "personas", "--title", "A Thing",
                        "--slug", "thing", "--date", "2026-03-01", "--no-prompt")
    assert result.returncode == 0, result.stderr
    assert path.read_text(encoding="utf-8") == before


def test_raw_frontmatter_project_tag_is_replaced_by_mapping(run_script, projects_repo):
    # What a CRUD UI edit that round-trips the exported tags would leave behind.
    edit(projects_repo / f"research/raw/{RAW_SESSION}/session-notes.md",
         "  - usability\nrelated_components", "  - usability\n  - project-cross-cutting\nrelated_components")
    records, _ = export(run_script)
    assert records[f"raw:{RAW_SESSION}"]["tags"] == ["onboarding", "usability", "project-onboarding"]


def test_unreadable_projects_yml_never_drops_records(run_script, projects_repo):
    (projects_repo / "research/projects.yml").write_text("projects: [unclosed\n", encoding="utf-8")
    records, stderr = export(run_script)
    assert len(records) == 6
    assert project_of(records[f"raw:{RAW_SESSION}"]) == "project-cross-cutting"
    assert project_of(records["component:cta-primary"]) == "project-cross-cutting"
    assert "projects.yml: unparseable" in stderr
    result = run_script("build_index.py", "--check")
    assert result.returncode == 1
    assert "projects.yml: unparseable" in result.stderr


def test_duplicate_mapping_key_is_rejected(run_script, projects_repo):
    edit(projects_repo / "research/projects.yml", "components:\n",
         f"  {RAW_SESSION}: project-cross-cutting\ncomponents:\n")
    result = run_script("build_index.py")
    assert result.returncode == 1
    assert "duplicate key" in result.stderr


@pytest.mark.parametrize("change, message", [
    (("research/findings/onboarding.md", "  - project-onboarding\n", ""),
     "onboarding.md: needs exactly one project-* tag, has none"),
    (("personas/new-user.md", "project-onboarding]", "project-onboarding, project-cross-cutting]"),
     "new-user.md: needs exactly one project-* tag"),
    (("analytics/summaries/onboarding-funnel.md", "project-onboarding]", "project-checkout]"),
     "project tag 'project-checkout' isn't listed in projects.yml"),
    (("research/projects.yml", "cta-primary: project-onboarding", "cta-primary: project-mystery"),
     "components entry 'cta-primary' uses unknown project 'project-mystery'"),
    (("research/projects.yml", "components:\n", "components:\n  gone-widget: project-onboarding\n"),
     "components entry 'gone-widget' doesn't exist"),
    (("research/projects.yml", "  - id: project-cross-cutting\n    label: Cross-cutting\n", ""),
     "'project-cross-cutting' must be listed under projects"),
    (("research/findings/tags.md", "- **`project-onboarding`** — Onboarding\n", ""),
     "project id 'project-onboarding' isn't defined in findings/tags.md"),
])
def test_build_index_rejects_bad_project_tagging(run_script, projects_repo, change, message):
    rel, old, new = change
    edit(projects_repo / rel, old, new)
    result = run_script("build_index.py")
    assert result.returncode == 1
    assert message in result.stderr
