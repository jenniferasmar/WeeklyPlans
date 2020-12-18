import json
from types import SimpleNamespace
import MySQL_Properties
from Models.Users import Users


class UsersService:

    def create_user(data):
        user_dict = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        user = Users(user_dict)
        MySQL_Properties.add_User(user)
        return user.name
