# Python Starter Template
## FastAPI, SQLAlchemy, Alembic, Sphinx, Pre-commit, unittest, and coverage

## Introduction
This is a starter template project for Python that comes preconfigured with essential libraries, enabling you to quickly kickstart your development process. It combines FastAPI, SQLAlchemy, Alembic, Sphinx, pre-commit, unittest, and coverage to provide a robust foundation for building web applications with a focus on API development.

## Features
- **Poetry** for dependancy management
- **FastAPI** for rapid API development with automatic interactive documentation.
- **SQLAlchemy** for powerful and flexible ORM (Object-Relational Mapping) to interact with databases.
- **Alembic** for easy database migrations and schema version control.
- **Sphinx** for generating detailed API documentation.
- **Pre-commit** for automatically checking code quality and applying formatting standards.
- **unittest** for writing unit tests to ensure the reliability of your code.
- **coverage** for measuring code test coverage.

### Current Status

- [x] set cwd to src
- [x] Structure
- [x] poetry
- [x] pre-commits
- [x] fastapi
- [x] Sphinx
- [x] Tests
- [x] Coverage
- [x] sqlalchemy
- [x] alembic
- [x] write some starter tests
- [x] documentation of the project
- [x] Docker build
- [x] make cookie-cutter
- [ ] Migration to SQLModel (later stage)

## Installation

1. create the project from the repository (check branch first):
```sh
cookiecutter https://github.com/Coni63/starter_kit.git --checkout convert_to_cookiecutter
```
2. fill the requested parameters but follow the rules:

```json
{
    "author": "email, name, company, anything you want"
    "license": "use the license you want, default is GPL",
    "project_name": "lowercase without space project name, default 'my_project'",
    "project_title": "nicer project name used for readme/sphinx, default 'My Project'",
    "module_name": "lowercase without space module name, default 'module1'",
    "module_title": "nicer module name used for readme/sphinx/swagger, default 'Module 1'",
    "year": 2023
}
```

3. follow the INSTRUCTION.md in the created project to start, develop, deploy it