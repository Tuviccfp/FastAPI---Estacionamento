from typing import Tuple

from sqlalchemy.dialects.sqlite import insert
from sqlmodel import Session, select

from user.user_table import UserTable

class UserRepository:
    def __init__(self, db_table: Session):
        self.db_table = db_table

    def create(self, user: UserTable) -> UserTable:
        self.db_table.add(user)
        self.db_table.commit()
        self.db_table.refresh(user)
        return user

    def get_by_email(self, user_email: str):
        result = self.db_table.exec(select(UserTable).where(
            user_email == UserTable.email
        ))
        return result.one_or_none()