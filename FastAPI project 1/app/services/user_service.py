from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.core.security import (hash_password , create_access_token, Access_token_expire_hours)
from typing import List
from app.schemas.user import UserCreate, UserUpdate, UserPatch
from app.repositories import user_repo
from app.models.user import User
from app.models.user_role import UserRole
from app.models.role import Role

def create_user(db: Session, user_in: UserCreate) -> User:
    try: 
        user = User(
            name= user_in.name,
            email = user_in.email,
            password_hash = hash_password(user_in.password),
            is_active = True
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        default_role = (
            db.query(Role).filter(Role.role_name=="user").first()
        )

        if not default_role:
            raise ValueError("Default Role 'user' not found !! ")
        
        user_role = UserRole(
            user_id = user.id,
            role_id = default_role.id
        )

        db.add(user_role)
        db.commit()

        access_token = create_access_token(
            data={"sub": str(user.id)}
        )

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "is_active": user.is_active,
            "created_at": user.created_at,
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": Access_token_expire_hours * 60 * 60 
        }
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists")
    

def get_users(db: Session) -> List[User]:
    return user_repo.get_users(db)

def get_user(db: Session, user_id: int):
    user = user_repo.get_user_by_id(db, user_id)

    if user is None:
        raise ValueError("User not found")

    return user

    
def update_user(db: Session, user_id: int, user_in: UserUpdate):
    user = user_repo.get_user_by_id(db, user_id)

    if user is None:
        raise ValueError("User not found")

    user.name = user_in.name
    user.email = user_in.email

    return user_repo.update_user(db, user)


def patch_user(db: Session, user_id: int, user_in: UserPatch) -> User:
    user = get_user(db, user_id)
    return user_repo.patch_user(db, user, user_in)

def delete_user(db: Session, user_id: int):
    user = user_repo.get_user_by_id(db, user_id)

    if user is None:
        raise ValueError("User not found")
    
    map_exists = db.query(UserRole).filter(
        UserRole.user_id == user_id
    ).first()

    if map_exists:
        raise ValueError(
            "User cannot be deleted as a role is assigned"
        )

    user_repo.delete_user(db, user)
