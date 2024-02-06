"""Tasks for maintaining the project.

Execute 'invoke --list' for guidance on using Invoke
"""

import platform
import webbrowser
from pathlib import Path
from typing import Optional

from invoke import call, task
from invoke.context import Context
from invoke.runners import Result

ROOT_DIR = Path(__file__).parent
DOCS_DIR = ROOT_DIR.joinpath("docs")
DOCS_BUILD_DIR = DOCS_DIR.joinpath("_build")
DOCS_INDEX = DOCS_BUILD_DIR.joinpath("index.html")
TEST_DIR = ROOT_DIR.joinpath("tests")
PYTHON_TARGETS = [
    TEST_DIR,
    ROOT_DIR.joinpath("hooks"),
    DOCS_DIR.joinpath("conf.py"),
    ROOT_DIR.joinpath("noxfile.py"),
    Path(__file__),
]
PYTHON_TARGETS_STR = " ".join([str(p) for p in PYTHON_TARGETS])


def _run(c: Context, command: str) -> Optional[Result]:
    return c.run(command, pty=platform.system() != "Windows")


@task()
def bake(c: Context, replay: bool = False) -> None:
    """Bake the cookie."""
    bake_options = (
        ["--replay", "--overwrite-if-exists"]
        if replay
        else ["--no-input", "--overwrite-if-exists"]
    )
    _run(c, f"poetry run cookiecutter {' '.join(bake_options)} .")


@task()
def watch(c: Context, replay: bool = False) -> None:
    """Bake and watch for changes."""
    bake(c, replay=replay)
    _run(
        c,
        f"poetry run watchmedo shell-command -p '*.*' "
        f"-c 'inv bake {'--replay' if replay else ''}' "
        "-W -R -D {{ cookiecutter.project_name }}",
    )


@task()
def clean_build(c: Context) -> None:
    """Clean up files from package building."""
    _run(c, "rm -fr build/")
    _run(c, "rm -fr dist/")
    _run(c, "rm -fr .eggs/")
    _run(c, "find . -name '*.egg-info' -exec rm -fr {} +")
    _run(c, "find . -name '*.egg' -exec rm -f {} +")


@task()
def clean_python(c: Context) -> None:
    """Clean up python file artifacts."""
    _run(c, "find . -name '*.pyc' -exec rm -f {} +")
    _run(c, "find . -name '*.pyo' -exec rm -f {} +")
    _run(c, "find . -name '*~' -exec rm -f {} +")
    _run(c, "find . -name '__pycache__' -exec rm -fr {} +")


@task()
def clean_tests(c: Context) -> None:
    """Clean up files from testing."""
    _run(c, "rm -fr .pytest_cache")


@task()
def clean_docs(c: Context) -> None:
    """Clean up files from documentation builds."""
    _run(c, f"rm -fr {DOCS_BUILD_DIR}")


@task(pre=[clean_build, clean_python, clean_tests, clean_docs])
def clean(c: Context) -> None:
    """Run all clean sub-tasks."""


@task()
def install_hooks(c: Context) -> None:
    """Install pre-commit hooks."""
    _run(c, "poetry run pre-commit install")


@task()
def hooks(c: Context) -> None:
    """Run pre-commit hooks."""
    _run(c, "poetry run pre-commit run --all-files")


@task(name="format", help={"check": "Checks if source is formatted without applying changes"})
def format_(c: Context, check: bool = False) -> None:
    """Format code."""
    isort_options = ["--check-only", "--diff"] if check else []
    _run(c, f"poetry run isort {' '.join(isort_options)} {PYTHON_TARGETS_STR}")
    black_options = ["--diff", "--check"] if check else ["--quiet"]
    _run(c, f"poetry run black {' '.join(black_options)} {PYTHON_TARGETS_STR}")


@task()
def ruff(c: Context) -> None:
    """Run ruff."""
    _run(c, f"poetry run ruff check {PYTHON_TARGETS_STR}")


@task()
def security(c: Context) -> None:
    """Run security related checks."""
    _run(
        c,
        "poetry export --with dev --format=requirements.txt --without-hashes | "
        "poetry run safety check --stdin --full-report",
    )


@task(pre=[ruff, security, call(format_, check=True)])
def lint(c: Context) -> None:
    """Run all linting."""


@task()
def mypy(c: Context) -> None:
    """Run mypy."""
    _run(c, f"poetry run mypy {PYTHON_TARGETS_STR}")


@task()
def tests(c: Context) -> None:
    """Run tests."""
    pytest_options = ["--xdoctest"]
    _run(c, f"poetry run pytest {' '.join(pytest_options)} {TEST_DIR}")


@task(
    help={
        "serve": "Build the docs watching for changes",
        "open_browser": "Open  the docs in the web browser",
    }
)
def docs(c: Context, serve: bool = False, open_browser: bool = False) -> None:
    """Build documentation."""
    build_docs = f"sphinx-build -b html {DOCS_DIR} {DOCS_BUILD_DIR}"
    _run(c, build_docs)
    if open_browser:
        webbrowser.open(DOCS_INDEX.absolute().as_uri())
    if serve:
        _run(c, f"poetry run watchmedo shell-command -p '*.rst;*.md' -c '{build_docs}' -R -D .")


@task(
    help={
        "part": "Part of the version to be bumped.",
        "dry_run": "Don't write any files, just pretend. (default: False)",
    }
)
def version(c: Context, part: str, dry_run: bool = False) -> None:
    """Bump version."""
    bump_options = ["--dry-run"] if dry_run else []
    _run(c, f"poetry run bump2version {' '.join(bump_options)} {part}")
