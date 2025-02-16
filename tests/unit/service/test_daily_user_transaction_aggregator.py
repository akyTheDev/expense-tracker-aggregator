"""Unit tests for daily credit card transaction aggregator service."""

import pytest
from datetime import date

from src.service.daily_user_transaction_aggregator import (
    DailyUserTransactionAggregator,
)

from src.model import Transaction


@pytest.fixture
def service(
    psql,
) -> DailyUserTransactionAggregator:
    return DailyUserTransactionAggregator(sql=psql)


class TestDailyUserTransactionAggregatorCreate():
    async def test_should_insert_a_new_line_if_date_is_new(self, service:DailyUserTransactionAggregator,psql):
        try:
            await service.create(
                Transaction(
                    userId=987,
                    cardId=13,
                    amount=123,
                    date=date(2025,2,3),
                )
            )

            [(user_id,amount,aggregation_count,aggregation_date)]= await psql.fetch(
                "select user_id,amount,aggregation_count,aggregation_date "
                "from daily_user_aggregation "
                "where user_id=987"
            )

            assert user_id==987
            assert amount==123
            assert aggregation_count==1
            assert aggregation_date==date(2025,2,3)

        finally:
            await psql.execute(
                "delete from daily_user_aggregation where user_id=987"
            )


    async def test_should_update_existing_line(self, service: DailyUserTransactionAggregator,psql):
        try:
            await service.create(
                Transaction(
                userId=101,
                cardId=123,
                amount=500,
                date=date(2025,1,3)
                )
            )

            [(user_id,amount,aggregation_count,aggregation_date)]= await psql.fetch(
                "select user_id,amount,aggregation_count,aggregation_date "
                "from daily_user_aggregation "
                "where user_id=101 and aggregation_date='2025-01-03'"
            )

            assert user_id==101
            assert amount==1500
            assert aggregation_count==35
            assert aggregation_date==date(2025,1,3)


        finally:
            await psql.execute(
                "update daily_user_aggregation "
                "set amount=1000, aggregation_count=34 "
                "where user_id=101 and aggregation_date='2025-01-03'"
            )

class TestDailyUserTransactionAggregatorUpdate():
 
    async def test_should_throw_not_implemented_error(self, service:DailyUserTransactionAggregator):
        with pytest.raises(NotImplementedError):
            await service.delete(Transaction(
                userId=1,
                cardId=13,
                amount=500,
                date=date(2025,1,3)
            ))
