import json
import re
from config import SUBSCRIPTION_FILE

GITHUB_REPO_URL_PATTERN = r"^https://github\.com/[^/]+/[^/]+/?$"

def load_subscriptions():
    try:
        with open(SUBSCRIPTION_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_subscriptions(subs):
    with open(SUBSCRIPTION_FILE, 'w') as f:
        json.dump(subs, f, indent=2)

def is_valid_github_repo_url(url):
    return re.match(GITHUB_REPO_URL_PATTERN, url) is not None

def add_subscription(repo_url):
    if not is_valid_github_repo_url(repo_url):
        raise ValueError("Invalid GitHub repository URL format.")
    
    subs = load_subscriptions()
    if repo_url not in subs:
        subs.append(repo_url)
        save_subscriptions(subs)
    else:
        print(f"[Warning] Subscription already exists: {repo_url}")

def remove_subscription(repo_url):
    subs = load_subscriptions()
    if repo_url in subs:
        subs.remove(repo_url)
        save_subscriptions(subs)
    else:
        print(f"[Warning] Subscription not found: {repo_url}")
