from .fake_db import FakeDB
from models.todo import Todo
from models.user import User
from repositories.user import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, db: FakeDB):
        self._db = db

    def get_user_by_name(self, user_name: str):
        user = self._db.find_user_by_name(user_name)
        todos = self._db.find_todos(user['id'])

        return User(
            id=str(user['id']),
            name=user['name'],
            age=user['age'],
            todos=[
                Todo(
                    id=str(todo['id']),
                    title=todo['title'],
                    done=todo['done'],
                )
                for todo in todos
            ],
        )
