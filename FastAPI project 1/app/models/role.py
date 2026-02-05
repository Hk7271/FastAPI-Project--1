from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.db.session import Base
from sqlalchemy.orm import relationship

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key= True)
    role_name = Column( String, unique=True, nullable= False)
    is_active = Column(Boolean, default= True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    users = relationship(
        "User",
        secondary="user_roles",
        back_populates="roles"
    )