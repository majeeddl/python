



from flask import Flask
from flask_restful import Api
from resources.home_resource import HomeResource

app = Flask(__name__)


# @app.route("/")
# def home():
#     return "Hello World Flask"

api = Api(app)
api.add_resource(HomeResource,"/")


if __name__ == 'main':
    app.run()

