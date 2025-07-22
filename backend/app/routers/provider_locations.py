from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/provider-locations/", response_model=list[schemas.ProviderLocationOut])
def read_provider_locations(db: Session = Depends(get_db)):
    return crud.get_provider_location(db)