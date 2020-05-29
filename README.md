# Cookiecutter Modern PyPackage

![Tests](https://github.com/fedejaure/cookiecutter-modern-pypackage/workflows/Tests/badge.svg)

[Cookiecutter][cookiecutter] template for a modern Python package.

* GitHub repo: <https://github.com/fedejaure/cookiecutter-modern-pypackage.git>
* Free software: MIT license

## Features

* Dependency tracking using poetry
* Testing setup pytest
* Github Actions ready for Continuous Integration testing
* Linting provided by flake8 with flakehell
* Docstring linting provided by [Darglint][darglint] using the [Google Python Style Guide][google styleguide]
* Static type checking by [Mypy][mypy]
* Formatting provided by black and isort
* Checks dependencies for known security vulnerabilities with [Safety][safety]
* [pre-commit][pre-commit] hooks.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter https://github.com/fedejaure/cookiecutter-modern-pypackage.git
```

Then:

* Create a repo and put it there.
* Install the dev requirements into a virtualenv. (`poetry install`)

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[pytest]: https://github.com/pytest-dev/pytest
[github actions]: https://github.com/features/actions
[flake8]: https://gitlab.com/pycqa/flake8
[flakehell]: https://github.com/life4/flakehell
[isort]: https://github.com/timothycrosley/isort
[black]: https://github.com/psf/black
[darglint]: https://github.com/terrencepreilly/darglint
[mypy]: https://github.com/python/mypy
[pre-commit]: https://pre-commit.com/
[safety]: https://github.com/pyupio/safety
[google styleguide]: https://google.github.io/styleguide/pyguide.html
