"""Pytest configurations."""

import os

import pytest

from src.database.psql import PSql


@pytest.fixture(scope="session", autouse=True)
def set_env_variable():
    """Set environment variables."""
    os.environ['AIOCACHE_DISABLE'] = "1"
    os.environ["DB__NAME"] = "postgres"
    os.environ["DB__USERNAME"] = "username"
    os.environ["DB__PASSWORD"] = "password"
    os.environ["DB__HOST"] = "localhost"
    os.environ["DB__PORT"] = "5433"
    os.environ["LOG_LEVEL"] = "info"
    os.environ["KAFKA__CLIENT_ID"] = "kafka-client"
    os.environ["KAFKA__BROKER"] = "localhost:59092"
    os.environ["KAFKA__USERNAME"] = "admin"
    os.environ["KAFKA__PASSWORD"] = "password"
    os.environ["KAFKA__CONSUMER_GROUP"] = "expense-tracker-aggregator"

@pytest.fixture
def psql() -> PSql:
    return PSql(
        username="username",
        password="password",
        host="localhost",
        port=5433,
        name="postgres",
    )
