from dataclasses import dataclass


@dataclass
class Todo:
    id: str
    title: str
    done: bool
