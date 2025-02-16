"""Unit tests for sql factory class."""

from src.database import SqlFactory


class DummySettings:
    class DB:
        HOST = "localhost"
        NAME = "test_db"
        PASSWORD = "test_pass"
        USERNAME = "test_user"
        PORT = 5432

def dummy_get_settings():
    return DummySettings


class TestSqlFactory:
    def test_get_sql_instance(self, mocker):
        """Test main parameters of sql class."""
        mocker.patch('src.database.sql_factory.get_settings', side_effect=dummy_get_settings)
        SqlFactory._sql_instance = None # type: ignore
        sql_instance = SqlFactory.get_sql_instance()

        assert sql_instance.name == "test_db"
        assert sql_instance.username == "test_user"
        assert sql_instance.password == "test_pass"
        assert sql_instance.port == 5432
        assert sql_instance.host == "localhost"

        sql_instance_2 = SqlFactory.get_sql_instance()
        assert sql_instance is sql_instance_2, "SqlFactory should implement singleton pattern."

