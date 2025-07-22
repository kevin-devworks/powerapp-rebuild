from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/providers/", response_model=list[schemas.ProviderOut])
def read_providers(db: Session = Depends(get_db)):
    return crud.get_providers(db)