

import sys
from dependency_injector.wiring import Provide, inject
from .containers import Container

from .services import UserService


@inject
def main(email: str, user_service: UserService = Provide[Container.user_service]) -> None:
    print('test')
    user = user_service.get_user(email)
    print(user)

if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    main(*sys.argv[1:])
