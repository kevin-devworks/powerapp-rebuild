from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/back-office-department-phone-number/", response_model=list[schemas.BackOfficeDepartmentPhoneNumberOut])
def read_back_office_department_phone_numbers(db: Session = Depends(get_db)):
    return crud.get_back_office_department_phone_numbers(db)