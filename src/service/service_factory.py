"""Service factory module."""

from functools import lru_cache

from src.database import SqlFactory

from .base_service import BaseService
from .daily_credit_card_transaction_aggregator import (
    DailyCreditCardTransactionAggregator,
)
from .daily_user_transaction_aggregator import DailyUserTransactionAggregator


class ServiceFactory:
    """Service factory class.

    Methods:
        create_daily_credit_card_transaction_aggregator: Create daily credit card
            transaction aggregator service.
        create_daily_user_transaction_aggregator: Create daily user transaction
            aggregator service.
    """

    @staticmethod
    @lru_cache(maxsize=1)
    def create_daily_credit_card_transaction_aggregator() -> BaseService:
        """Create daily credit card transaction aggregator service."""
        return DailyCreditCardTransactionAggregator(sql=SqlFactory.get_sql_instance())

    @staticmethod
    @lru_cache(maxsize=1)
    def create_daily_user_transaction_aggregator() -> BaseService:
        """Create daily user transaction aggregator service."""
        return DailyUserTransactionAggregator(sql=SqlFactory.get_sql_instance())
