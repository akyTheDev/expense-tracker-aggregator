"""Main module."""

import asyncio
from json import loads
from logging import Logger
from uuid import uuid4

from aiokafka import AIOKafkaConsumer, ConsumerRecord

from src.common import Settings, get_logger, get_settings

from .controller import ConsumerBaseController, ControllerFactory

loop = asyncio.new_event_loop()
logger: Logger = get_logger()
settings: Settings = get_settings()


kafka_topics_to_controller: dict[str, ConsumerBaseController] = {
    "transaction.create": ControllerFactory.create_transaction_create_aggregator(),
}


async def main() -> None:
    """Consume messages from Kafka."""
    consumer: AIOKafkaConsumer = AIOKafkaConsumer(
        *kafka_topics_to_controller.keys(),
        bootstrap_servers=settings.KAFKA.BROKER,
        group_id=settings.KAFKA.CONSUMER_GROUP,
        security_protocol="SASL_PLAINTEXT",
        sasl_mechanism="PLAIN",
        sasl_plain_username=settings.KAFKA.USERNAME,
        sasl_plain_password=settings.KAFKA.PASSWORD,
    )

    await consumer.start()
    try:
        msg: ConsumerRecord
        async for msg in consumer:
            request_id: str = str(uuid4())
            logger.info(
                f"{[request_id]} Message arrived. Topic: {msg.topic} "
                f"Message: {msg.value}"
            )
            controller: ConsumerBaseController = kafka_topics_to_controller[msg.topic]
            try:
                await controller.consume(
                    msg.key.decode("utf-8") if msg.key else "unknown-key",
                    loads(msg.value),
                )
                logger.info(f"{[request_id]} Message handled: Request: {request_id}")
            except Exception as error:
                logger.error(
                    f"{[request_id]} Error on handling message. Error: {error}"
                )

    finally:
        await consumer.stop()


if __name__ == "__main__":
    loop.run_until_complete(main())
