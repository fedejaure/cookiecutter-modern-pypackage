import datetime
from contextlib import contextmanager

from cookiecutter.utils import rmtree


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join("LICENSE")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "python_boilerplate" in found_toplevel_files
        assert "tests" in found_toplevel_files


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(cookies, extra_context={"open_source_license": "Not open source"}) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "LICENSE" not in found_toplevel_files
        assert "License" not in result.project.join("README.md").read()
