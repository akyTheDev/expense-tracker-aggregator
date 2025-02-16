"""Postgresql class."""

from aiocache import cached
from asyncpg import create_pool
from asyncpg.pool import Pool
from overrides import override

from .sql import Sql


class PSql(Sql):
    """Psql class."""

    @cached()
    async def _get_pool(self) -> Pool:
        """Get database connection pool."""
        return await create_pool(
            user=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.name,
            min_size=5,
            max_size=20,
            command_timeout=60,
        )

    @override
    async def fetch(self, query: str) -> list[tuple]:
        """Return the result of executing the passed query.

        Arguments:
            query: Query to perform.

        Returns:
            The result of executing the passed query.
        """
        pool: Pool = await self._get_pool()
        async with pool.acquire() as conn:
            return [tuple(row) for row in await conn.fetch(query)]

    @override
    async def execute(self, query: str) -> None:
        """Execute the passed query.

        Arguments:
            query: Query to perform.
        """
        pool: Pool = await self._get_pool()
        async with pool.acquire() as conn:
            await conn.execute(query)
