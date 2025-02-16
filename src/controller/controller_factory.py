"""Controller factory module."""

from functools import lru_cache

from src.controller.transaction_create_aggregator import (
    TransactionCreateAggregatorController,
)
from src.service import ServiceFactory

from .consumer_base_controller import ConsumerBaseController


class ControllerFactory:
    """Controller factory class.

    Methods:
        transaction_create_aggregator: Create transaction create aggregator controller.
    """

    @staticmethod
    @lru_cache(maxsize=1)
    def create_transaction_create_aggregator() -> ConsumerBaseController:
        """Create transaction create aggregator controller."""
        return TransactionCreateAggregatorController(
            daily_user_transaction_aggregator=ServiceFactory.create_daily_user_transaction_aggregator(),
            daily_credit_card_transaction_aggregator_service=ServiceFactory.create_daily_credit_card_transaction_aggregator(),
        )
