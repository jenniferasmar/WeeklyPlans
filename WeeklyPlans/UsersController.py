from flask import Flask, request
from Services.UsersService import UsersService

app = Flask(__name__)


@app.route("/createUser", methods=['POST'])
def create():
    data = request.data
    return UsersService.create_user(data)


if __name__ == "__main__":
    app.run(debug=True)
