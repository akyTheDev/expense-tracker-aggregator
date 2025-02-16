"""Shared controller objects."""

from abc import ABC, abstractmethod
from logging import Logger

from pydantic import BaseModel, ConfigDict, Field

from src.common import get_logger


class ConsumerBaseController(ABC, BaseModel):
    """Consumer base controller class."""

    model_config = ConfigDict(arbitrary_types_allowed=True)
    logger: Logger = Field(default_factory=lambda: get_logger())

    @abstractmethod
    async def consume(self, message_key: str, message_value: dict) -> None:
        """Consume the coming message and process it."""
