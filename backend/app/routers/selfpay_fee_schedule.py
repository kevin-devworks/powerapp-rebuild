from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter()

@router.get("/selfpay-fee-schedule/", response_model=list[schemas.SelfPayFeeScheduleOut])
def read_selfpay_fee_schedule(db: Session = Depends(get_db)):
    return crud.get_selfpay_fee_schedule(db)