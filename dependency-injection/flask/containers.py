

from dependency_injector import containers, providers

from github import Gitghub


import services


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".views"])

    config = providers.Configuration(yaml_files=["config.yml"])

    github_client = providers.Factory(
        Gitghub,
        login_or_token=config.github.auth_token,
        timeout=config.github.request_timeout
        )
        
    search_service = providers.Factory(
        services.SearchService,
        github_client=github_client,
    )
