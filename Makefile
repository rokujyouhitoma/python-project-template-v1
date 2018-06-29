all: isort yapf flake8 mypy pytest

isort:
	isort

yapf:
	yapf -i -r .

flake8:
	flake8

mypy:
	mypy .

pytest:
	PYTHONPATH=src pytest
