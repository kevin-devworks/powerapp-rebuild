from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine
from .dependencies import get_db
from app.routers import back_office_department_phone_numbers, clinical_departments_sub_departments, clinical_departments, departments, faq, insurances, location_addresses, location_phone_numbers, location_types, phone_numbers, provider_alerts, provider_locations, provider_teams, providers, roles, selfpay_fee_schedule, staff_department_roles, staff_phone_numbers, staff

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running!"}

app.include_router(back_office_department_phone_numbers.router)
app.include_router(clinical_departments_sub_departments.router)
app.include_router(clinical_departments.router)
app.include_router(departments.router)
app.include_router(faq.router)
app.include_router(insurances.router)
app.include_router(location_addresses.router)
app.include_router(location_phone_numbers.router)
app.include_router(location_types.router)
app.include_router(phone_numbers.router)
app.include_router(provider_alerts.router)
app.include_router(provider_locations.router)
app.include_router(provider_teams.router)
app.include_router(providers.router)
app.include_router(roles.router)
app.include_router(selfpay_fee_schedule.router)
app.include_router(staff_department_roles.router)
app.include_router(staff_phone_numbers.router)
app.include_router(staff.router)


"""

@app.get("/providers/", response_model=list[schemas.ProviderOut])
def read_providers(db: Session = Depends(get_db)):
    return crud.get_providers(db)

@app.get("/provider-alerts/", response_model=list[schemas.ProviderAlertOut])
def read_provider_alerts(db: Session = Depends(get_db)):
    return crud.get_provider_alerts(db)

@app.get("/staff/", response_model=list[schemas.StaffOut])
def read_staff(db: Session = Depends(get_db)):
    return crud.get_staff(db)

@app.get("/phone-numbers/", response_model=list[schemas.PhoneNumberOut])
def read_phone_numbers(db: Session = Depends(get_db)):
    return crud.get_phone_numbers(db)

@app.get("/provider-locations/", response_model=list[schemas.ProviderLocationOut])
def read_locations(db: Session = Depends(get_db)):
    return crud.get_locations(db)

@app.get("/insurances/", response_model=list[schemas.InsuranceOut])
def read_insurances(db: Session = Depends(get_db)):
    return crud.get_insurances(db)

@app.get("/selfpay-fee-schedule/", response_model=list[schemas.SelfPayFeeScheduleOut])
def read_selfpay_fees(db: Session = Depends(get_db)):
    return crud.get_selfpay_fees(db)

@app.get("/faq/", response_model=list[schemas.FAQOut])
def read_faq(db: Session = Depends(get_db)):
    return crud.get_faq(db)

"""