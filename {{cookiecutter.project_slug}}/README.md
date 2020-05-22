{% set is_open_source = cookiecutter.open_source_license != 'Not open source' %}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* GitHub repo: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug|replace('_', '-') }}.git
* Documentation: https://{{ cookiecutter.project_slug|replace('_', '-') }}.readthedocs.io.
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
