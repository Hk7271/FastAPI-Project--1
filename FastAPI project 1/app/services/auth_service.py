from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import LoginRequest
from app.core.security import verify_password, create_access_token


def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email ==email).first()

    if not user:
        return None
    
    if not verify_password(password, user.password_hash):
        return None
    token = create_access_token(
        data= {"sub": str(user.id)}
    )

    return token