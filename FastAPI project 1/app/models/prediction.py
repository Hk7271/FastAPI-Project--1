from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from app.db.session import Base


class IrisPrediction(Base):
    __tablename__ = "iris_predictions"

    id = Column(Integer, primary_key=True, index=True)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)
    prediction = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
