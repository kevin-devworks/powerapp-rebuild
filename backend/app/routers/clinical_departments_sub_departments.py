from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/clinical-departments-sub-departments/", response_model=list[schemas.ClinicalDepartmentSubDepartmentOut])
def read_clinical_departments_sub_departments(db: Session = Depends(get_db)):
    return crud.get_clinical_departments_sub_departments(db)