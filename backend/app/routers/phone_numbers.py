from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/phone-numbers/", response_model=list[schemas.PhoneNumberOut])
def read_phone_numbers(db: Session = Depends(get_db)):
    return crud.get_phone_numbers(db)