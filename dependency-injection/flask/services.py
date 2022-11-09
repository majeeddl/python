
from github import Github, Repository

class SearchServices :

    def __init__(self,github_client:Github) -> None:
        self._github_client  = github_client

    def search_repository(self, query, limit):
        repositories = self._github_client.search_repoditory(
            query=query,
            **{"in":"name"}
        )

        return [
            self._format_commit(repository) for repository in repositories[:limit]
        ]
    
    def _format_repo(self, repository: Repository):
        commits = repository.get_commits()
        return {
            "url": repository.html_url,
            "name": repository.name,
            "owner": {
                "login": repository.owner.login,
                "url": repository.owner.html_url,
                "avatar_url": repository.owner.avatar_url,
            },
            "latest_commit": self._format_commit(commits[0]) if commits else {},
        }

    def _format_commit(sel):
        return {
            "sha": "sha",
            "url": "html_url",
            "message": "message",
            "author_name": "author.name",
        }
