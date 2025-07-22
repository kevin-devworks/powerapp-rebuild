from pathlib import Path
import pandas as pd
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

# Adjust according to your csv directory
CSV_FOLDER = Path(__file__).parent.parent / "csv_data"

def get_csv_path(filename: str) -> Path:
    return CSV_FOLDER / filename

# Map models, schemas, and CSV filenames
TABLE_CONFIG = [
    {"model": models.ClinicalDepartment, "schema": schemas.ClinicalDepartmentOut, "csv": "clinical_departments.csv"},
    {"model": models.ClinicalDepartmentSubDepartment, "schema": schemas.ClinicalDepartmentSubDepartmentOut, "csv": "clinical_departments_sub_departments.csv"},
    {"model": models.Department, "schema": schemas.DepartmentOut, "csv": "departments.csv"},
    {"model": models.LocationAddress, "schema": schemas.LocationAddressOut, "csv": "location_addresses.csv"},
    {"model": models.LocationPhoneNumber, "schema": schemas.LocationPhoneNumberOut, "csv": "location_phone_numbers.csv"},
    {"model": models.LocationType, "schema": schemas.LocationTypeOut, "csv": "location_types.csv"},
    {"model": models.PhoneNumber, "schema": schemas.PhoneNumberOut, "csv": "phone_numbers.csv"},
    {"model": models.ProviderLocation, "schema": schemas.ProviderLocationOut, "csv": "provider_locations.csv"},
    {"model": models.ProviderTeam, "schema": schemas.ProviderTeamOut, "csv": "provider_teams.csv"},
    {"model": models.Provider, "schema": schemas.ProviderOut, "csv": "providers.csv"},
    {"model": models.Role, "schema": schemas.RoleOut, "csv": "roles.csv"},
    {"model": models.StaffDepartmentRole, "schema": schemas.StaffDepartmentRoleOut, "csv": "staff_department_roles.csv"},
    {"model": models.StaffPhoneNumber, "schema": schemas.StaffPhoneNumberOut, "csv": "staff_phone_numbers.csv"},
    {"model": models.Staff, "schema": schemas.StaffOut, "csv": "staff.csv"},
]

def seed_table(session: Session, model, schema, csv_file: Path):
    print(f"Seeding {model.__name__} from {csv_file}")
    df = pd.read_csv(csv_file)
    inserted = 0

    for record in df.to_dict(orient="records"):
        try:
            validated = schema.model_validate(record)
            db_obj = model(**validated.model_dump())
            session.add(db_obj)
            inserted += 1
        except Exception as e:
            print(f"Skipping row due to error: {e}\nRow: {record}")

    session.commit()
    print(f"Inserted {inserted} rows into {model.__tablename__}")

def main():
    session = SessionLocal()
    try:
        for config in TABLE_CONFIG:
            csv_path = get_csv_path(config["csv"])
            seed_table(session, config["model"], config["schema"], csv_path)
    finally:
        session.close()

if __name__ == "__main__":
    main()
