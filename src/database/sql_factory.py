"""Sql factory."""

from src.common import get_settings

from .psql import PSql
from .sql import Sql


class SqlFactory:
    """Database factory class."""

    _sql_instance: Sql = None

    @classmethod
    def get_sql_instance(cls) -> Sql:
        """Get the SQL database instance.

        If the instance does not exist, create it.

        Returns:
            The SQL database instance.
        """
        if cls._sql_instance is None:
            settings = get_settings()
            cls._sql_instance = PSql(
                host=settings.DB.HOST,
                name=settings.DB.NAME,
                password=settings.DB.PASSWORD,
                username=settings.DB.USERNAME,
                port=settings.DB.PORT,
            )

        return cls._sql_instance
