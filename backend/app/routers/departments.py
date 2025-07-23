from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/departments/", response_model=list[schemas.DepartmentOut])
def read_departments(db: Session = Depends(get_db)):
    return crud.get_departments(db)