from sqlalchemy.orm import Session
from typing import List
from app.models.user_role import UserRole
from app.schemas.user_role import UserRoleCreate, UserRoleDelete
from app.repositories import user_role_repo


def create_user_role (db: Session, user_role_in: UserRoleCreate):
    exists_role = db.query(UserRole).filter(
        UserRole.role_id == user_role_in.role_id
    ).first()

    if exists_role:
        raise ValueError(
            "Role already Assigned"
        )
    
    return user_role_repo.create_user_role(db,user_role_in)

def delete_user_role (db: Session, user_role_in: UserRoleDelete):
    return user_role_repo.delete_user_role(db, user_role_in)
