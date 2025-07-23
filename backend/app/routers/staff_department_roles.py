from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/staff_department_roles/", response_model=list[schemas.StaffDepartmentRoleOut])
def read_staff_department_roles(db: Session = Depends(get_db)):
    return crud.get_staff_department_roles(db)