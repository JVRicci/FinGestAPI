from sqlalchemy.orm import Session

from src.models.transactions import Transaction
from src.schemas.transaction import TransactionCreate


class TransactionRepository:
    def __init__(self, db: Session):
        self._db = db

    def create(self, data: TransactionCreate) -> Transaction:
        transaction = Transaction(**data.model_dump())

        self.db.add(transaction)
        self._db.commit()
        self.db.refresh(transaction)

        return transaction

    def list(self) -> list[Transaction]:
        return self._db.query(Transaction).order_by(Transaction.created_at.desc()).all()
