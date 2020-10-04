{% set is_open_source = cookiecutter.open_source_license != 'Not open source' %}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![PyPI - Version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug|replace('_', '-') }}/workflows/tests/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug|replace('_', '-') }}/actions?workflow=tests)
[![Read the Docs](https://readthedocs.org/projects/{{ cookiecutter.project_slug|replace('_', '-') }}/badge/)](https://{{ cookiecutter.project_slug|replace('_', '-') }}.readthedocs.io/)
{% endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* GitHub repo: <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug|replace('_', '-') }}.git>
* Documentation: <https://{{ cookiecutter.project_slug|replace('_', '-') }}.readthedocs.io>
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}

## Features

* TODO

## Quickstart

TODO

## Credits

This package was created with [Cookiecutter][cookiecutter] and the [fedejaure/cookiecutter-modern-pypackage][cookiecutter-modern-pypackage] project template.

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cookiecutter-modern-pypackage]: https://github.com/fedejaure/cookiecutter-modern-pypackage/tree/develops
