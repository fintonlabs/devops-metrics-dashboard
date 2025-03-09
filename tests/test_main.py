import unittest
from unittest.mock import patch
from main import GitHubAPI

class TestGitHubAPI(unittest.TestCase):
    @patch('main.requests.get')
    def test_get_repo_info(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {"name": "test_repo", "stargazers_count": 10}

        github_api = GitHubAPI("test_token")
        repo_info = github_api.get_repo_info("test_owner", "test_repo")

        self.assertEqual(repo_info, {"name": "test_repo", "stargazers_count": 10})

if __name__ == '__main__':
    unittest.main()