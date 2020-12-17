import json
from types import SimpleNamespace


class UsersService:

    def create_user(data):
        user_dict = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        user = Users(user_dict)
        return user.name