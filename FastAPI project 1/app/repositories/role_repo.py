from sqlalchemy.orm import Session
from typing import List
from app.models.role import Role
from app.schemas.role import RoleCreate, RoleUpdate

def create_role(db: Session, role_in: RoleCreate) -> Role:
    role = Role(
        role_name= role_in.role_name,
        is_active=True
    )
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def get_roles(db:Session) -> List[Role]:
    return db.query(Role).all()

def get_role_by_id(db:Session, role_id: int):
    return db.query(Role).filter(Role.id==role_id).first()

def update_role(db: Session,role):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def delete_role(db:Session, role: Role):
    if role is None:
        raise ValueError("Not Found")
    db.delete(role)
    db.commit()