import enum
from Models.Task import Task


class DayOfWeek(enum.Enum):
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Sun = 7


class Day:

    def __init__(self, day_type: DayOfWeek, tasks=None):
        self.dayType = day_type
        if tasks is None:
            self.tasks = list[Task]
        else:
            self.tasks = tasks

    def add_task(self, new_task: Task):
        self.tasks.append(new_task)
