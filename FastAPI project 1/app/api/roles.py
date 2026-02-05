from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.db.session import get_db
from app.schemas.role import(
    RoleCreate,
    RoleUpdate,
    RoleResponse
)
from app.services import role_service

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post(
    "/",
    response_model= RoleResponse,
    status_code= status.HTTP_201_CREATED
)
def create_role(
    role_in: RoleCreate,
    db: Session = Depends(get_db)
):
    return role_service.create_role(db, role_in)

@router.get(
    "/",
    response_model=List[RoleResponse]
)
def get_roles(
    db:Session = Depends(get_db)
):
    return role_service.get_roles(db)

@router.get(
    "/{role_id}",
    response_model= RoleResponse    
)
def get_role(
    role_id: int,
    db:Session = Depends(get_db)
):
    return role_service.get_role(db, role_id)

@router.put(
    "/{role_id}",
    response_model= RoleResponse
)
def update_role(
    role_id: int,
    role_in: RoleUpdate,
    db: Session = Depends(get_db)
):
    return role_service.update_role(db, role_id, role_in)

@router.delete(
    "/{role_id}",
    status_code= status.HTTP_204_NO_CONTENT

)
def delete_role(
    role_id: int,
    db: Session = Depends(get_db)
):
    return role_service.delete_role(db, role_id)
