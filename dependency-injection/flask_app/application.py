

from flask import Flask
from dependency_injector.wiring import Provide, inject

from .containers import Container
from .services import SearchService


@inject
def home(search_service: SearchService = Provide[Container.search_service]):
    print("test")
    print(search_service.search_repositories())
    return "Hello, Flask!"


def create_app() -> Flask:
    container = Container()
    # container.config.github.auth_token.from_env("GITHUB_TOKEN")

    print("heeeee")
    app = Flask(__name__)
    # app.container = container
    container.wire(modules=[__name__])

    @app.route("/")
    def index(search_service: SearchService = Provide[Container.search_service]):
        home()
        return "Hello, Flask!"

    return app
