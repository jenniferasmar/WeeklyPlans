from Models.Day import Day
from datetime import datetime
from Models.Day import DayOfWeek


class Week:
    current_day = datetime.today()

    def __init__(self):
        self.this_week = [Day] * 7
        self.initialize_week()

    def initialize_week(self):
        for i in range(7):
            self.this_week[i].day_type = DayOfWeek(i+1)

