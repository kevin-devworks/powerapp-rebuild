from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/provider-teams", response_model=list[schemas.ProviderTeamOut])
def read_provider_teams(db: Session = Depends(get_db)):
    return crud.get_location_addresses(db)