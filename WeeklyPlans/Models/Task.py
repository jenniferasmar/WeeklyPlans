import enum


class TaskType(enum.Enum):
    ToDo = 1
    PG = 2
    Done = 3


class Task:
    def __init__(self, task_type: TaskType):
        self.type = task_type

