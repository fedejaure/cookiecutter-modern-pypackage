"""Script that run after the project is generated."""
from pathlib import Path
from typing import Union
import shutil
import os

PROJECT_DIR = Path.cwd()
PROJECT_TESTS = PROJECT_DIR / Path("tests")
PROJECT_SRC = PROJECT_DIR / Path("src/{{ cookiecutter.project_slug }}")
PROJECT_DOCS = PROJECT_DIR / Path("docs")


def remove_file(filepath: Union[str, Path]) -> None:
    """Remove a file from the file system."""
    Path.unlink(PROJECT_DIR / filepath)


def remove_folder(folder_path: Union[str, Path]) -> None:
    """Remove a folder from the file system."""
    shutil.rmtree(PROJECT_DIR / folder_path)


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
        remove_file("LICENSE.rst")
    else:
        add_symlink(PROJECT_DOCS / "license.rst", "../LICENSE.rst")

    if "Poetry" == "{{ cookiecutter.package_tool}}":
        remove_file(PROJECT_DIR / "Pipfile")
        remove_file(PROJECT_DIR / "Pipfile.lock")
        remove_folder(PROJECT_DIR / "tools")
        remove_file(PROJECT_DIR / 'Makefile')
        os.system("invoke install")
    else:
        remove_file(PROJECT_DIR / "poetry.lock")
        remove_file(PROJECT_DIR / "pyproject.toml")
        os.system(PROJECT_DIR / "tools/install_hooks.sh")
        os.system(PROJECT_DIR / "tools/install.sh")



    add_symlink(PROJECT_DOCS / "readme.md", "../README.md")
    add_symlink(PROJECT_DOCS / "changelog.md", "../CHANGELOG.md")

