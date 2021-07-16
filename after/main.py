from icecream import ic
from services.binding_specs import ServiceBindingSpec
from services.user import UserService

import pinject


def main():
    obj_graph = pinject.new_object_graph(
        binding_specs=[
            ServiceBindingSpec(),
        ],
        only_use_explicit_bindings=True,
    )
    user_service = obj_graph.provide(UserService)
    user1 = user_service.get_user_by_name('John')

    ic(user1.id, user1.name, user1.age)

    for todo in user1.todos:
        ic(todo.id, todo.title)


if __name__ == '__main__':
    main()
