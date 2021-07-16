from .todo import Todo
from dataclasses import dataclass
from typing import List


@dataclass
class User:
    id: str
    name: str
    age: int
    todos: List[Todo]
