"""Daily user transaction aggregator service module."""

from overrides import override
from pydantic import Field
from pypika import PostgreSQLQuery as PsqlQuery
from pypika import Table

from src.common import get_constants
from src.model import Transaction

from .base_service import BaseService


class DailyUserTransactionAggregator(BaseService[Transaction]):
    """Daily user transaction aggregator service class."""

    aggregation_table: Table = Field(
        default_factory=lambda: Table(get_constants()["daily_user_aggregation_table"])
    )

    @override
    async def create(self, data: Transaction) -> None:
        """Process the create request.

        If there is any existing row with the same user and date, then
        update the existing row. Otherwise, insert a new row.

        Arguments:
            data: Transaction data.

        Returns:
            None.
        """
        query = (
            PsqlQuery.into(self.aggregation_table)
            .columns(
                "user_id",
                "amount",
                "aggregation_count",
                "aggregation_date",
            )
            .insert(data.user_id, data.amount, 1, data.date)
            .on_conflict("user_id", "aggregation_date")
            .do_update(
                self.aggregation_table.amount,
                self.aggregation_table.amount + data.amount,
            )
            .do_update(
                self.aggregation_table.aggregation_count,
                self.aggregation_table.aggregation_count + 1,
            )
        )

        await self.sql.execute(str(query))

    @override
    async def delete(self, data: Transaction) -> None:
        """Process the delete request."""
        raise NotImplementedError("The delete method is not implemented!")
