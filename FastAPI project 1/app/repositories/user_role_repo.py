from sqlalchemy.orm import Session
from typing import List
from app.models.user_role import UserRole
from app.schemas.user_role import UserRoleCreate, UserRoleDelete

def create_user_role(db: Session, user_role_in: UserRoleCreate) -> UserRole:
    user_role = UserRole(
        user_id = user_role_in.user_id,
        role_id = user_role_in.role_id
    )
    db.add(user_role)
    db.commit()
    return user_role

def delete_user_role(db: Session, user_role_in: UserRoleDelete):
    map = db.query(UserRole).filter(
        UserRole.user_id == user_role_in.user_id,
        UserRole.role_id == user_role_in.role_id
    ).first()

    db.delete(map)
    db.commit()