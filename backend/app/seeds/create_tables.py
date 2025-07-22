from app.database import Base, engine
import app.models

print("Creating all tables based on models.py ...")
Base.metadata.create_all(bind=engine)
print("✅ All tables created successfully!")
