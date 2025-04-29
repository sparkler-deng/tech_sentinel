import os
import requests
from datetime import datetime
from config import GITHUB_TOKEN

GITHUB_API_URL = "https://api.github.com"
REPORTS_DIR = "reports"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def fetch_repo_issues(owner: str, repo: str) -> list:
    """Fetch open issues for a repository."""
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"
    params = {
        "state": "open",
        "per_page": 100
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    issues = response.json()

    # 排除 PR（issues接口返回PR，需要过滤掉）
    issues = [i for i in issues if "pull_request" not in i]
    return issues

def fetch_repo_pull_requests(owner: str, repo: str) -> list:
    """Fetch open pull requests for a repository."""
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls"
    params = {
        "state": "open",
        "per_page": 100
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def fetch_repo_commits(owner: str, repo: str, since_iso: str) -> list:
    """获取今日以来的 commit 列表"""
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/commits"
    params = {
        "since": since_iso,
        "per_page": 100
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def save_daily_progress(owner: str, repo: str):
    issues = fetch_repo_issues(owner, repo)
    pulls = fetch_repo_pull_requests(owner, repo)

    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{repo.replace('/', '-')}-{today}.md"
    filepath = os.path.join(REPORTS_DIR, filename)

    # 获取当天的 commits（从 00:00 UTC 开始）
    since_iso = datetime.utcnow().strftime("%Y-%m-%dT00:00:00Z")
    commits = fetch_repo_commits(owner, repo, since_iso)

    os.makedirs(REPORTS_DIR, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Daily Progress Report: {owner}/{repo} ({today})\n\n")

        f.write("## 🐛 Open Issues\n")
        if issues:
            for issue in issues:
                f.write(f"- [{issue['title']}]({issue['html_url']}) by {issue['user']['login']}\n")
        else:
            f.write("- No open issues.\n")

        f.write("\n## 🔀 Open Pull Requests\n")
        if pulls:
            for pr in pulls:
                f.write(f"- [{pr['title']}]({pr['html_url']}) by {pr['user']['login']}\n")
        else:
            f.write("- No open pull requests.\n")

        f.write("\n## ✅ Commits Today\n")
        if commits:
            for c in commits:
                msg = c['commit']['message'].split("\n")[0]
                author = c['commit']['author']['name']
                url = c['html_url']
                f.write(f"- [{msg}]({url}) by {author}\n")
        else:
            f.write("- No commits found today.\n")

    print(f"[OK] Saved daily progress: {filepath}")
    return filepath
