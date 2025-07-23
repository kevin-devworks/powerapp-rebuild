from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/location-addresses/", response_model=list[schemas.LocationAddressOut])
def read_location_addresses(db: Session = Depends(get_db)):
    return crud.get_location_addresses(db)