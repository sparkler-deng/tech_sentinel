import schedule
import time
from subscriptions.manager import load_subscriptions
from fetcher.github_api import get_repo_events
from reporter.generator import generate_report
from notifier.email_notifier import EmailNotifier

def job():
    print("[Scheduler] Running scheduled job...")

    updates = {}
    subs = load_subscriptions()
    if not subs:
        print("[Scheduler] No subscriptions found.")
        return

    for repo_url in subs:
        owner, repo = parse_repo_url(repo_url)
        events = get_repo_events(owner, repo)
        updates[repo_url] = parse_events(events)

    report = generate_report(updates)
    notifier = EmailNotifier()
    notifier.notify(report)

def start_scheduler_background():
    from config import SCHEDULE_INTERVAL, DEBUG

    print("[Scheduler] Starting background scheduler... DEBUG =", DEBUG)

    if DEBUG:
        schedule.every(1).minutes.do(job)
    else:
        if SCHEDULE_INTERVAL == "daily":
            schedule.every().day.at("09:00").do(job)
        elif SCHEDULE_INTERVAL == "weekly":
            schedule.every().monday.at("09:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(5)

def parse_repo_url(repo_url: str):
    parts = repo_url.rstrip('/').split('/')
    return parts[-2], parts[-1]

def parse_events(events):
    return [f"{event['type']} by {event['actor']['login']}" for event in events]
