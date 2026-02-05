from sqlalchemy.orm import Session
from typing import List
from app.models.role import Role
from app.schemas.role import RoleCreate, RoleUpdate
from app.repositories import role_repo
from app.models.user_role import UserRole

def create_role (db:Session, role_in: RoleCreate) -> Role:
    return role_repo.create_role(db, role_in)

def get_roles (db:Session) -> List[Role]:
    return role_repo.get_roles(db)

def get_role (db:Session, role_id: int):
    role = role_repo.get_role_by_id(db, role_id)

    if role is None:
        raise ValueError("Not Found")
    
    return role

def update_role (db:Session, role_id: int, role_in: RoleUpdate):
    role = role_repo.get_role_by_id(db, role_id)

    if role is None:
        raise ValueError("Not Found")
    return role_repo.update_role(db, role)

def delete_role (db: Session, role_id: int):
    role = role_repo.get_role_by_id(db,role_id)

    if role is None:
        raise ValueError("Not Found")
    
    if role.role_name.strip().lower()=="super_admin":
        raise ValueError(
            "The super_admin role can never be deleted"
        )
    
    map_exists = db.query(UserRole).filter(
        UserRole.role_id == role_id
    ).first()

    if map_exists:
        raise ValueError(
            "Role cannot be deleted because it is assigned"
        )
    return role_repo.delete_role(db, role)
    
