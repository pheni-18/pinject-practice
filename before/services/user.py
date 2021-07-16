from repositories.user import IUserRepository


class UserService:
    def __init__(self, repo: IUserRepository):
        self._repo = repo

    def get_user_by_name(self, user_name: str):
        user = self._repo.get_user_by_name(user_name)
        return user
