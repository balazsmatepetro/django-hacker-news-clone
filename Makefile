init:
	mkdir -p ./.venv/
	virtualenv --python=python3.8 ./.venv/py3.8

.PHONY: init
