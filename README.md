# Develop a dashboard that aggregates and visualizes key metrics from DevOps tools, providing real-time insights into pipeline performance

# Overview
This project focuses on developing a dashboard that aggregates and visualizes key metrics from DevOps tools, providing real-time insights into pipeline performance. By integrating with GitHub's API, the dashboard can pull data directly from your repositories and display it in an easy-to-understand visual format. This allows teams to monitor the state of their DevOps pipelines, quickly identifying bottlenecks, inefficiencies, or areas of concern. It's a powerful tool for any team looking to streamline their development process and make data-driven decisions to boost their productivity.

# Features

- **GitHub Integration 🔄**  
  The dashboard is built to integrate seamlessly with GitHub. It utilizes the GitHub API to fetch real-time data about the repositories. By using an OAuth token for authentication, it can access and display data from both public and private repositories.

- **Real-time Data 📈**  
  The data displayed on the dashboard is fetched in real-time, ensuring that the metrics you're seeing are always up-to-date. This real-time functionality is crucial for monitoring the current state of your DevOps pipelines and making timely decisions.

- **Rich Data Visualization 📊**  
  The dashboard uses the `matplotlib` library for visualizing the fetched data. This library allows for a wide range of visualization options, enabling the dashboard to display complex data in a user-friendly manner. Whether you want to see a pie chart of commit frequencies, a bar graph of issue resolutions, or a scatter plot of pull requests over time, this dashboard can accommodate your needs.

- **Data Aggregation 🗄️**  
  The dashboard not only fetches data but also aggregates it in a meaningful way. It uses the `pandas` library to manage and manipulate the fetched data, enabling you to see aggregated metrics like average commit size, issue resolution time, etc.

- **Repository Specific Information 📂**  
  The dashboard can fetch and display detailed information about specific repositories. This includes data like the number of branches, commits, contributors, etc. This feature can be very useful for maintaining an overview of specific projects.

- **Type Checking 🛠️**  
  The code utilizes Python's typing system to ensure that the data being processed is of the expected type. This helps prevent potential bugs related to unexpected data types and improves the overall reliability of the software.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

# Installation Instructions

This guide provides step-by-step instructions on how to install and configure the DevOps Dashboard project. 

## Prerequisites

Before you install the project, ensure your system meets the following prerequisites:

- Python 3.6 or higher. You can download it from the [official Python website](https://www.python.org/downloads/).
- Pip, Python’s package installer. It's typically included in the Python installation.
- Git, to clone the project repository. Download from the [official Git website](https://git-scm.com/downloads).
- Access to the internet to fetch data from the GitHub API.

## Required Python Libraries

The project requires the following Python libraries:

- requests
- matplotlib
- pandas

You can install these libraries using pip. The command to install them is:

```bash
pip install requests matplotlib pandas
```

## Installation Process

Follow these steps to install the DevOps Dashboard project:

1. Clone the project repository from GitHub. Replace `<url>` with the repository's URL.

    ```bash
    git clone <url>
    ```

2. Navigate into the project directory:

    ```bash
    cd <project-directory>
    ```

3. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Verification

To verify the installation, run the following command:

```bash
python <main-script>.py
```

Replace `<main-script>.py` with the name of the main Python script for the project. If the program runs without any errors, the installation was successful.

## Post-Installation Configuration

Before using the `GitHubAPI` class, you need to provide your GitHub OAuth token. The token is used to authenticate with the GitHub API.

To generate a new token:

1. Go to your GitHub settings.
2. In the left sidebar, click Developer settings.
3. In the left sidebar, click Personal access tokens.
4. Click Generate new token.
5. Give your token a descriptive name.
6. Select the scopes, or permissions, you'd like to grant this token. To fetch repository information, select `repo`.
7. Click Generate token.

Copy the generated token and use it to instantiate the `GitHubAPI` class as follows:

```python
github_api = GitHubAPI("<your-token>")
```

Replace `<your-token>` with the token you generated. You're now ready to use the `GitHubAPI` class to fetch data from the GitHub API. Be sure to keep your token safe and don't share it with others.

# Dashboard Aggregator for DevOps Tools Documentation

This guide provides detailed documentation for the `GitHubAPI` class, a component of our dashboard project that interacts with the GitHub API to retrieve repository information.

## Table of Contents
1. Basic Usage
2. Common Use Cases
3. Command-Line Arguments
4. Expected Outputs
5. Advanced Usage

## 1. Basic Usage

To begin, you will need to instantiate the `GitHubAPI` class with your GitHub OAuth token:

```python
api = GitHubAPI("your_token_here")
```

You can then use the `get_repo_info` method to retrieve information about a specific repository:

```python
repo_info = api.get_repo_info("owner_name", "repo_name")
```

## 2. Common Use Cases

The `get_repo_info` method is typically used to fetch detailed information about a repository, such as:

- The repository's name
- The repository owner's name
- The number of stars
- The number of forks
- The date it was created
- The language used

For example, to fetch the number of stars a repository has:

```python
repo_info = api.get_repo_info("owner_name", "repo_name")
stars_count = repo_info['stargazers_count']
```

## 3. Command-Line Arguments

Currently, the `GitHubAPI` class does not interact with command-line arguments. All parameters are passed directly to the methods.

## 4. Expected Outputs

The `get_repo_info` method returns a dictionary with information about the specified repository. An example output might look like this:

```python
{
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "private": false,
    "owner": {
        "name": "octocat",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
    },
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2016-12-06T13:06:37Z",
    "pushed_at": "2011-01-26T19:06:43Z",
    "homepage": "",
    "size": 108,
    "stargazers_count": 80,
    "watchers_count": 80,
    "language": "Ruby",
    "forks_count": 9,
}
```

## 5. Advanced Usage

For advanced usage, you can extend the `GitHubAPI` class to include other API endpoints. For example, you could add a method to fetch a list of all repositories for a particular user:

```python
def get_user_repos(self, username: str) -> Dict[str, Any]:
    response = requests.get(f"{self.base_url}/users/{username}/repos", 
                            headers={'Authorization': f'token {self.token}'})
    return response.json()
```
This would allow you to iterate through all of a user's repositories and aggregate data in your dashboard:

```python
repos_info = api.get_user_repos("username")
for repo in repos_info:
    print(repo['name'], repo['stargazers_count'])
```

# GitHubAPI Class Documentation

The `GitHubAPI` class is designed to interact with the GitHub API. This class is responsible for fetching repository information using the GitHub API.

## Class Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| base_url  | str  | The base URL for the GitHub API. This is set to "https://api.github.com" by default. |
| token     | str  | The OAuth token used for authenticating with the GitHub API. |

## Class Methods

### `__init__(self, token: str)`

This is the constructor method for the `GitHubAPI` class. This method initializes a new instance of the class.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| token     | str  | The OAuth token used for authenticating with the GitHub API. |

#### Example Usage

```python
github_api = GitHubAPI(token="your_github_oauth_token")
```

---

### `get_repo_info(self, owner: str, repo: str) -> Dict[str, Any]`

This method returns a dictionary containing information about a GitHub repository.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| owner     | str  | The username of the repository owner. |
| repo      | str  | The name of the repository. |

#### Return Value

The method returns a dictionary containing information about the specified GitHub repository.

#### Example Usage

```python
repo_info = github_api.get_repo_info(owner="octocat", repo="Hello-World")
```

## Best Practices and Common Patterns

1. **Token Handling:** Ensure that your OAuth tokens are stored securely. Do not hard-code them into your scripts. Consider using environment variables or secure token storage solutions.

2. **Error Handling:** The methods in this class do not include error handling. You should implement error handling in your code to handle potential API errors, such as rate limiting, repository not found, etc.

3. **Data Usage:** The data returned from the `get_repo_info` method can be used to gain insights into repository details such as forks count, stars count, open issues count, etc. Use this data according to your application's requirements.

## ⚙️ Configuration
Configuration options for customizing the application's behavior.

## 🔍 Troubleshooting
Common issues and their solutions.

## 🤝 Contributing
Guidelines for contributing to the project.

## 📄 License
This project is licensed under the MIT License.

## Features

- Complete feature 1: Detailed description
- Complete feature 2: Detailed description
- Complete feature 3: Detailed description

## API Documentation

### Endpoints

#### `GET /api/resource`

Returns a list of resources.

**Parameters:**

- `limit` (optional): Maximum number of resources to return

**Response:**

```json
{
  "resources": [
    {
      "id": 1,
      "name": "Resource 1"
    }
  ]
}
```
