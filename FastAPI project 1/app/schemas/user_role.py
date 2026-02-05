from pydantic import BaseModel

class UserRoleBase (BaseModel):
    user_id: int
    role_id: int

class UserRoleCreate(UserRoleBase):
    pass


class UserRoleDelete(UserRoleBase):
    pass

class UserRoleResponse(UserRoleBase):
    
    class Config:
        from_attributes = True