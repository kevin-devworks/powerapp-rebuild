from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/clinical-departments/", response_model=list[schemas.ClinicalDepartmentOut])
def read_clinical_departments(db: Session = Depends(get_db)):
    return crud.get_clinical_departments(db)