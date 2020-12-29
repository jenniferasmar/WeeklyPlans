import enum
from Models.Day import Day


class TaskType(enum.Enum):
    ToDo = 1
    PG = 2
    Done = 3


class Task:
    def __init__(self, task_name: str, task_type: TaskType, task_duration: float, task_days: list[Day]):
        self.title = task_name
        self.type = task_type
        self.duration = task_duration
        self.which_day = task_days



