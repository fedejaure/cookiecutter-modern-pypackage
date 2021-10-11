"""Nox sessions."""
import platform
import tempfile
from typing import Any

import nox
from nox.sessions import Session

nox.options.sessions = ["tests", "mypy"]
python_versions = ["3.7", "3.8", "3.9", "3.10"]


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
            "--without-hashes",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=python_versions)
def tests(session: Session) -> None:
    """Run the test suite."""
    session.install(".")
    install_with_constraints(
        session, "invoke", "pytest", "xdoctest", "coverage[toml]", "pytest-cov"
    )
    try:
        session.run(
            "inv",
            "tests",
            env={
                "COVERAGE_FILE": f".coverage.{platform.system()}.{platform.python_version()}",
            },
        )
    finally:
        if session.interactive:
            session.notify("coverage")


@nox.session
def coverage(session: Session) -> None:
    """Produce the coverage report."""
    args = session.posargs if session.posargs and len(session._runner.manifest) == 1 else []
    install_with_constraints(session, "invoke", "coverage[toml]")
    session.run("inv", "coverage", *args)


@nox.session(python=python_versions)
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    session.install(".")
    install_with_constraints(session, "invoke", "mypy")
    session.run("inv", "mypy")


@nox.session(python="3.10")
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    install_with_constraints(session, "invoke", "safety")
    session.run("inv", "safety")
