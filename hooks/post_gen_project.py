"""Script that run after the project is generated."""
from pathlib import Path
from typing import Union

PROJECT_DIRECTORY = Path.cwd()
PROJECT_TESTS = PROJECT_DIRECTORY / Path("tests")
PROJECT_SRC = PROJECT_DIRECTORY / Path("{{ cookiecutter.project_slug }}")
PROJECT_DOCS = PROJECT_DIRECTORY / Path("docs")


def remove_file(filepath: Union[str, Path]) -> None:
    """Remove a file from the file system."""
    Path.unlink(PROJECT_DIRECTORY / filepath)


def add_symlink(path: Path, target: Union[str, Path], target_is_directory: bool = False) -> None:
    """Add symbolic link to target."""
    if path.is_symlink():
        path.unlink()
    path.symlink_to(target, target_is_directory)


if __name__ == "__main__":

    if "No command-line interface" in "{{ cookiecutter.command_line_interface }}":
        remove_file(PROJECT_TESTS / "test_cli.py")
        remove_file(PROJECT_SRC / "cli.py")

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    add_symlink(PROJECT_DOCS / "readme.md", "../README.md")
    add_symlink(PROJECT_DOCS / "changelog.md", "../CHANGELOG.md")
