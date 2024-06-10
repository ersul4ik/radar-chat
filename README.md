# tech-radar

A short description of the project

## Development Requirements

- Python3.11.0
- Pip
- Poetry (Python Package Manager)

## Installation

```sh
python -m venv venv
source venv/bin/activate
make install
```

## Runnning Localhost

`make run`

## Runnin in Docker

`make deploy`

## Running Tests

`make test`

## Access Swagger Documentation

> <http://localhost:8080/docs>

## Access Redocs Documentation

> <http://localhost:8080/redoc>

## Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:

    app
    |
    ├── api                 - web related stuff.
    │   └── routes          - web routes.
    └── main.py             - FastAPI application creation and configuration.
    └── tests            - pytest
