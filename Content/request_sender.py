import requests

class GitHubSender:
    url = "https://api.github.com"

    def get_repos_of_user(self, user: str, pagination:int = 100):
        return requests.get(
            f'{self.url}/users/{user}/repos',params={"prer_page": pagination}
            ).json()
    
    def get_repos_of_org(self, org: str, pagination:int = 100):
        return requests.get(
            f'{self.url}/orgs/{org}/repos',params={"prer_page": pagination}
            ).json()

    def get_repo_content(self, owner: str, repo: str, path: str = ""):
        print(f'{self.url}/repos/{owner}/{repo}/contents/{path}')
        return requests.get(
            f'{self.url}/repos/{owner}/{repo}/contents/{path}'
            ).json()

    def get_repos_commits(self, owner: str, repo: str):
        return requests.get(
            f'{self.url}/repos/{owner}/{repo}/commits'
            ).json()
    
    def check_rate_limit(self):
        return requests.get(f"{self.url}/rate_limit").json()
    

    def search_repositories(self, query:str, pagination:int = 100):
        url = f"{self.url}/search/repositories"
        params = {"q": query, "per_page": pagination}
        response = requests.get(url, params=params)
        return response.json()