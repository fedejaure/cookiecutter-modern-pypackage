
clean: clean-pyc clean-test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint:
	@poetry run flakehell lint {{ cookiecutter.project_slug }} tests
	@poetry run isort -rc --check-only {{ cookiecutter.project_slug }} tests
	@poetry run black --check {{ cookiecutter.project_slug }} tests

fmt:
	@poetry run isort -rc {{ cookiecutter.project_slug }} tests
	@poetry run black {{ cookiecutter.project_slug }} tests

test:
	@poetry run py.test --verbose tests

coverage:
	@poetry run py.test --verbose --cov-report term --cov-report html --cov={{ cookiecutter.project_slug }} tests

dev: clean
	poetry install

hooks:
	poetry run pre-commit install

install: clean
	poetry install --no-dev
