from abc import ABCMeta, abstractmethod


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_user_by_name(self, user_name: str):
        pass
