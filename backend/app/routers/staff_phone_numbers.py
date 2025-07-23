from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/staff_phone_numbers/", response_model=list[schemas.StaffPhoneNumberOut])
def read_staff_phone_numbers(db: Session = Depends(get_db)):
    return crud.get_staff_phone_numbers(db)