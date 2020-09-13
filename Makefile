.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

test: ## run tests quickly with the default Python
	python manage.py test

install: clean ## install the package to the active Python's site-packages
	python -m pip install --upgrade pip
	python -m pip install -r requirements_dev.txt

run: ## run local development server
	python manage.py runserver

createsuperuser: ## create super user
	python manage.py createsuperuser

makemigration: ## creating new migrations based on changes
	python manage.py makemigrations

migrate: ## responsible for changing migrations
	python manage.py makemigrations