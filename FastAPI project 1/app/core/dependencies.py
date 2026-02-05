from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.db.session import get_db
from app.models.user import User
from app.core.security import Secret_key, Algorithm

security = HTTPBearer()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
):
   try: 
      payload = jwt.decode(
         credentials.credentials,
         Secret_key,
         algorithms=[Algorithm]
      )

      user_id: str | None = payload.get("sub")
      if user_id is None:
         raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
         )
    
   except JWTError:
      raise HTTPException(
         status_code= status.HTTP_401_UNAUTHORIZED,
         detail="Invalid or Expired Token"
      )
    
   user = db.query(User).filter(User.id == int(user_id)).first()
   
   if user is None:
      raise HTTPException(
         status_code=status.HTTP_401_UNAUTHORIZED,
         detail="No user Found"
      )
   
   return user

def require_roles(*allowed_roles: str):
   def role_checker(current_user: User = Depends(get_current_user)):
      user_roles = { role.role_name for role in current_user.roles}

      if not user_roles.intersection(allowed_roles):
         raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission Denied"
         )
      
      return current_user
   return role_checker