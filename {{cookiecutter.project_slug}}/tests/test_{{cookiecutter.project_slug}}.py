"""Tests for `{{ cookiecutter.project_slug }}` package."""
import pytest
import {{ cookiecutter.project_slug }}


@pytest.fixture
def version():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    yield modern_python_boilerplate.__version__


def test_version(version):
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "{{ cookiecutter.version }}"
