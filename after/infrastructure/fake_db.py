import uuid


class FakeDB:
    _user_id1 = uuid.uuid4()
    _user_id2 = uuid.uuid4()
    _user_id3 = uuid.uuid4()

    _users = [
        {
            'id': _user_id1,
            'name': 'John',
            'age': 20,
        },
        {
            'id': _user_id2,
            'name': 'Bob',
            'age': 25,
        },
        {
            'id': _user_id3,
            'name': 'Rebecca',
            'age': 22,
        },
    ]

    _todos = [
        {
            'id': uuid.uuid4(),
            'title': 'Buy a milk',
            'done': False,
            'user_id': _user_id1
        },
        {
            'id': uuid.uuid4(),
            'title': 'Play the piano',
            'done': True,
            'user_id': _user_id1
        },
        {
            'id': uuid.uuid4(),
            'title': 'Running',
            'done': False,
            'user_id': _user_id2
        },
    ]

    @classmethod
    def find_user_by_name(cls, user_name: str):
        user = None
        for _user in cls._users:
            if user_name == _user['name']:
                user = _user

        return user

    @classmethod
    def find_todos(cls, user_id: str):
        todos = []
        for _todo in cls._todos:
            if user_id == _todo['user_id']:
                todos.append(_todo)

        return todos
