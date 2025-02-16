"""Unit tests for SQL abstract class."""

from src.database import Sql


class SqlConcrete(Sql):
    async def execute(self, query):
        raise NotImplementedError

    async def fetch(self, query):
        raise NotImplementedError



class TestSql:
    def test_sql(self):
        """Test main parameters of sql class."""
        sql_concrete_class = SqlConcrete(
            name="postgres",
            username="admin",
            password="password",
            host="database.service.com",
            port=5432,
        )

        assert sql_concrete_class.name == "postgres"
        assert sql_concrete_class.username == "admin"
        assert sql_concrete_class.password == "password"
        assert sql_concrete_class.port == 5432
        assert sql_concrete_class.host == "database.service.com"
