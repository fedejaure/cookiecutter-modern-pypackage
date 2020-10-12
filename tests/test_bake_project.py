"""Tests for `cookiecutter-modern-pypackage` package."""
import datetime
import os
import shlex
import subprocess
from contextlib import contextmanager
from typing import Any, Dict, Generator

import pytest
from cookiecutter.utils import rmtree
from pytest_cookies.plugin import Cookies, Result


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
def bake_in_temp_dir(cookies: Cookies, *args: Any, **kwargs: Any) -> Result:
    """Delete the temporal directory that is created when executing the tests.

    Args:
        cookies: A cookie to be baked and its temporal files will be removed.
        *args: Variable length argument list to be passed to the bake command.
        **kwargs: Arbitrary keyword arguments to be passed to the bake command.

    Yields:
        The baked cookie.
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command: str, dirpath: str) -> int:
    """Run a command from inside a given directory, returning the exit status.

    Args:
        command: A command that will be executed.
        dirpath: A path of the directory the command is being run.

    Returns:
        The return code of the command.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def test_year_compute_in_license_file(cookies: Cookies) -> None:
    """Test that the year computed is in the license file."""
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join("LICENSE.rst")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def test_bake_with_defaults(cookies: Cookies) -> None:
    """Test bake the project with the default values."""
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "modern_python_boilerplate" in found_toplevel_files
        assert "tests" in found_toplevel_files


def test_bake_not_open_source(cookies: Cookies) -> None:
    """Test bake not open-source project."""
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "LICENSE.rst" not in found_toplevel_files
        assert "License" not in result.project.join("README.md").read()


@pytest.mark.parametrize(
    "extra_context",
    [
        {},
        {"open_source_license": "Not open source"},
        {
            "open_source_license": "Not open source",
            "command_line_interface": "No command-line interface",
        },
        {"open_source_license": "BSD", "command_line_interface": "Click"},
    ],
)
def test_bake_and_run_invoke(cookies: Cookies, extra_context: Dict[str, str]) -> None:
    """Test bake the project and check invoke commands."""
    invoke_commands = [
        "inv clean",
        "inv lint",
        "inv mypy",
        "inv tests",
        "inv coverage",
        "inv docs",
        "inv version -d minor",
    ]
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        assert result.project.isdir()
        assert run_inside_dir("poetry install", str(result.project)) == 0
        for inv_cmd in invoke_commands:
            assert run_inside_dir(f"poetry run {inv_cmd}", str(result.project)) == 0
