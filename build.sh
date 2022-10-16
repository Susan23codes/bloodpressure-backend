#!/usr/bin/env bash
# exit on error
set -o errexit

pipenv install

pipenv run python bloodpressureTracker/manage.py migrate
