from user.user_repository import UserRepository
from user.user_table import UserTable


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_by_email(self, email: str) -> bool | None:
        return self.user_repo.get_by_email(email)

    def create_new_user(self, user: UserTable):
        get_email = self.get_by_email(user.email)
        print(get_email)
        if get_email:
            raise Exception("Email already exists")
        return self.user_repo.create(user)