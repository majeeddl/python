"""Main module."""

import sys
from dependency_injector.wiring import Provide, inject

from multi_container.services import UserService
from .containers import Application


@inject
def main(email: str, user_service: UserService = Provide[Application.services.user]) -> None:
    print('test')
    user = user_service.get_user(email)
    print(user)



if __name__ == "__main__":
    application = Application()
    application.init_resources()
    application.wire(modules=[__name__])

    main(*sys.argv[1:])
