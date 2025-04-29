import requests
from config import GITHUB_TOKEN

GITHUB_API_URL = "https://api.github.com"

def get_repo_events(owner, repo):
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(f"{GITHUB_API_URL}/repos/{owner}/{repo}/events", headers=headers)
    response.raise_for_status()
    return response.json()
