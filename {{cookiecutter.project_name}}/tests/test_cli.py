"""Tests for `{{ cookiecutter.project_slug }}`.cli module."""

from typing import List

import pytest
from typer.testing import CliRunner

import {{ cookiecutter.project_slug }}
from {{ cookiecutter.project_slug }} import cli

runner = CliRunner()


@pytest.mark.parametrize(
    "options,expected",
    [
        ([], "{{ cookiecutter.project_slug }}.cli.main"),
        (["--help"], "Usage: "),
        (
            ["--version"],
            f"{{ cookiecutter.project_name }}, version { {{ cookiecutter.project_slug }}.__version__ }\n",
        ),
    ],
)
def test_command_line_interface(options: List[str], expected: str) -> None:
    """Test the CLI."""
    result = runner.invoke(cli.app, options)
    assert result.exit_code == 0
    assert expected in result.stdout
