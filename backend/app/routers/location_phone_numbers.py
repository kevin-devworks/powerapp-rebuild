from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/location-phone-numbers/", response_model=list[schemas.LocationPhoneNumberOut])
def read_location_phone_numbers(db: Session = Depends(get_db)):
    return crud.get_location_addresses(db)