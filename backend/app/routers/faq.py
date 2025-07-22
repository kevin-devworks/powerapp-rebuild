from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/faq/", response_model=list[schemas.FAQOut])
def read_faq(db: Session = Depends(get_db)):
    return crud.get_faq(db)