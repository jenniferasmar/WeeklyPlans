import enum


class TaskType(enum.Enum):
    ToDo = 1
    PG = 2
    Done = 3


class Task:
    def __init__(self, task_name: str, task_type: TaskType, task_start: float, task_duration: float):
        self.title = task_name
        self.type = task_type
        self.start_time = task_start
        self.duration = task_duration
        self.repeat = False

    def set_repeat(self, boolean: bool):
        self.repeat = boolean



