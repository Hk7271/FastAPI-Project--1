from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserPatch

def create_user (db: Session, user_in: UserCreate) -> User:
    user = User(
        name=user_in.name,
        email=user_in.email,
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db: Session) -> List[User]:
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def patch_user(db:Session, user: User, user_in: UserPatch) -> User:
    if user_in.name is not None:
        user.name = user_in.name
    if user_in.email is not None:
        user.email = user_in.email
    if user_in.is_active is not None:
        user.is_active = user_in.is_active

    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: User):
    if user is None:
        raise ValueError("User not found")
     
    db.delete(user)
    db.commit()
