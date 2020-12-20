from flask import Flask, request
from Services.UsersService import UsersService
from flask_cors import CORS, cross_origin
app = Flask(__name__)


@app.route("/createUser", methods=['POST'])
@cross_origin()
def create():
    data = request.data
    return UsersService.create_user(data)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=3000)

