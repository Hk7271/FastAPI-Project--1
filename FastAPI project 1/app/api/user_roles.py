from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from typing import List
from app.schemas.user_role import UserRoleCreate, UserRoleDelete, UserRoleResponse
from app.services import user_role_service

router = APIRouter(prefix="/user-roles",tags=["User Roles"])

@router.post("/",response_model= UserRoleResponse, status_code=status.HTTP_201_CREATED)
def create_user_role (
    user_role_in: UserRoleCreate,
    db: Session = Depends(get_db)
):
    try:
        return user_role_service.create_user_role(db, user_role_in)
    except ValueError:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST
        )
    
@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_role (user_role_in: UserRoleDelete, db: Session = Depends(get_db)):
    try:
        user_role_service.delete_user_role(db,user_role_in)
    except ValueError:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND
        )
