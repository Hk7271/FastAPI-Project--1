from pydantic import BaseModel
from datetime import datetime

class IrisBase(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisCreate(IrisBase):
    pass
class IrisUpdate(IrisBase):
    pass

class IrisResponse(IrisBase):
    id: int
    prediction: str

    class config:
        from_attributes = True