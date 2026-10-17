SHELL := /bin/bash

.PHONY: rs mm mig csu sa rc rcf rf rfc rm

rs:
	uv run djcodebot/manage.py runserver

mm:
	uv run djcodebot/manage.py makemigrations

mig:
	uv run djcodebot/manage.py migrate

csu:
	uv run djcodebot/manage.py createsuperuser

sa:
	@echo -n "Enter app name: "; read app_name; uv run djcodebot/manage.py startapp $$app_name

rc:
	uv run ruff check .

rcf:
	uv run ruff check . --fix

rf:
	uv run ruff format .

rfc:
	uv run ruff format --check .

rm:
	uv run mypy --config-file mypy.ini
