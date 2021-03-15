#!/usr/bin/env sh

export PIPENV_VENV_IN_PROJECT=true;
pip3 install pipenv;
pipenv sync --dev --python 3.6;
export VIRTUAL_ENV=.venv/
