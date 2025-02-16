"""Unit tests for postgresql class."""

from tests.conftest import psql  # noqa: F401


class TestPsql:
    async def test_execute_and_fetch(self, psql):
        try:
            add_table_query = "create table name (id INT PRIMARY KEY, name TEXT)"
            await psql.execute(add_table_query)
            add_row_query = (
                "insert into name (id, name) values " "(1, 'test1')," "(2, 'test2')"
            )
            await psql.execute(add_row_query)
            result = await psql.fetch("select * from name")
            assert result == [
                (1,"test1"),
                (2,"test2")
            ]
        finally:
            await psql.execute("drop table name")


