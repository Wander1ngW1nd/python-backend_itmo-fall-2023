# Python Backend (Web Services), Fall 2023

Homeworks on \"Python Backend\" course conducted at ITMO University, fall 2023

## Homeworks description

### Homework 1. Hello World
Task:
* create "Hello world" app
* implement several entrypoints: path-, query- and request-body-based
* configure linters and formatters
* add comments and docstrings to functions

## Development

### Dependencies Management

Project’s dependencies are managed by [poetry](https://python-poetry.org/). So, all the dependencies and configuration parameters are listed in [pyproject.toml](pyproject.toml).


### Pre-commit Hooks

This project uses pre-commit hooks for code quality checking. For this purpose [https://pre-commit.com](https://pre-commit.com/) framework is utilized.

Now the following linters are used for pre-commit hooks:

- [black](https://black.readthedocs.io/en/latest/)
- [isort](https://pycqa.github.io/isort/)
- [mypy](https://mypy.readthedocs.io/en/stable/)
- [pylint](https://pylint.readthedocs.io/en/latest/index.html)

Their specific configuration details can be found in [pyproject.toml](pyproject.toml).

To initialize pre-commit hooks, you need to execute the following command:

```bash
pre-commit install
```

To manually check the staged code base before committing you can run:

```bash
pre-commit run
```

If you want to check all files, not only those staged for commit, run:

```bash
pre-commit run --all-files
```

To skip some hooks while committing:

```bash
SKIP=black git commit -m "foo"
```
