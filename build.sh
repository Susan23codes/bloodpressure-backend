#!/usr/bin/env bash
# exit on error
set -o errexit

pipenv install

pipenv run python manage.py migrate
pipenv run python manage.py collectstatic
pipenv run python manage.py createsuperuser --noinput
