"""Tests for `{{ cookiecutter.project_slug }}` module."""
from typing import Iterator

import pytest

import {{ cookiecutter.project_slug }}


@pytest.fixture
def version() -> Iterator[str]:
    """Sample pytest fixture."""
    yield {{ cookiecutter.project_slug }}.__version__


def test_version(version: Iterator[str]) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "{{ cookiecutter.version }}"
