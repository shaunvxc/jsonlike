SHELL := /bin/bash

init:
	@pip install -r requirements.txt

test:
	@nosetests ./tests/
