"""Unit tests for daily credit card transaction aggregator service."""

import pytest
from datetime import date

from src.service.daily_credit_card_transaction_aggregator import (
    DailyCreditCardTransactionAggregator,
)

from src.model import Transaction


@pytest.fixture
def service(
    psql,
) -> DailyCreditCardTransactionAggregator:
    return DailyCreditCardTransactionAggregator(sql=psql)


class TestDailyCreditCardTransactionAggregatorCreate():
    async def test_should_insert_a_new_line_if_date_is_new(self, service: DailyCreditCardTransactionAggregator,psql):
        try:
            await service.create(
                Transaction(
                    userId=1,
                    cardId=13,
                    amount=123,
                    date=date(2025,2,3),
                )
            )

            [(credit_card_id,amount,aggregation_count,aggregation_date)]= await psql.fetch(
                "select credit_card_id,amount,aggregation_count,aggregation_date "
                "from daily_credit_card_aggregation "
                "where credit_card_id=13"
            )

            assert credit_card_id==13
            assert amount==123
            assert aggregation_count==1
            assert aggregation_date==date(2025,2,3)

        finally:
            await psql.execute(
                "delete from daily_credit_card_aggregation where credit_card_id=13"
            )


    async def test_should_update_existing_line(self, service: DailyCreditCardTransactionAggregator,psql):
        try:
            await service.create(
                Transaction(
                userId=1,
                cardId=100,
                amount=500,
                date=date(2025,1,3)
                )
            )

            [(credit_card_id,amount,aggregation_count,aggregation_date)]= await psql.fetch(
                "select credit_card_id,amount,aggregation_count,aggregation_date "
                "from daily_credit_card_aggregation "
                "where credit_card_id=100 and aggregation_date='2025-01-03'"
            )

            assert credit_card_id==100
            assert amount==2000
            assert aggregation_count==14
            assert aggregation_date==date(2025,1,3)


        finally:
            await psql.execute(
                "update daily_credit_card_aggregation "
                "set amount=1500, aggregation_count=13 "
                "where credit_card_id=100 and aggregation_date='2025-01-03'"
            )

class TestDailyCreditCardTransactionAggregatorDelete():
 
    async def test_should_throw_not_implemented_error(self, service: DailyCreditCardTransactionAggregator):
        with pytest.raises(NotImplementedError):
            await service.delete(Transaction(
                userId=1,
                cardId=13,
                amount=500,
                date=date(2025,1,3)
            ))
