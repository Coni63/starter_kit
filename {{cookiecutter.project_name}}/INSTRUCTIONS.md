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

## Prerequisites

- Python 3.9 or higher installed on your system. This project is set on 3.11

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project's root directory.
1. Replace the git by one brand new for your project
    ```
    rm -r .git
    git init
    git remote add origin <path/to/git>
    ```
1. Create a virtual environment:
    ```bash
    poetry config virtualenvs.in-project true  # recommended
    poetry install
    ```
2. Add hooks to the git project
    ```bash
    pre-commit install
    ```
2. Rename modules as required (update imports)
3. In `src/api/module*/routes.py`, update the `openapi_tag` and `url_prefix` in addition of updating routes as expected.
3. Update the configuration file (see next part)

## Configuration

A configuration file in yaml is set to prepopulate as much as possible the project. This file is present at the root of the project in `config.yaml`. It currently have 2 parts:

- logging:
   - Setup for the logging module for the entire application
      - allows to simply load the logger in any app and simply log
   - refer to https://docs.python.org/3/library/logging.config.html#logging-config-fileformat
- application
   - other variable used for the project
      - feel free  to add new one
      - you can refer to it as a dictionary using:
      ```py
      from setup import cfg

      print(cfg["application"]["project"]) # -> template
      ```
This configuration is parsed when loading `setup.py` but the setup file also set other general purposes

## Development

1. Run pre-commit check regularly:
    ```bash
    pre-commit run
    pre-commit run --all-files  # use on the first run at least
    ```

2. If you change a model or create a new one:
    ```bash
    alembic revision --autogenerate -m "create account table"
    alembic upgrade head  # only if you are sure about your migration :D
    ```

3. Set the documentation sphinx

- The project already has pre-commits hooks to ensure that docstrings are generated
- The sphinx module is already set with auto-generated documentation as a result you just need to:
   - create a new rst file and populate it either with automodule/autoclass
   - add it to the index.rst (refer to module1.rst)
   - Of course you can use the full power of sphinx, this is just the minimal step

4. Run tests

The project being split between `/src/`and `/tests/` and the application's cwd is `src`, ze first need to add src to the PATH. Then tests can be run as usual:
```bash
set PYTHONPATH=%PYTHONPATH%;./src     # for Windows
export PYTHONPATH=$PYTHONPATH:./src   # for Linux

python -m unittest discover tests
python -m unittest discover tests.sub_test.script_test.ClassTest.method_test
```

The coverage is also included by replacing `unitest` by `coverage`:
```bash
set PYTHONPATH=%PYTHONPATH%;./src     # for Windows
export PYTHONPATH=$PYTHONPATH:./src   # for Linux

coverage run -m unittest discover
```


## Serve

- Locally:
    ```bash
    cd src
    uvicorn api.main:app — reload
    ```
    Navigate to http://localhost:8000/docs for the swagger documentation

- Build Docker Image
    ```bash
    poetry export -f requirements.txt -o requirements.txt  # If there is changes of dependancies, you can export the requirements with this command

    # build a new image with the updated app
    docker build --pull --rm -f "Dockerfile" -t image_name:0.1 "."

    # run the image on port 8000
    docker run --rm -d -p 8000:8000/tcp image_name:0.1
    ```

- Build the Documentation
    ```bash
    cd docs
    make html  # in PS or 'make.bat html' in CMD
    ```

## Structure

This starter template project follows the principles of Domain-Driven Design (DDD) to create a well-organized and maintainable application. The DDD approach emphasizes modeling the business domain in the application's architecture. The each module of the `src/app` part is divided into the following parts:

### Models
The models directory contains the domain entities and value objects. These are the core components representing the fundamental building blocks of your application's business logic. By encapsulating the business rules and logic within these models, you ensure that the domain logic remains separate from the infrastructure and application layers, promoting a clear separation of concerns.

### Infrastructure/alembic
The infrastructure/alembic directory houses the database migration scripts. These migration scripts are responsible for defining and updating the database schema to match the changes in the domain model. Following migrations allows for easy management of database changes without affecting existing data, ensuring a smooth evolution of the application over time.

### Infrastructure/Repository
The infrastructure/repository directory contains the implementation of the repositories. A repository acts as an abstraction over data access and provides an interface for interacting with the domain models. By placing the repository implementation in the infrastructure layer, it is easier to switch data storage technologies or manage data access concerns effectively.

### Infrastructure/Database
The infrastructure/database directory is where the database-related code resides. This could include database configuration, connection management, and any helper functions related to the database. Keeping the database-specific code separate from the rest of the application ensures that the domain model remains agnostic of the underlying storage technology.

### Application
The application directory contains the use cases and application services that orchestrate the interactions between the various domain models. Use cases represent specific actions or business processes in the application, while application services act as the bridge between the presentation layer and the domain layer.

### API
The API part of the presentation layer (handled in `src/api`) is only an access point for the application. This can be replaced by any other solutions such as UI or schedulled scripts for examples. As a result, it is responsible only to handle authentication/authorization and handling errors. The logic of the application is handled in the application layer of the app.

### Example with E-Commerce website

In an e-commerce website following the Domain-Driven Design (DDD) architecture, each layer has its distinct responsibilities:

- The Presentation Layer focuses on user interactions and rendering:
    - Provides all the API used by the website to handle items, customers, orders
    - The rendering is handled mainly by the front that is not included in this project
- The Application Layer coordinates user requests and enforces business workflows
    - Orchestrating interactions between multiple Domain Layer components to fulfill user requests, like creating an order, updating inventory, and calculating shipping costs.
    - Implementing business rules and workflow logic that govern the e-commerce processes.
- The Domain Layer encapsulates business logic and domain entities:
    - Defining and managing domain entities like Product, Cart, Order, and Customer, ensuring business rules are enforced within each entity.
    - Defining aggregates, which are consistency boundaries that enforce transactional integrity.
    - Implementing domain services for complex operations that do not naturally fit within an entity.
- The Infrastructure Layer handles technical aspects and external integrations.
    - Handle the communication with databases or external data sources for domain entities.
    - Handling communication with external services like payment gateways, shipping providers, and email services.
    - Managing caching, logging, and other cross-cutting concerns.


### Conclusion
Following the Domain-Driven Design structure in this starter template project can significantly enhance the maintainability, scalability, and extensibility of your Python application. By keeping the core domain logic separate from the infrastructure and application layers, you create a robust foundation for building and evolving complex software systems with ease.

Feel free to customize this template to fit the specific needs of your project and enjoy the benefits of Domain-Driven Design in your Python application!
