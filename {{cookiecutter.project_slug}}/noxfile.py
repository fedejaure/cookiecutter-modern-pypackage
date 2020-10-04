"""Nox sessions."""
import nox
import nox_poetry.patch  # noqa: F401
from nox.sessions import Session

nox.options.sessions = ["tests", "mypy"]


@nox.session(python=["3.6", "3.8", "3.7"])
def tests(session: Session) -> None:
    """Run the test suite."""
    session.install(".")
    session.install("invoke", "pytest", "xdoctest")
    session.run("inv", "tests")


@nox.session(python=["3.6", "3.8", "3.7"])
def mypy(session: Session) -> None:
    """Run the test suite."""
    session.install("invoke", "mypy")
    session.run("inv", "mypy")
