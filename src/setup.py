from __future__ import annotations

import logging.config
from pathlib import Path

import yaml
from app.module1.infrastructure.models import Base
from app.module1.infrastructure.models import ItemModel  # noqa: F401
from sqlalchemy import create_engine


def load_config() -> dict:
    print(__file__)
    file = Path(__file__).parent.parent / "config.yaml"
    print(file)
    with open(file) as f:
        config = yaml.safe_load(f.read())
    return config


def setupLogging(logging_config: dict):
    logging.config.dictConfig(logging_config)


def init_db(cfg):
    engine = create_engine(cfg["application"]["database_conn_string"], echo=True)
    Base.metadata.create_all(engine)


cfg = load_config()
setupLogging(cfg["logging"])

# If you does not want to use alembic, you can simply create the database by uncommenting the following line
# init_db(cfg)
