"""Nox sessions."""
import tempfile
from typing import Any

import nox
from nox.sessions import Session

nox.options.sessions = ["tests", "mypy"]


def install_with_constraints(session: Session, *args: str, **kwargs: Any) -> None:
    """Install packages constrained by Poetry's lock file.

    This function is a wrapper for nox.sessions.Session.install. It
    invokes pip to install packages inside of the session's virtualenv.
    Additionally, pip is passed a constraints file generated from
    Poetry's lock file, to ensure that the packages are pinned to the
    versions specified in poetry.lock. This allows you to manage the
    packages as Poetry development dependencies.

    Arguments:
        session: The Session object.
        args: Command-line arguments for pip.
        kwargs: Additional keyword arguments for Session.install.
    """
    with tempfile.NamedTemporaryFile(delete=False) as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=["3.6", "3.8", "3.7"])
def tests(session: Session) -> None:
    """Run the test suite."""
    install_with_constraints(
        session, "invoke", "pytest", "xdoctest", "cookiecutter", "pytest-cookies"
    )
    session.run("inv", "tests")


@nox.session(python=["3.6", "3.8", "3.7"])
def mypy(session: Session) -> None:
    """Run the test suite."""
    install_with_constraints(session, "invoke", "mypy")
    session.run("inv", "mypy")
