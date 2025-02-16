"""Integration tests for transaction create controller."""
import pytest
from src.model import Transaction
from src.service import BaseService
from src.controller.transaction_create_aggregator import TransactionCreateAggregatorController

@pytest.fixture
def dummy_transaction_data():
    return {
        "amount": 100.0,
        "date":"2023-05-01",
        "cardId":123,
        "userId":987
    }

@pytest.fixture
def controller(mocker):
    mock_daily_user_service: BaseService = mocker.Mock(spec=BaseService)
    mock_daily_user_service.create = mocker.AsyncMock(return_value="user_result")
    
    mock_daily_cc_service: BaseService = mocker.Mock(spec=BaseService)
    mock_daily_cc_service.create = mocker.AsyncMock(return_value="cc_result")
    
    return TransactionCreateAggregatorController(
        daily_user_transaction_aggregator=mock_daily_user_service,
        daily_credit_card_transaction_aggregator_service=mock_daily_cc_service,
    )
 

class TestTransactionCreateAggregatorController:

    async def test_consume_success(self, dummy_transaction_data, controller):
        await controller.consume("", dummy_transaction_data)
        
        transaction = Transaction(**dummy_transaction_data)
        
        controller.daily_user_transaction_aggregator.create.assert_awaited_once_with(transaction)
        controller.daily_credit_card_transaction_aggregator_service.create.assert_awaited_once_with(transaction)
        

    async def test_consume_handles_exceptions(self, mocker, controller, dummy_transaction_data):
        controller.logger = mocker.Mock()

        controller.daily_user_transaction_aggregator.create.side_effect = Exception("User service error")

        await controller.consume("", dummy_transaction_data)

        transaction = Transaction(**dummy_transaction_data)

        controller.daily_user_transaction_aggregator.create.assert_awaited_once_with(transaction)
        controller.daily_credit_card_transaction_aggregator_service.create.assert_awaited_once_with(transaction)
        controller.logger.error.assert_called_once()

