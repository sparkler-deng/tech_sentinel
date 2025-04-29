import json
from config import SUBSCRIPTION_FILE

def load_subscriptions():
    with open(SUBSCRIPTION_FILE, 'r') as f:
        return json.load(f)

def add_subscription(repo_url):
    subs = load_subscriptions()
    if repo_url not in subs:
        subs.append(repo_url)
        with open(SUBSCRIPTION_FILE, 'w') as f:
            json.dump(subs, f)
