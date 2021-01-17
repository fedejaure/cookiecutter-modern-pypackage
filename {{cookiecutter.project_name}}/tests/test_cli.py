"""Tests for `{{ cookiecutter.project_slug }}`.cli module."""
from typing import List

import pytest
from click.testing import CliRunner

import {{ cookiecutter.project_slug }}
from {{ cookiecutter.project_slug }} import cli


@pytest.mark.parametrize(
    "options,expected",
    [
        ([], "{{ cookiecutter.project_slug }}.cli.main"),
        (["--help"], "Usage: main [OPTIONS]"),
        (["--version"], f"main, version { {{ cookiecutter.project_slug }}.__version__ }\n"),
    ],
)
def test_command_line_interface(options: List[str], expected: str) -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, options)
    assert result.exit_code == 0
    assert expected in result.output
