from datetime import datetime, date
from Models.Day import DayOfWeek
from Models.Users import Users


class CurrentParameters:
    _instance = None

    def __init__(self):
        if CurrentParameters._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            now = datetime.now()
            today = date.today()

            self.current_user = None
            self.current_date = today.strftime("%d/%m/%Y")
            self.current_time = now.strftime("%H:%M:%S")
            week_day = datetime.today().weekday()
            self.current_day = DayOfWeek(week_day + 1)
            CurrentParameters._instance = self

    @staticmethod
    def instance():
        if CurrentParameters._instance is None:
            print('Creating new instance')
            _instance = CurrentParameters()
        return CurrentParameters._instance
