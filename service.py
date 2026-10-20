
from sqlalchemy.orm import Session
from repository import UserRepository
from schema import UserCreateRequest
from user import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, db: Session, user_payload: UserCreateRequest):
        user = User(
            name=user_payload.name,
            email=user_payload.email,
            age=user_payload.age
        )
        return self.user_repository.create_user(db, user)

    def get_all_user(self, db: Session):
        return self.user_repository.get_all_user(db)

    def get_user_by_email(self, db: Session, email: str):
        return self.user_repository.get_user_by_email(db, email)

    def delete_by_email(self, db: Session, email: str):
        return self.user_repository.delete_by_email(db, email)
