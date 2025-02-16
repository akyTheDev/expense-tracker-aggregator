"""Transaction aggregator controller."""

from asyncio import gather

from overrides import override

from src.model import Transaction
from src.service import BaseService

from .consumer_base_controller import ConsumerBaseController


class TransactionCreateAggregatorController(ConsumerBaseController):
    """Transaction aggregator consumer class.

    Attributes:
        daily_credit_card_transaction_aggregator_service: The credit card transaction
            aggregator service.
        daily_user_transaction_aggregator: The user transaction aggregator service.

    Methods:
        consume: Process the transaction by calling services.
    """

    daily_credit_card_transaction_aggregator_service: BaseService
    daily_user_transaction_aggregator: BaseService

    @override
    async def consume(self, message_key: str, message_value: dict) -> None:
        """Consume the coming message and process it."""
        transaction: Transaction = Transaction(**message_value)

        results = await gather(
            self.daily_user_transaction_aggregator.create(transaction),
            self.daily_credit_card_transaction_aggregator_service.create(transaction),
            return_exceptions=True,
        )

        if any([isinstance(result, Exception) for result in results]):
            self.logger.error(
                f"An error occurred in the transaction create aggregator: {results}",
                exc_info=True,
            )
