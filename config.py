import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
SUBSCRIPTION_FILE = "subscriptions.json"

SCHEDULE_INTERVAL = "daily"
NOTIFICATION_CHANNELS = ["email", "slack"]

DEBUG = True
