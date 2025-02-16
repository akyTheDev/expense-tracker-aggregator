"""Unit tests for controller factory."""

from src.controller import ControllerFactory
from src.controller.transaction_create_aggregator import TransactionCreateAggregatorController
from src.service import ServiceFactory
from src.service import BaseService

from tests import get_sql


class DummyService(BaseService):
    async def create(self, data):
        return None

    async def delete(self, data):
        return None

class TestControllerFactory:
    def test_create_transaction_create_aggregator(self, mocker):

        # Patch ServiceFactory's creation methods.
        mocker.patch.object(
            ServiceFactory,
            "create_daily_user_transaction_aggregator",
            return_value=DummyService(sql=get_sql())
        )
        mocker.patch.object(
            ServiceFactory,
            "create_daily_credit_card_transaction_aggregator",
            return_value=DummyService(sql=get_sql())
        )
        controller = ControllerFactory.create_transaction_create_aggregator()
        assert isinstance(controller, TransactionCreateAggregatorController)

