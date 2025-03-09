import requests
import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict, Any

class GitHubAPI:
    """
    A class used to interact with the GitHub API.

    ...

    Attributes
    ----------
    base_url : str
        a formatted string of the base url for the GitHub API
    token : str
        the OAuth token for authenticating with the GitHub API

    Methods
    -------
    get_repo_info(owner: str, repo: str) -> Dict[str, Any]:
        Returns a dictionary containing information about a GitHub repository.
    """

    def __init__(self, token: str):
        """
        Parameters
        ----------
        token : str
            The OAuth token for authenticating with the GitHub API.
        """

        self.base_url = "https://api.github.com"
        self.token = token

    def get_repo_info(self, owner: str, repo: str) -> Dict[str, Any]:
        """Returns a dictionary containing information about a GitHub repository.

        Parameters
        ----------
        owner : str
            The owner of the repository.
        repo : str
            The name of the repository.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing information about the repository.
        """

        url = f"{self.base_url}/repos/{owner}/{repo}"
        headers = {"Authorization": f"token {self.token}"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()

def visualize_data(data: Dict[str, Any]):
    """Visualizes the data from a GitHub repository using matplotlib.

    Parameters
    ----------
    data : Dict[str, Any]
        The data from a GitHub repository.
    """

    df = pd.DataFrame(data)
    df.plot(kind='bar', x='name', y='stargazers_count', color='blue')
    plt.title('GitHub Repo Star Count')
    plt.xlabel('Repo Name')
    plt.ylabel('Star Count')
    plt.show()

# Example usage:
github_api = GitHubAPI("your_token_here")
repo_info = github_api.get_repo_info("owner_name", "repo_name")
visualize_data(repo_info)