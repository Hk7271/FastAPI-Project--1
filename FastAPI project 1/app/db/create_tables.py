"""
Work of this file is handed over to alembic 

from app.db.session import engine, Base

from app.models.role import Role
from app.models.prediction import IrisPrediction
from app.models.user import User
from app.models.user_role import UserRole


Base.metadata.create_all(bind=engine)

print("All tables created successfully")

"""