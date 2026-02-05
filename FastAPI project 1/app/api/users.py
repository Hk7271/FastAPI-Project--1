from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.user import(
    UserCreate,
    UserUpdate,
    UserPatch,
    UserResponse,
    UserCreateResponseWithToken
)
from app.services import user_service
from app.core.dependencies import get_current_user , require_roles
from app.models.user import User

router = APIRouter()

@router.post(
    "/",
    response_model= UserCreateResponseWithToken,
    status_code= status.HTTP_201_CREATED
)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db)
):
    return user_service.create_user(db, user_in)

@router.get(
    "/",
    response_model=List[UserResponse]

)
def get_users(db: Session = Depends(get_db),
              current_user: User = Depends(require_roles("admin","super_admin"))):
    return user_service.get_users(db)

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles("user","admin","super_admin"))
):
   if(
       "user" in {r.role_name for r in current_user.roles}
       and current_user.id != user_id
   ):
       raise HTTPException(
           status_code= status.HTTP_403_FORBIDDEN,
           detail="Users can only access their own data"

       )
   return user_service.get_user(db, user_id)
@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    user_in: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles("super_admin"))
):
    try:
        return user_service.update_user(db, user_id, user_in) 

    except ValueError:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
@router.patch(
    "/{user_id}",
    response_model=UserResponse

)
def patch_user(
    user_id: int,
    user_in: UserPatch,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles("super_admin"))
):
    try:
        return user_service.patch_user(db, user_id, user_in)
    except ValueError:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )  

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles("super_admin"))
):
    try:
        user_service.delete_user(db, user_id)
    except ValueError:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

