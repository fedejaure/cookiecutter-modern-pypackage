"""Tests for `cookiecutter-modern-pypackage` package."""
import datetime
import os
import shlex
import subprocess
from contextlib import contextmanager
from typing import Any, Iterator

from cookiecutter.utils import rmtree
from pytest_cookies.plugin import Cookies, Result


@contextmanager
def inside_dir(dirpath: str) -> Iterator[None]:
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies: Cookies, *args: Any, **kwargs: Any) -> Result:
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command: str, dirpath: str) -> int:
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def test_year_compute_in_license_file(cookies: Cookies) -> None:
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join("LICENSE")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def test_bake_with_defaults(cookies: Cookies) -> None:
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "modern_python_boilerplate" in found_toplevel_files
        assert "tests" in found_toplevel_files


def test_bake_not_open_source(cookies: Cookies) -> None:
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "LICENSE" not in found_toplevel_files
        assert "License" not in result.project.join("README.md").read()


def test_bake_and_run_lints(cookies: Cookies) -> None:
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert run_inside_dir("make install", str(result.project)) == 0
        assert run_inside_dir("make lint", str(result.project)) == 0


def test_bake_and_run_mypy(cookies: Cookies) -> None:
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert run_inside_dir("make install", str(result.project)) == 0
        assert run_inside_dir("make mypy", str(result.project)) == 0


def test_bake_and_run_tests(cookies: Cookies) -> None:
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert run_inside_dir("make install", str(result.project)) == 0
        assert run_inside_dir("make tests", str(result.project)) == 0


def test_bake_and_run_coverage(cookies: Cookies) -> None:
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert run_inside_dir("make install", str(result.project)) == 0
        assert run_inside_dir("make coverage", str(result.project)) == 0
