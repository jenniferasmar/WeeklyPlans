import json
from types import SimpleNamespace
import MySQL_Properties
from Models.Users import Users
from flask_api import status
from flask import Response
from Models.CurrentParameters import CurrentParameters

current_parameter = CurrentParameters.instance()


def create_user(data):
    user_dict = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    user_db = MySQL_Properties.get_user_by_email(user_dict.email)
    if not user_db:
        user = Users(user_dict)
        MySQL_Properties.add_user(user)
        return Response("{User Registered}", status=200, mimetype='application/json')
    return Response("{User Exists}", status=203, mimetype='application/json')


def login_user(data):
    user = MySQL_Properties.get_user_by_email(data['email'])
    if not user:
        return Response("{User not found}", status=203, mimetype='application/json')
    if user[2] == data['password']:
        current_parameter.current_user = user
        return Response("{User logged in}", status=200, mimetype='application/json')
    if user[2] != data['password']:
        return Response("{Password do not match}", status=204, mimetype='application/json')
    return Response("{Error not handled}", status=501, mimetype='application/json')
