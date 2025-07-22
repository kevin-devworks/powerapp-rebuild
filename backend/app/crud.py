from sqlalchemy.orm import Session
from . import models

# Read-only queries only

def get_providers(db: Session):
    return db.query(models.Provider).all()

def get_provider_alerts(db: Session):
    return db.query(models.ProviderAlert).all()

def get_staff(db: Session):
    return db.query(models.Staff).all()

def get_phone_numbers(db: Session):
    return db.query(models.PhoneNumber).all()

def get_provider_location(db: Session):
    return db.query(models.ProviderLocation).all()

def get_insurances(db: Session):
    return db.query(models.Insurance).all()

def get_selfpay_fee_schedule(db: Session):
    return db.query(models.SelfPayFeeSchedule).all()

def get_faq(db: Session):
    return db.query(models.FAQ).all()

def get_back_office_department_phone_numbers(db: Session):
    return db.query(models.BackOfficeDepartmentPhoneNumber).all()

def get_clinical_departments_sub_departments(db: Session):
    return db.query(models.ClinicalDepartmentSubDepartment).all()

def get_clinical_departments(db: Session):
    return db.query(models.ClinicalDepartment).all()

