from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/insurances/", response_model=list[schemas.InsuranceOut])
def read_insurances(db: Session = Depends(get_db)):
    return crud.get_insurances(db)