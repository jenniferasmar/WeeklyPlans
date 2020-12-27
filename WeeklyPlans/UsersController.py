from flask import Flask, request
from Services import UsersService
from flask_cors import CORS, cross_origin
app = Flask(__name__)


# requests name, password and email in body
@app.route("/createUser", methods=['POST'])
@cross_origin()
def create():
    data = request.data
    return UsersService.create_user(data)


# request email and password in body
@app.route("/login", methods=['POST'])
@cross_origin()
def login():
    data = request.json
    result = UsersService.login_user(data)
    return result


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=3000)

