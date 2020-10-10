# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]
### Changed
- github actions ready to configure activity types.
- isort from `^5.5.4` to `^5.5.4`.

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


[Unreleased]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.2.1...develop
[0.2.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.1.4...v0.2.0
[0.1.4]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/fedejaure/cookiecutter-modern-pypackage/compare/releases/tag/v0.1.0
