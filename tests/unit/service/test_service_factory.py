"""Unit tests for service factory."""

from src.service import ServiceFactory
from src.service.daily_credit_card_transaction_aggregator import DailyCreditCardTransactionAggregator
from src.service.daily_user_transaction_aggregator import DailyUserTransactionAggregator

class TestServiceFactory:

    def test_create_daily_user_transaction_aggregator(self,):
        service = ServiceFactory.create_daily_user_transaction_aggregator()
        assert isinstance(service, DailyUserTransactionAggregator)

    def test_create_daily_credit_card_transaction_aggregator(self,):
        service = ServiceFactory.create_daily_credit_card_transaction_aggregator()
        assert isinstance(service,  DailyCreditCardTransactionAggregator)

