import json
from types import SimpleNamespace
import MySQL_Properties
from Models.Users import Users
from flask_api import status


def create_user(data):
    user_dict = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    user = Users(user_dict)
    MySQL_Properties.add_user(user)
    return user.name


def login_user(data):
    user = MySQL_Properties.get_user_by_email(data['email'])
    if not user:
        return status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
    if user[2] == data['password']:
        return status.HTTP_200_OK
    if user[2] != data['password']:
        return status.HTTP_204_NO_CONTENT
    return status.HTTP_501_NOT_IMPLEMENTED
