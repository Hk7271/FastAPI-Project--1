from pydantic import BaseModel
from datetime import datetime

class RoleBase(BaseModel):
    role_name: str
class RoleCreate(RoleBase):
    pass 
class RoleUpdate(RoleBase):
    is_active: bool
class RoleResponse(RoleBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class config:
        from_attributes : True