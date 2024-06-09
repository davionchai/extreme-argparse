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

