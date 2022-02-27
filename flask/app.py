from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import hmac

from classes.user import User

app = Flask(__name__)
app.secret_key = 'secret'

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and hmac.compare_digest(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

jwt = JWT(app, authenticate, identity)

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'



class HelloWorld(Resource):
    @jwt_required()
    def get(self):
        return {'hello': 'world'}

api = Api(app)

api.add_resource(HelloWorld, '/hello')



if __name__ == '__main__':
    app.run()
