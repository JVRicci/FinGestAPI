from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.databse import get_db
from src.schemas.transaction import TransactionCreate, TransactionResponse
from src.services.transaction_service import TransactionService

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=TransactionResponse)
def create_transaction(
    data: TransactionCreate,
    db: Session = Depends(get_db),
):
    """Create a new transaction."""
    service = TransactionService(db)
    return service.create_transaction(data)


@router.get("/", response_model=list[TransactionResponse])
def list_transactions(db: Session = Depends(get_db)):
    """List all transactions."""
    service = TransactionService(db)
    return service.list_transactions()
