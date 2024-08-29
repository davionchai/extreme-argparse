ENV=.venv
PYTHON_VERSION=3.9

.PHONY: check-conda
check-conda: 
	which conda

.PHONY: init
init:
	python$(PYTHON_VERSION) -m venv $(ENV)
	$(ENV)/bin/python$(PYTHON_VERSION) -m pip install --upgrade pip

.PHONY: install
install:
	$(ENV)/bin/python$(PYTHON_VERSION) -m pip install -r requirements_dev.txt

.PHONY: clean
clean:
	rm -rf logs
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf pytest_report.xml
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf extreme_argparse.egg-info

.PHONY: build
build:
	pip install -r requirements_build.txt
	python setup.py sdist bdist_wheel
