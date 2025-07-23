from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/location-types/", response_model=list[schemas.LocationTypeOut])
def read_location_types(db: Session = Depends(get_db)):
    return crud.get_location_types(db)