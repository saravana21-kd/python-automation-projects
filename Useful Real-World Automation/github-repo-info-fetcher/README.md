# GitHub Repo Info Fetcher

A simple Python automation script that fetches information about any public GitHub repository using the GitHub REST API.

## Features

- Fetch repository details
- Show stars, forks, issues
- Display primary programming language
- Works with any public GitHub repository

## Technologies Used

- Python
- Requests library
- GitHub REST API

## Installation

```
pip install requests
```

## Usage

```
python repo_info_fetcher.py
```

Enter the repository owner and repository name when prompted.

## Example

Input:

```
owner: torvalds
repo: linux
```

Output:

- Repository name
- Stars
- Forks
- Language
- Issues count
- Repository URL
