# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

### Added
- `.safety-policy.yml` file.

### Changed
- typer from `^0.9.0` to `^0.12.3`.
- coverage from `^7.4.1` to `^7.5.3`.
- pytest-cov from `^4.1.0` to `^5.0.0`.
- sphinx from `^7.2.6` to `^7.3.7`.
- black from `^24.2.0` to `^24.4.2`.
- mypy from `^1.8.0` to `^1.10.0`.
- ruff from `^0.2.1` to `^0.4.8`.
- safety from `^3.0.1` to `^3.2.1`.
- pytest from `^8.0.1` to `^8.2.2`.
- pre-commit from `^3.6.1` to `^3.7.1`.
- xdoctest from `^1.1.3` to `^1.1.4`.
- watchdog from `^4.0.0` to `^4.0.1`.
- poetry pre-commit hooks from `1.7.1` to `1.8.3`.
- codecov/codecov-action from `v3.1.4` to `v4.4.1`.
- actions/upload-artifact from `v4` to `v4.3.3`.
- actions/download-artifact from `v4` to `v4.1.7`.
- actions/setup-python from `v5.0.0` to `v5.1.0`.
- mindsers/changelog-reader-action from `v2.2.2` to `v2.2.3`.
- peter-evans/create-pull-request from `v6.0.0` to `v6.0.5`.
- actions/checkout from `v4.1.1` to `v4.1.6`.

## [3.0.1] - 2024-02-18
### Fixed
- Github funding file syntax.

## [3.0.0] - 2024-02-17
### Added
- Ruff `^0.2.1`.
- Python `3.12` support.
- `CODEOWNERS` file.
- `FUNDING.yml` file.
- poetry pre-commit hooks.
- Typer `^0.9.0`.
- `py.typed` file.
- `CITATION.cff` file.

### Changed
- mypy from `^1.7.0` to `^1.8.0`.
- actions/setup-python from `v4.7.1` to `v5.0.0`.
- sphinx from `^7.1.2` to `^7.2.6`.
- isort from `^5.12.0` to `^5.13.2`.
- black from `^23.11.0` to `^24.2.0`.
- pre-commit from `^3.5.0` to `^3.6.1`.
- github/codeql-action from `v2` to `v3`.
- coverage from `^7.3.2` to `^7.4.1`.
- pypa/gh-action-pypi-publish from from `v1.8.10` to `v1.8.11`.
- actions/upload-artifact from `v2.2.4` to `v4`.
- actions/download-artifact from `v2.0.10` to `v4`.
- Contributor Covenant from `v2.0` to `v2.1`.
- pytest from `^7.4.3` to `^8.0.1`.
- safety from `^2.4.0b2` to `^3.0.1`.
- peter-evans/create-pull-request from `v5.0.2` to `v6.0.0`.
- xdoctest from `^1.1.2` to `^1.1.3`.
- watchdog from `^3.0.0` to `^4.0.0`.

### Removed
- falke8 and flakeheaven.
- darglint.
- Python `3.8` support.
- Click in favor of Typer.

### Fixed
- template whitespace control.
- docs typo.

## [2.3.1] - 2023-11-18
### Changed
- actions/setup-python from `v4.6.1` to `v4.7.1`.
- actions/checkout from `v3.5.2` to `v4.1.1`.
- peter-evans/create-pull-request from `v5.0.1` to `v5.0.2`.
- pypa/gh-action-pypi-publish from from `v1.4.2` to `v1.8.10`.
- pre-commit-hooks from `v4.4.0` to `v4.5.0`.
- sphinx from `^7.0.1` to `^7.1.2`.
- invoke from `^2.1.2` to `^2.2.0`.
- pre-commit from `^3.3.2` to `^3.5.0`.
- black from `^23.3.0` to `^23.11.0`.
- mypy from `^1.3.0` to `^1.7.0`.
- safety from `^2.4.0b1` to `^2.4.0b2`.
- pytest from `^7.3.1` to `^7.4.3`.
- xdoctest from `^1.1.1` to `^1.1.2`.
- coverage from `^7.2.6` to `^7.3.2`.
- click from `^8.1.3` to `^8.1.7`.
- flake8-builtins from `^2.1.0` to `^2.2.0`.

### Fixed
- readthedocs config.

## [2.3.0] - 2023-05-28
### Changed
- Reorganized dev dependencies into groups.
- Renamed invoke safety task to invoke security.
- flakeheaven pre-coomit hook with local deps.

## [2.2.1] - 2023-05-25
### Changed
- Moved mypy configurations from `mypy.ini` to `pyproject.toml`.
- Moved poetry `dev-dependencies` to `group.dev.dependencies`.
- peter-evans/create-pull-request from `v4.2.3` to `v5.0.1`.
- actions/checkout from `v3.3.0` to `v3.5.2`.
- codecov/codecov-action from `v2.0.2` to `v3.1.4`.
- actions/setup-python from `v4.5.0` to `v4.6.1`.
- pytest-cov from `^3.0.0` to `^4.1.0`.
- coverage from `^7.2.1` to `^7.2.6`.
- flakeheaven from `^3.2.1` to `^3.3.0`.
- black from `^23.1.0` to `^23.3.0`.
- sphinx from `^6.1.3` to `^7.0.1`.
- flake8-bugbear from `^23.2.13` to `^23.3.12`.
- watchdog from `^2.3.1` to `^3.0.0`.
- pytest-cookies from `^0.6.1` to `^0.7.0`.
- pytest from `^7.2.2` to `^7.3.1`.
- mypy from `^1.0.1` to `^1.3.0`.
- pre-commit from `^3.1.1` to `^3.3.2`.
- invoke from `^2.0.0` to `^2.1.2`.

### Fixed
- Adjusted minimum target version for Black.

## [2.2.0] - 2023-03-09
### Added
- Python `3.11` support.
- nox-poetry.
- flake8-broken-line `^0.6.0`.
- flakeheaven `^3.2.1`.

### Changed
- black from `^21.9b0` to `^23.1.0`.
- flake8 from `^3.9.2` to `>=4.0.1,<5.0.0`.
- checkout action from `v2.3.4` to `v2.4.0`.
- darglint from `^1.8.0` to `^1.8.1`.
- actions/setup-python from `v2.2.2` to `v4.5.0`.
- actions/checkout from `v2.4.0` to `v3.3.0`.
- github/codeql-action from `v1` to `v2`.
- peter-evans/create-pull-request from `v3.10.1` to `v4.2.3`.
- mindsers/changelog-reader-action from `v2.0.0` to `v2.2.2`.
- pre-commit from `^2.15.0` to `^3.1.1`.
- isort from `^5.9.3` to `^5.12.0`.
- sphinx from `^4.2.0` to `^6.1.3`.
- flake8-bugbear from `^21.9.2` to `^23.2.13`.
- mypy from `^0.910` to `^1.0.1`.
- pre-commit-hooks from `v4.0.1` to `v4.4.0`.
- watchdog from `^2.1.6` to `^2.3.1`.
- invoke from `^1.6.0` to `^2.0.0`.
- pytest from `^6.2.5` to `^7.2.2`.
- xdoctest from `^0.15.10` to `^1.0.0`.
- flake8-bandit from `^2.1.2` to `^3.0.0`.
- safety from `^1.10.3` to `^2.4.0b1`.
- flake8-annotations from `^2.6.2` to `^2.9.1`.
- flake8-blind-except from `^0.2.0` to `^0.2.1`.
- flake8-logging-format from `^0.6.0` to `^0.9.0`.
- xdoctest from `^1.0.0` to `^1.1.1`.
- coverage from `^6.0.1` to `^7.2.1`.
- flake8-docstrings from `1.6.0` to `1.7.0`.
- flake8-builtins from `1.5.3` to `2.1.0`.
- click from `^8.0.3` to `^8.1.3`.

### Removed
- Python `3.7` support.
- flakehell `^0.9.0`.

## [2.1.0] - 2021-10-12
### Added
- Python `3.10` support.

### Changed
- pre-commit from `^2.13.0` to `^2.15.0`.
- watchdog from `^2.1.3` to `^2.1.6`.
- flake8-bugbear from `^21.4.3` to `^21.9.2`.
- xdoctest from `^0.15.5` to `^0.15.10`.
- sphinx from `^4.1.1` to `^4.2.0`.
- black from `^21.7b0` to `^21.9b0`.
- pytest from `^6.2.4` to `^6.2.5`.
- isort from `^5.9.2` to `^5.9.3`.
- peter-evans/create-pull-request from `v3.10.0` to `v3.10.1`.
- coverage from `^5.3` to `^6.0.1`.
- pytest-cov from `^2.10.1` to `^3.0.0`.
- click from `^8.0.1` to `^8.0.3`.

## [2.0.1] - 2021-07-26
### Fixed
- package discovery when `project_name` != `project_slug`.
- `end-of-file` hook.
- pypi release step only for open source projects.

### Changed
- isort from `^5.8.0` to `^5.9.2`.
- watchdog from `^2.1.2` to `^2.1.3`.
- xdoctest from `^0.15.4` to `^0.15.5`.
- mypy from `^0.902` to `^0.910`.
- sphinx from `^4.0.2` to `^4.1.1`.
- invoke from `^1.5.0` to `^1.6.0`.
- actions/upload-artifact from `v2.2.0` to `v2.2.4`.
- actions/download-artifact from `v2.0.5` to `v2.0.10`.
- codecov/codecov-action from `v1.3.1` to `v2.0.2`.
- pypa/gh-action-pypi-publish for `v1.4.1` to `v1.4.2`.

## [2.0.0] - 2021-06-12
### Added
- optional `CODE_OF_CONDUCT.md` file.
- optional `CONTRIBUTING.md` file.
- optional `SECURITY.md` file.
- multiple issue templates config.
- codeql analysis workflow.
- pre-commit autoupdate workflow.

### Changed
- sphinx from `3.5.4` to `4.0.2`.
- watchdog from `2.0.3` to `2.1.2`.
- flake8 from `3.9.1` to `3.9.2`.
- pytest from `6.2.3` to `6.2.4`.
- pre-commit from `^2.12.1` to `^2.13.0`.
- pre-commit-hooks from `^3.0.0` to `^4.0.1`.
- black from `^20.8b1` to `^21.5b2`.
- click from `^7.1.2` to `^8.0.1`.
- mypy from `^0.812` to `^0.902`.

### Removed
- Python `3.6` support.

## [1.2.3] - 2021-04-27
### Changed
- sphinx from `3.5.2` to `3.5.4`.
- flake8 from `3.8.4` to `3.9.1`.
- isort from `5.7.0` to `5.8.0`.
- flake8-bugbear from `21.3.2` to `21.4.3`.
- flake8-annotations from `2.6.1` to `2.6.2`.
- darglint from `1.7.0` to `1.8.0`.
- pytest from `6.2.2` to `6.2.3`.
- watchdog from `^2.0.2` to `^2.0.3`.
- pre-commit from `^2.11.1` to `^2.12.1`.
- actions/setup-python from `v2.2.1` to `v2.2.2`.
- pre-commit flakehell additional_dependencies versions config.

### Fixed
- flakehell config for flake8 >= 3.9.1.

## [1.2.2] - 2021-03-19
### Changed
- xdoctest from `0.15.2` to `0.15.4`.
- pre-commit from `^2.9.3` to `^2.11.1`.
- pytest from `^6.2.1` to `^6.2.2`.
- mypy from `^0.790` to `^0.812`.
- watchdog from `^1.0.2` to `^2.0.2`.
- sphinx from `^3.4.3` to `^3.5.2`.
- darglint from `^1.5.8` to `^1.7.0`.
- flake8-annotations from `^2.5.0` to `^2.6.1`.
- flake8-bugbear from `^20.11.1` to `^21.3.2`.
- flake8-docstrings from `1.5.0` to `1.6.0`.
- codecov/codecov-action from `v1.0.13` to `v1.3.1`.

### Fixed
- bump2version invoke command.

## [1.2.1] - 2021-01-23
### Changed
- xdoctest from `0.15.0` to `0.15.2`.

### Fixed
- bump2version config file.

## [1.2.0] - 2021-01-17
### Added
- pyproject `documentation` entry.
- pyproject `tool.poetry.urls` section.

### Fixed
- Readme links.

### Changed
- sphinx from `^3.4.0` to `^3.4.3`.
- safety from `^1.10.0` to `^1.10.3`.
- flake8-blind-except from `^0.1.1` to `^0.2.0`.
- flake8-annotations from `^2.1.0` to `^2.5.0`.
- isort from `^5.6.4` to `^5.7.0`.
- invoke from `^1.4.1` to `^1.5.0`.
- flakehell from `^0.7.1` to `^0.9.0`.
- parametrize cli tests.

## [1.1.3] - 2020-12-23
### Changed
- sphinx from `^3.3.0` to `^3.4.0`.
- recommonmark from `0.6.0` to `0.7.1`.
- watchdog from `^0.10.2` to `^1.0.2`.
- pre-commit from `^2.8.2` to `^2.9.3`.
- flakehell from `^0.7.0` to `^0.7.1`.
- safety from `^1.9.0` to `^1.10.0`.
- darglint from `^1.3.0` to `^1.5.8`.
- flake8-bugbear from `^20.1.4` to `^20.11.1`.
- actions/setup-python from `v2.1.4` to `v2.2.1`.
- pytest from `^6.1.2` to `^6.2.1`.

## [1.1.2] - 2020-11-07
### Changed
- flakehell from `^0.6.1` to `^0.7.0`.
- create-release action from `v1` to `v1.1.4`.
- checkout action from `v2` to `v2.3.4`.
- setup-python action from `v2` to `v2.1.4`.
- sphinx from `^3.2.1` to `^3.3.0`.
- pre-commit from `^2.7.1` to `^2.8.2`.
- pytest from `^6.1.1` to `^6.1.2`.

### Fixes
- mypy nox session requirements.

## [1.1.1] - 2020-10-18
### Fixes
- `docs/conf.py` imports.
- coverage config.

## [1.1.0] - 2020-10-17
### Changed
- to `src` structure.
- `poject_name` validation.

### Added
- `project_title`.

## [1.0.1] - 2020-10-15
### Fixed
- unnecessary `validation_depth` on `mindsers/changelog-reader-action`.

## [1.0.0] - 2020-10-15
### Added
- License section on the docs.
- Codecov integration.
- PyPI and TestPyPI steps on the release workflow.
- Python `3.9` support.

### Changed
- github actions ready to configure activity types.
- isort from `^5.5.4` to `^5.6.4`.
- bump2version from `master` to `^1.0.1`.
- mypy from `^0.782` to `^0.790`.
- coverage from `^5.1` to `^6.0.1`.
- pytest-cov from `^2.8.1` to `^2.10.1`.
- pytest from `^5.4.2` to `^6.1.1`.
- flake8 from `^3.7.9` to `^3.8.4`.

### Fixed
- missing pre-commit requirement.
- get release version on the release workflow.

## [0.2.1] - 2020-10-05
### Changed
- changelog-reader-action from v1.1.0 to v2.
- sphinx from 3.0.4 to 3.2.1.
- flakehell from 0.3.6 to 0.6.1.
- black from 19.10b0 to 20.8b1.
- xdoctest from 0.12.0 to 0.15.0.
- mypy from 0.770 to 0.782

### Fixed
- read the docs dependencies.

## [0.2.0] - 2020-10-04
### Added
- Dependabot configuration.
- Safety session to nox.
- Safety step to the test workflow.

### Changed
- flake8 version to `^3.7.9`.
- isort version to `^5.5.4`.
- poetry export without hashes on the noxfiles.

### Removed
- Pyup.io integration.
- seed-isort-config from the pre-commit-config.

### Fixed
- docs/readme.md symbolic link to README.md.
- docs/changelog.md symbolic link to CHANGELOG.md.
- missing badges.

## [0.1.4] - 2020-09-07
### Changed
- Python actions to the v2.

### Removed
- Unnecessary python steps on the release workflow.

### Fixed
- bump2version version.

## [0.1.3] - 2020-08-13
### Fixed
- isort support for pyproject.toml
- docs conf code style.

### Removed
- sphinx-autodoc-typehints from the dev requirements.

## [0.1.2] - 2020-06-14
### Fixed
- Read the docs build config.

### Removed
- Pytype from the dev requirements.

## [0.1.1] - 2020-06-14
### Added
- New option `serve` to the invoke docs task.

### Changed
- Improve docs tutorial section.
- Improve docs index section.

### Fixed
- README spelling.
- Ivoke pytype task typo.

## [0.1.0] - 2020-06-11
### Added
- First release.


[Unreleased]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v3.0.1...develop
[3.0.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v3.0.0...v3.0.1
[3.0.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v2.3.1...v3.0.0
[2.3.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v2.3.0...v2.3.1
[2.3.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v2.2.1...v2.3.0
[2.2.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v2.2.0...v2.2.1
[2.2.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v2.0.1...v2.1.0
[2.0.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v1.2.3...v2.0.0
[1.2.3]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v1.2.2...v1.2.3
[1.2.2]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v1.2.1...v1.2.2
[1.2.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v1.1.3...v1.2.0
[1.1.3]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.2.1...v1.0.0
[0.2.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.1.4...v0.2.0
[0.1.4]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/releases/tag/v0.1.0
