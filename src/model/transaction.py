"""Transaction model."""

from datetime import date

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    """Transaction model.

    Attributes:
        userId: The user id of the transaction.
        date: The date of the transaction.
        amount: The amount of the transaction.
        description: The description of the transaction.
        card_id: The card ID of the transaction.
    """

    user_id: int = Field(ge=0, alias="userId")
    date: date
    amount: float = Field(ge=0)
    description: str = Field(default="No description")
    card_id: int = Field(alias="cardId", ge=0)
