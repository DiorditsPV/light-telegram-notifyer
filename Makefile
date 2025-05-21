.PHONY: install test clean lint

install:
	pip install -e .

req:
	pip install -r requirements.txt

test:
	pytest tests/

run-example:
	python ltm/utils/reply_chatid.py

build:
	python -m build --wheel

clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	rm -rf *.egg
	rm -rf *.whl
	rm -rf *.pyc
