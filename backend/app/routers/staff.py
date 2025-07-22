from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/staff/", response_model=list[schemas.StaffOut])
def read_staff(db: Session = Depends(get_db)):
    return crud.get_staff(db)