# Python Backend (Web Services), Fall 2023

Homeworks on \"Python Backend\" course conducted at ITMO University, fall 2023

## Homeworks description

### Homework 3. Microservices
Task:
* create app on the base of microservices system
* at least the 1 client microservice and 2 support microservices
* cover the functionality with tests

In this homework I created the service calculating customer lifetime value for a given period of time, based on their purchase statistics.
You can read more about the underlying models here: [https://lifetimes.readthedocs.io/en/latest](https://lifetimes.readthedocs.io/en/latest)

## Development

### Dependencies Management

Project’s dependencies are managed by [poetry](https://python-poetry.org/). So, all the dependencies and configuration parameters are listed in [pyproject.toml](pyproject.toml).

### Project structure

As it was mentioned above, this service utilizes 3 components:
* clv (which is intended for client use)
* bgnbd (containing first part of the underlying model)
* gg (containing second part of the underlying model)

Sources for all the components can be found in corresponding folders, along with their Dockerfiles.
So, any of the components can be manually built separately, however it is not the meant way of usage.
You can read about the service build pipeline in the corresponding [section](#Build)


### Build

The service can be built using [docker-compose](https://docs.docker.com/compose/).
To build the project, clone the repository and run the following command from the repository root:

```bash
docker-compose up -d
```

After that main part of the service should be binded to your 8003 port, so you can try it at
```
0.0.0.0:8003
```


### Pre-commit Hooks

This project uses pre-commit hooks for code quality checking. For this purpose [https://pre-commit.com](https://pre-commit.com/) framework is utilized.

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

### Testing

This project uses [pytest](https://docs.pytest.org/en/latest/) framework for testing.

Files with tests for each microservice are stored in corresponding folders. So, to run tests, you can execute the following command from repository root:

```bash
pytest <service>/test_<service>.py
```
where <service> is one of:
* bgnbd
* gg
* clv
