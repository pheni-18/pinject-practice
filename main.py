from icecream import ic
from infrastructure.fake_db import FakeDB
from infrastructure.user import UserRepository
from services.user import UserService


def main():
    fake_db = FakeDB()
    user_repo = UserRepository(fake_db)
    user_service = UserService(user_repo)
    user1 = user_service.get_user_by_name('John')

    ic(user1.id, user1.name, user1.age)

    for todo in user1.todos:
        ic(todo.id, todo.title)


if __name__ == '__main__':
    main()
