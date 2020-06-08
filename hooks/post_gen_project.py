"""Script that run after the project is generated."""
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()
PROJECT_TESTS = PROJECT_DIRECTORY / Path("tests")
PROJECT_SRC = PROJECT_DIRECTORY / Path("{{ cookiecutter.project_slug }}")


def remove_file(filepath: str) -> None:
    """Remove a file from the file system."""
    Path.unlink(PROJECT_DIRECTORY / filepath)


if __name__ == "__main__":

    if "No command-line interface" in "{{ cookiecutter.command_line_interface }}":
        remove_file(PROJECT_TESTS / "test_cli.py")
        remove_file(PROJECT_SRC / "cli.py")

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
