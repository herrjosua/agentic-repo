"""
Shared fixtures for the research/scripts test suite.

Every script under test derives its folder paths from its own __file__ (there is no --root flag
or env var), so the isolation strategy is:

  * Subprocess tests copy research/scripts/*.py into tmp_path/repo/research/scripts/ next to a
    small synthetic corpus and run the *copy* with the venv Python — the same way the CRUD UI
    backend shells out to them. The scripts' own path logic then resolves to tmp_path.
  * Direct function tests import the real modules (pytest.ini puts research/scripts on
    sys.path) and monkeypatch their module-level *_ROOT constants at the synthetic corpus.

A session-level guard snapshots every file under the real research/, design-tokens/,
analytics/, and deliverable folders before the run and fails the run if anything changed —
research/raw/ is append-only per AGENTS.md, and no test may touch real data.
"""
import os
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

# Importing the real scripts must not drop __pycache__/ into research/scripts/.
sys.dont_write_bytecode = True

REAL_REPO_ROOT = Path(__file__).resolve().parent.parent
REAL_SCRIPTS_DIR = REAL_REPO_ROOT / "research" / "scripts"

_venv_python = REAL_REPO_ROOT / ".venv" / "bin" / "python"
PYTHON = str(_venv_python) if _venv_python.exists() else sys.executable

from build_index import DELIVERABLE_FOLDERS  # noqa: E402

GUARDED_DIRS = ["research", "design-tokens", "analytics", *DELIVERABLE_FOLDERS]


# ---------------------------------------------------------------------------------------------
# Real-repo guard
# ---------------------------------------------------------------------------------------------

def _snapshot_real_repo():
    snap = {}
    for d in GUARDED_DIRS:
        root = REAL_REPO_ROOT / d
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if "__pycache__" in p.parts or not p.is_file():
                continue
            st = p.stat()
            snap[str(p.relative_to(REAL_REPO_ROOT))] = (st.st_size, st.st_mtime_ns)
    return snap


def pytest_sessionstart(session):
    session.config._real_repo_snapshot = _snapshot_real_repo()


def pytest_sessionfinish(session, exitstatus):
    before = getattr(session.config, "_real_repo_snapshot", None)
    if before is None:
        return
    after = _snapshot_real_repo()
    changed = sorted(
        {k for k in before.keys() | after.keys() if before.get(k) != after.get(k)}
    )
    if changed:
        sys.stderr.write(
            "\n❌ Tests modified the REAL repo (must only use tmp_path):\n"
            + "".join(f"   {c}\n" for c in changed)
        )
        session.exitstatus = pytest.ExitCode.TESTS_FAILED


# ---------------------------------------------------------------------------------------------
# Synthetic corpus
# ---------------------------------------------------------------------------------------------

RAW_SESSION = "2026-01-19-onboarding-usability-test"

CORPUS = {
    "research/findings/tags.md": """\
        # Tag Glossary

        - **`onboarding`** — first-run experience
        - **`usability`** — usability testing
        - **`mobile`** — mobile surfaces
        """,
    f"research/raw/{RAW_SESSION}/session-notes.md": """\
        ---
        title: Onboarding usability test
        date: 2026-01-19
        type: usability-test
        status: raw
        tags:
          - onboarding
          - usability
        related_components:
          - cta-primary
        related_findings:
          - ../../findings/onboarding.md
        ---

        # Onboarding usability test

        ## Key Findings
        - **[HIGH]** *(discoverability)* Participants missed the primary CTA.
        """,
    f"research/raw/{RAW_SESSION}/participants.md": """\
        ---
        title: Participants — Onboarding usability test
        date: 2026-01-19
        type: usability-test
        status: raw
        tags: [onboarding]
        related_components: []
        related_findings:
          - ../../findings/onboarding.md
        ---

        # Participants

        **Count:** 5
        """,
    "research/findings/onboarding.md": """\
        ---
        title: Onboarding
        date: 2026-01-20
        type: synthesis
        status: synthesized
        researcher: J. Alvarez
        tags:
          - onboarding
          - usability
        related_components:
          - cta-primary
        related_findings: []
        related_analytics:
          - onboarding-funnel.md
        ---

        # Onboarding

        Users struggle to find the primary CTA.
        """,
    "analytics/summaries/onboarding-funnel.md": """\
        ---
        title: Onboarding funnel
        date: 2026-01-21
        type: analytics
        status: synthesized
        tool: amplitude
        tags: [onboarding]
        related_findings:
          - ../../research/findings/onboarding.md
        ---

        # Onboarding funnel

        40% drop-off at step 2.
        """,
    "design-tokens/components/cta-primary.md": """\
        ---
        title: CTA Primary
        generated_from: tokens.tokens.json
        ---

        # CTA Primary

        Primary call-to-action button.
        """,
    "personas/new-user.md": """\
        ---
        title: New User
        date: 2026-01-22
        status: draft
        designer: Sam Okafor
        tags: [onboarding]
        related_findings:
          - ../research/findings/onboarding.md
        source_type: native
        segment: first-time users
        based_on: []
        ---

        # New User

        A first-time user of the app.
        """,
    "journey-maps/new-user-journey.md": """\
        ---
        title: New User Journey
        date: 2026-01-23
        status: draft
        designer: ""
        tags: [onboarding]
        related_findings: []
        source_type: native
        persona_ref: ../personas/new-user.md
        scope: onboarding
        ---

        # New User Journey

        From install to first task.
        """,
}


def write_file(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content), encoding="utf-8")
    return path


@pytest.fixture
def fake_repo(tmp_path):
    """A small, self-consistent synthetic repo (build_index.py passes clean on it once its
    indexes are generated) with a copy of research/scripts/*.py inside it."""
    root = tmp_path / "repo"
    scripts = root / "research" / "scripts"
    scripts.mkdir(parents=True)
    for src in REAL_SCRIPTS_DIR.glob("*.py"):
        (scripts / src.name).write_bytes(src.read_bytes())
    for rel, content in CORPUS.items():
        write_file(root, rel, content)
    return root


@pytest.fixture
def run_script(fake_repo):
    """Run a script *copy* inside fake_repo as a subprocess via the venv Python, the way the
    CRUD UI backend does. stdin is closed unless `input` is given, so a script that
    unexpectedly prompts fails fast instead of hanging."""
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"}

    def _run(script, *args, input=None):
        return subprocess.run(
            [PYTHON, str(fake_repo / "research" / "scripts" / script), *args],
            cwd=fake_repo,
            env=env,
            input=input,
            stdin=None if input is not None else subprocess.DEVNULL,
            capture_output=True,
            text=True,
            timeout=60,
        )

    return _run


@pytest.fixture
def patch_roots(fake_repo, monkeypatch):
    """Point the real, imported modules' *_ROOT constants at fake_repo for direct function
    tests. Returns fake_repo."""
    import build_index
    import build_search_ui
    import new_research_session

    research = fake_repo / "research"
    for mod in (build_index, build_search_ui, new_research_session):
        for name, value in {
            "RESEARCH_ROOT": research,
            "REPO_ROOT": fake_repo,
            "RAW_ROOT": research / "raw",
            "FINDINGS_ROOT": research / "findings",
            "TAGS_FILE": research / "findings" / "tags.md",
            "INDEX_FILE": research / "_index.md",
            "ANALYTICS_ROOT": fake_repo / "analytics",
            "ANALYTICS_SUMMARIES_ROOT": fake_repo / "analytics" / "summaries",
            "ANALYTICS_INDEX_FILE": fake_repo / "analytics" / "_index.md",
            "COMPONENTS_ROOT": fake_repo / "design-tokens" / "components",
            "OUTPUT_FILE": research / "search.html",
        }.items():
            if hasattr(mod, name):
                monkeypatch.setattr(mod, name, value)
    return fake_repo
