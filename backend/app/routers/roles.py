from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/roles/", response_model=list[schemas.RoleOut])
def read_roles(db: Session = Depends(get_db)):
    return crud.get_roles(db)