"""Nox sessions."""
import nox
from nox_poetry import Session, session

nox.options.sessions = ["tests", "mypy"]
python_versions = ["3.8", "3.9", "3.10", "3.11"]


@session(python=python_versions)
def tests(session: Session) -> None:
    """Run the test suite."""
    session.install("invoke", "pytest", "xdoctest", "cookiecutter", "pytest-cookies")
    session.run("inv", "tests")


@session(python=python_versions)
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    session.install("invoke", "mypy")
    session.run("inv", "mypy")


@session(python="3.11")
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    session.install("invoke", "safety")
    session.run("inv", "safety")
