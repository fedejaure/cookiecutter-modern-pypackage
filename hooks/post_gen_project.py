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

    if "Pipenv" == "{{ cookiecutter.package_tool}}":
        shutil.copyfile("./pipenv_files/Pipfile", PROJECT_DIR / "Pipfile")
        shutil.copyfile("./pipenv_files/Pipfile.lock", PROJECT_DIR / "Pipfile.lock")
        shutil.copyfile("./pipenv_files/Makefile", PROJECT_DIR / "Makefile")
        os.system(PROJECT_DIR / "tools/install_hooks.sh")
        os.system(PROJECT_DIR / "tools/install.sh")
    else:
        shutil.copyfile("./poetry_files/noxfile.py", PROJECT_DIR / "noxfile.py")
        shutil.copyfile("./poetry_files/pyproject.toml", PROJECT_DIR / "pyproject.toml")
        shutil.copyfile("./poetry_files/tasks.py", PROJECT_DIR / "tasks.py")

    remove_folder(PROJECT_DIR / "pipenv_files")
    remove_folder(PROJECT_DIR / "poetry_files")
    add_symlink(PROJECT_DOCS / "readme.md", "../README.md")
    add_symlink(PROJECT_DOCS / "changelog.md", "../CHANGELOG.md")

