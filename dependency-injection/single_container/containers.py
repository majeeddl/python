import logging.config
from dependency_injector import containers, providers

from .services import UserService

class Container(containers.DeclarativeContainer):

    config = providers.Configuration(ini_files='config.ini')


    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )

    # # Gateways

    # database_client = providers.Singleton(
    #     sqlite3.connect,
    #     config.database.dsn,
    # )

    #Services

    user_service = providers.Factory(
        UserService,
        db="majeed"
    )
