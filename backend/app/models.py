from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship
from .database import Base


# ---------------- Feature A ---------------- #
class Staff(Base):
    __tablename__ = "staff"
    staff_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    department_roles = relationship("StaffDepartmentRole", back_populates="staff")
    provider = relationship("Provider", back_populates="staff")
    phone_number_id = relationship("StaffPhoneNumber")

class Department(Base):
    __tablename__ = "departments"
    department_id = Column(Integer, primary_key=True, nullable=False, index=True)
    department = Column(String, nullable=False)

    department_roles = relationship("StaffDepartmentRole", back_populates="department")

class Role(Base):
    __tablename__ = "roles"
    role_id = Column(Integer, primary_key=True, nullable=False, index=True)
    role = Column(String, nullable=False)

    department_roles = relationship("StaffDepartmentRole", back_populates="role")

class StaffDepartmentRole(Base):
    __tablename__ = "staff_department_roles"
    staff_department_roles_id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False, index=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False, index=True)
    role_id = Column(Integer, ForeignKey('roles.role_id'), nullable=False, index=True)

    staff = relationship("Staff", back_populates="department_roles")
    department = relationship("Department", back_populates="department_roles")
    role = relationship("Role", back_populates="department_roles")

class Provider(Base):
    __tablename__="providers"
    provider_id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False)
    #team_id = Column(Integer, ForeignKey('provider_teams.provider_team_id'), nullable=False, index=True)
    specialty = Column(String)
    insurance_not_accepted = Column(String)
    patient_age_minimum = Column(String)
    patient_case_restrictions = Column(String)
    patient_conditions_will_not_see = Column(String)
    npi = Column(String)

    staff = relationship("Staff", back_populates="provider")
    '''team = relationship("ProviderTeam", back_populates="provider")'''

class ProviderTeam(Base):
    __tablename__ = "provider_teams"
    provider_team_id = Column(Integer, primary_key=True, index=True)
    provider_id = Column(Integer, ForeignKey('providers.provider_id'), nullable=False, index=True)
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.role_id'), nullable=False)
    phone_number_id = Column(Integer, ForeignKey('phone_numbers.phone_number_id'), nullable=True)

class PhoneNumber(Base):
    __tablename__ = "phone_numbers"
    phone_number_id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, nullable=False)

class StaffPhoneNumber(Base):
    __tablename__ = "staff_phone_numbers"
    staff_phone_number_id = Column(Integer, primary_key=True, index=True)
    phone_number_id = Column(Integer, ForeignKey('phone_numbers.phone_number_id'), nullable=False, index=True)
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False, index=True)

class ClinicalDepartment(Base):
    __tablename__ = "clinical_departments"
    clinical_department_id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False)

class ClinicalDepartmentSubDepartment(Base):
    __tablename__ = "clinical_department_sub_departments"
    clinical_department_sub_department_id = Column(Integer, primary_key=True, index=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.role_id'), nullable=False)
    phone_number_id = Column(Integer, ForeignKey('phone_numbers.phone_number_id'), nullable=False)

class BackOfficeDepartmentPhoneNumber(Base):
    __tablename__ = "back_office_department_phone_numbers"
    back_office_department_phone_number_id = Column(Integer, primary_key=True, index=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False, index=True)
    phone_number_id = Column(Integer, ForeignKey('phone_numbers.phone_number_id'), nullable=False)

class GroupDepartment(Base):
    __tablename__ = "group_departments"
    group_department_id = Column(Integer, primary_key=True, index=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False)

class LocationAddress(Base):
    __tablename__ = "location_addresses"
    address_id = Column(Integer, primary_key=True, index=True)
    address_name = Column(String, nullable=True)
    street_address_one = Column(String, nullable=False)
    street_address_two = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)

class LocationType(Base):
    __tablename__ = "location_types"
    location_type_id = Column(Integer, primary_key=True, index=True)
    location_type = Column(String, nullable=False)

class LocationPhoneNumber(Base):
    __tablename__ = "location_phone_numbers"
    location_phone_number_id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey('location_addresses.address_id'), nullable=False)
    check_in_phone_number_id = Column(String, nullable=True)
    check_out_phone_number_id = Column(String, nullable=True)
    main_fax_number_id = Column(String, nullable=False)

class ProviderLocation(Base):
    __tablename__ = "provider_locations"
    provider_location_id = Column(Integer, primary_key=True, index=True)
    provider_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False, index=True)
    address_id = Column(Integer, ForeignKey('location_addresses.address_id'), nullable=False)
    location_type_id = Column(Integer, ForeignKey('location_types.location_type_id'), nullable=False)

# ---------------- Feature B ---------------- #
'''
class ProviderAlert(Base):
    __tablename__ = "provider_alerts"
    alert_id = Column(Integer, primary_key=True, index=True)
    provider_id = Column(Integer, ForeignKey('providers.provider_id'), nullable=False)
    alert_message = Column(String, nullable=False)
    effective_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)
'''

# ---------------- Feature C ---------------- #
'''
class Insurance(Base):
    __tablename__ = "insurances"
    insurance_id = Column(Integer, primary_key=True, index=True)
    provider_id = Column(Integer, ForeignKey("providers.provider_id"), nullable=False)
    insurance_company = Column(String, nullable=False)
    plan_name = Column(String)
    referral = Column(Boolean, nullable=False)
'''

# ---------------- Feature D ---------------- #
'''
class FAQ(Base):
    __tablename__ = "faq"
    faq_id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
'''

# ---------------- Feature E ---------------- #
'''
class SelfPayFeeSchedule(Base):
    __tablename__ = "self_pay_fee_schedule"
    procedure_code_id = Column(Integer, primary_key=True, index=True)
    procedure_code = Column(String, nullable=False)
    procedure_description = Column(String)
    fee_amount = Column(Integer)
'''