from dependency_injector import containers, providers

from .services import SearchService


class Container(containers.DeclarativeContainer):

    # wiring_config = containers.WiringConfiguration(modules=[".views"])

    # config = providers.Configuration(yaml_files=["config.yml"])

    search_service = providers.Factory(
        SearchService
    )
