from repositories.user import IUserRepository

import pinject


class UserService:
    @pinject.inject()
    def __init__(self, user_repo: IUserRepository):
        self._user_repo = user_repo

    def get_user_by_name(self, user_name: str):
        user = self._user_repo.get_user_by_name(user_name)
        return user
