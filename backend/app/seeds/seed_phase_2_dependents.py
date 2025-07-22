# ✅ Phase 2: Dependent Data Seed Script
# File: app/seeds/seed_phase_2_dependents.py

from pathlib import Path
import pandas as pd
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

CSV_FOLDER = Path(__file__).parent.parent / "csv_data"

def get_csv_path(filename: str) -> Path:
    return CSV_FOLDER / filename

def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle null values and type coercion before validation.
    Converts NaN to None and ensures zip_code is a string if applicable.
    """
    df = df.where(pd.notnull(df), None)
    if "zip_code" in df.columns:
        df["zip_code"] = df["zip_code"].astype(str)
    return df

TABLE_CONFIG = [
    {"model": models.ClinicalDepartment, "schema": schemas.ClinicalDepartmentOut, "csv": "clinical_departments.csv"},
    {"model": models.ClinicalDepartmentSubDepartment, "schema": schemas.ClinicalDepartmentSubDepartmentOut, "csv": "clinical_departments_sub_departments.csv"},
    {"model": models.StaffDepartmentRole, "schema": schemas.StaffDepartmentRoleOut, "csv": "staff_department_roles.csv"},
    {"model": models.StaffPhoneNumber, "schema": schemas.StaffPhoneNumberOut, "csv": "staff_phone_numbers.csv"},
    {"model": models.Provider, "schema": schemas.ProviderOut, "csv": "providers.csv"},
    {"model": models.ProviderTeam, "schema": schemas.ProviderTeamOut, "csv": "provider_teams.csv"},
    {"model": models.ProviderLocation, "schema": schemas.ProviderLocationOut, "csv": "provider_locations.csv"},
]

def seed_table(session: Session, model, schema, csv_file: Path):
    print(f"Seeding {model.__name__} from {csv_file}")
    df = pd.read_csv(csv_file)
    df = preprocess_dataframe(df)
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