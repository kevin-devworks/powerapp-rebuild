from pydantic import BaseModel
from datetime import date

# ---- STAFF ----
class StaffOut(BaseModel):
    staff_id: int
    name: str
    email: str
    class Config:
        from_attributes = True

# ---- DEPARTMENT ----
class DepartmentOut(BaseModel):
    department_id: int
    department: str
    class Config:
        from_attributes = True

# ---- ROLE ----
class RoleOut(BaseModel):
    role_id: int
    role: str
    class Config:
        from_attributes = True

# ---- STAFF DEPARTMENT ROLE ----
class StaffDepartmentRoleOut(BaseModel):
    staff_department_roles_id: int
    staff_id: int
    department_id: int
    role_id: int
    class Config:
        from_attributes = True

# ---- PROVIDERS ----
class ProviderOut(BaseModel):
    provider_id: int
    staff_id: int
    specialty: str
    insurance_not_accepted: str | None = None
    patient_age_minimum: str
    patient_case_restrictions: str | None = None
    patient_conditions_will_not_see: str | None = None
    npi: str | None = None
    class Config:
        from_attributes = True

# ---- PROVIDER TEAM ----
class ProviderTeamOut(BaseModel):
    provider_team_id: int
    provider_id: int
    staff_id: int
    role_id: int
    phone_number_id: int | None = None
    class Config:
        from_attributes = True

# ---- PROVIDER ALERTS ----
class ProviderAlertOut(BaseModel):
    provider_id: int
    alert_message: str
    effective_date: date
    expiration_date: date

# ---- PHONE NUMBERS ----
class PhoneNumberOut(BaseModel):
    phone_number_id: int
    phone_number: str
    class Config:
        from_attributes = True

# ---- STAFF PHONE NUMBERS ----
class StaffPhoneNumberOut(BaseModel):
    phone_number_id: int
    staff_id: int
    class Config:
        from_attributes = True

class ClinicalDepartmentOut(BaseModel):
    department_id: int

class ClinicalDepartmentSubDepartmentOut(BaseModel):
    department_id: int
    role_id: int
    phone_number_id: int
    class Config:
        from_attributes = True

class BackOfficeDepartmentPhoneNumberOut(BaseModel):
    department_id: int
    phone_number_id: int
    class Config:
        from_attributes = True

class GroupDepartmentOut(BaseModel):
    group_department_id: int
    department_id: int
    class Config:
        from_attributes = True

# ---- LOCATIONS ----
class LocationAddressOut(BaseModel):
    address_name: str | None = None
    street_address_one: str
    street_address_two: str | None = None
    city: str
    state: str
    zip_code: str

class LocationTypeOut(BaseModel):
    location_type_id: int
    location_type: str
    class Config:
        from_attributes = True

class LocationPhoneNumberOut(BaseModel):
    location_id: int
    check_in_phone_number_id: int
    check_out_phone_number_id: int
    main_fax_number_id: int
    class Config:
        from_attributes = True

# ---- PROVIDER LOCATIONS ----
class ProviderLocationOut(BaseModel):
    provider_id: int 
    address_id: int
    location_type_id: int
    class Config:
        from_attributes = True

# ---- INSURANCES ----
class InsuranceOut(BaseModel):
    provider_id: int
    insurance_company: str
    plan_name: str | None = None

# ---- SELF PAY FEE SCHEDULE ----
class SelfPayFeeScheduleOut(BaseModel):
    procedure_code: str
    procedure_description: str | None = None
    fee_amount: int
    
class FAQOut(BaseModel):
    question: str
    answer: str
    class Config:
        from_attributes = True