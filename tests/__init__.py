"""Tests module."""

from src.database import Sql, SqlFactory

def get_sql() -> Sql:
    """Get sql instance."""
    return SqlFactory.get_sql_instance()
