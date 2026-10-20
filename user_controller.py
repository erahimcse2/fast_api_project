
from fastapi import APIRouter, Depends, status
from schema import UserCreateRequest
from database import get_db
from service import UserService
from sqlalchemy.orm import Session
from repository import UserRepository

router = APIRouter(
    prefix="/user",
)


@router.post("/create")
def create_user(payload: UserCreateRequest, db: Session = Depends(get_db)):
    service = UserService(UserRepository())
    return service.create_user(db, payload)


@router.get("/list")
def get_all_user(db: Session = Depends(get_db)):
    service = UserService(UserRepository())
    return service.get_all_user(db)


@router.get("/{email}")
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    service = UserService(UserRepository())
    return service.get_user_by_email(db, email)


@router.delete("/{email}")
def delete_user_by_email(email: str, db: Session = Depends(get_db)):
    service = UserService(UserRepository())
    return service.delete_by_email(db, email)
