from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/provider-alerts/", response_model=list[schemas.ProviderAlertOut])
def read_provider_alerts(db: Session = Depends(get_db)):
    return crud.get_provider_alerts(db)