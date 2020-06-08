"""Tests for `{{ cookiecutter.project_slug }}`.cli module."""
from click.testing import CliRunner

import {{ cookiecutter.project_slug }}
from {{ cookiecutter.project_slug }} import cli


def test_command_line_interface() -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_slug }}.cli.main" in result.output


def test_command_line_interface_help() -> None:
    """Test the CLI help option."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert f"Usage: main [OPTIONS]" in help_result.output


def test_command_line_interface_version() -> None:
    """Test the CLI version option."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--version"])
    assert help_result.exit_code == 0
    assert f"main, version { {{ cookiecutter.project_slug }}.__version__ }\n" == help_result.output
