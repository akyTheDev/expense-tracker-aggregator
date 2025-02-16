"""Shared service objects."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, validate_call

from src.database import Sql

T = TypeVar("T")


class BaseService(ABC, BaseModel, Generic[T]):
    """Base service class.

    Attributes:
        logger: The logger object.
        sql: The sql database instance.


    Methods:
        create: Process the create request.
        delete: Process the delete request.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    sql: Sql

    @abstractmethod
    @validate_call
    async def create(self, data: T) -> None:
        """Process the create request."""

    @abstractmethod
    @validate_call
    async def delete(self, data: T) -> None:
        """Process the delete request."""
