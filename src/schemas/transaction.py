from decimal import Decimal
from pydantic import BaseModel

from src.models.transactions import TransactionType


class TransactionCreate(BaseModel):
    """Schema for creating a transaction."""

    description: str
    amount: Decimal
    type: TransactionType
    category: str


class TransactionResponse(BaseModel):
    id: int
    description: str
    amount: Decimal
    type: TransactionType
    category: str

    class Config:
        from_attributes = True
