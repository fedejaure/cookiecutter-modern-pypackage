"""Tests for `cookiecutter-modern-pypackage` package."""
import datetime
import os
import shlex
import subprocess
import sys
from contextlib import contextmanager
from typing import Dict, Generator, List, Optional

import pytest
from cookiecutter.utils import rmtree
from pytest_cookies.plugin import Cookies, Result

skip_on_windows = pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")

COOKIE_CONTEXT_NOT_OPEN_SOURCE = {"open_source_license": "Not open source"}
COOKIE_CONTEXT_CLI = {"command_line_interface": "Click"}
COOKIE_CONTEXT_BSD = {"open_source_license": "BSD"}
COOKIE_CONTEXT_NO_CLI = {"command_line_interface": "No command-line interface"}
COOKIE_CONTEXT_DIFF_NAME_AND_SLUG = {
    "project_name": "some-project-name",
    "project_slug": "some_project",
}


@contextmanager
def inside_dir(dirpath: str) -> Generator[None, None, None]:
    """Execute code from inside the given directory.

    Args:
        dirpath: A path to the directory where the command is being run.

    Yields:
        None.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies: Cookies, extra_context: Optional[Dict[str, str]] = None) -> Result:
    """Bake a cookie and clean up the temporary directory created during tests.

    Args:
        cookies: The cookie to be baked, and its temporal files will be removed.
        extra_context: An optional additional context to be provided to the bake command.

    Yields:
        The baked cookie.
    """
    result = cookies.bake(extra_context=extra_context)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_dir(command: str, dirpath: str) -> int:
    """Run a command from inside a given directory, returning the exit status.

    Args:
        command: A command that will be executed.
        dirpath: A path of the directory the command is being run.

    Returns:
        The return code of the command.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command), shell=False)  # noqa: S603


def test_year_compute_in_license_file(cookies: Cookies) -> None:
    """Test that the year computed is in the license file."""
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project_path.joinpath("LICENSE.rst")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read_text()


def test_bake_with_defaults(cookies: Cookies) -> None:
    """Test bake the project with the default values."""
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "src" in found_toplevel_files
        assert "tests" in found_toplevel_files


def test_bake_not_open_source(cookies: Cookies) -> None:
    """Test bake not open-source project."""
    with bake_in_temp_dir(cookies, extra_context=COOKIE_CONTEXT_NOT_OPEN_SOURCE) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "LICENSE.rst" not in found_toplevel_files
        assert "License" not in result.project_path.joinpath("README.md").read_text()


def _test_bake_and_run_invoke_tasks(
    cookies: Cookies, extra_context: Dict[str, str], inv_tasks: List[str]
) -> None:
    """Test bake the project and check invoke tasks."""
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        assert run_inside_dir("git init", str(result.project_path)) == 0
        assert run_inside_dir("git add .", str(result.project_path)) == 0
        assert run_inside_dir('git config user.email "t@test.com"', str(result.project_path)) == 0
        assert run_inside_dir('git config user.name "Test User"', str(result.project_path)) == 0
        assert run_inside_dir("git commit -m 'initial commit'", str(result.project_path)) == 0
        assert run_inside_dir("poetry install", str(result.project_path)) == 0
        for task in inv_tasks:
            assert run_inside_dir(f"poetry run inv {task}", str(result.project_path)) == 0


@pytest.mark.parametrize(
    "extra_context",
    [
        None,
        COOKIE_CONTEXT_NOT_OPEN_SOURCE,
        {**COOKIE_CONTEXT_NOT_OPEN_SOURCE, **COOKIE_CONTEXT_NO_CLI},
        {**COOKIE_CONTEXT_CLI, **COOKIE_CONTEXT_BSD},
        COOKIE_CONTEXT_DIFF_NAME_AND_SLUG,
    ],
)
def test_bake_and_run_invoke(cookies: Cookies, extra_context: Dict[str, str]) -> None:
    """Test bake the project and check invoke tasks."""
    invoke_tasks = [
        "install-hooks",
        "hooks",
        "clean",
        "lint",
        "mypy",
        "tests",
        "coverage",
        "version -d minor",
        "docs",
    ]
    _test_bake_and_run_invoke_tasks(cookies, extra_context, invoke_tasks)
