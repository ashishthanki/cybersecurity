# Project

Basic Data Science Project format.

# Installation Instructions

- Install `pyenv`
- Install the python version in `.python-version` file.

```
pyenv install 3.12.4
```

- Ensure the python version installed:

```
pyenv which python
/Users/ashish/.pyenv/versions/3.12.4/bin/python
```

- Install [poetry](https://python-poetry.org/docs/).
- Ensure poetry environment is pointing to that python version path:

```
poetry env use <path-to-python-version>
```

- Install venv using poetry

```
poetry install
```
