CMD:=poetry run
PYMODULE:=j5
TESTS=tests
EXTRACODE:=tests_hw

all: type test lint

lint: 
	$(CMD) flake8 $(PYMODULE) $(TESTS) $(EXTRACODE)

type: 
	$(CMD) mypy $(PYMODULE) $(TESTS) $(EXTRACODE)

test: 
	$(CMD) pytest --cov=$(PYMODULE) $(TESTS)

test-cov:
	$(CMD) pytest --cov=$(PYMODULE) $(TESTS) --cov-report=html

isort:
	$(CMD) isort --recursive $(PYMODULE) $(TESTS) $(EXTRACODE)

clean:
	git clean -Xdf # Deleta arquivos que não estão no .gitignore