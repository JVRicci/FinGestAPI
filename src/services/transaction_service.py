from sqlalchemy.orm import Session

from src.core.redis import redis_client
from src.repositories.transaction_repository import TransactionRepository
from src.schemas.transaction import TransactionCreate


class TransactionService:
    def __init__(self, db: Session):
        self._repository = TransactionRepository(db)

    def create_transaction(self, data: TransactionCreate):
        """Create a new transaction and invalidate the dashboard summary cache."""
        transaction = self._repository.create()

        redis_client.delete("dashboard:summary")

        return transaction

    def list_transactions(self):
        """List all transactions."""
        return self._repository.list()
