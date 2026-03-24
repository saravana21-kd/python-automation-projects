import requests

def get_repo_info(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\nRepository Information")
        print("----------------------")
        print("Name:", data["name"])
        print("Owner:", data["owner"]["login"])
        print("Description:", data["description"])
        print("Stars:", data["stargazers_count"])
        print("Forks:", data["forks_count"])
        print("Open Issues:", data["open_issues_count"])
        print("Language:", data["language"])
        print("Repo URL:", data["html_url"])

    else:
        print("Error: Repository not found or API limit reached.")

owner = input("Enter repository owner: ")
repo = input("Enter repository name: ")

get_repo_info(owner, repo)