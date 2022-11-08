from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from email_client import EmailClient
from email_reader import EmailReader


class Containter(containers.DeclarativeContainer):
    config = providers.Configuration('config')

    email_client = providers.Singleton(EmailClient, config)

    email_reader = providers.Singleton(EmailReader, config)


# class Clients(containers.DeclarativeContainer):
#     email_client = providers.Singleton(EmailClient, Containter.config)


# class Readers(containers.DeclarativeContainer):
#     email_reader = providers.Singleton(EmailReader,Containter.config)
