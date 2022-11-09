

from dependency_injector import containers, providers

from github import Gitghub


from . import services

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".views"])