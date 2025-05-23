import threading
import time

from datetime import datetime
                    
from scheduler.scheduler import start_scheduler_background
from subscriptions.manager import load_subscriptions, add_subscription, remove_subscription
from fetcher.github_api import get_repo_events
from reporter.generator import generate_report
from fetcher.github_fetcher import save_daily_progress
from reporter.daily_reporter import generate_daily_summary
from llm.openai_client import OpenAIClient

def print_help():
    print("\n=== Welcome to Tech Sentinel (Interactive Mode) ===\n")
    print("Available commands:")
    print("  add <owner/repo>      Add a GitHub repository to the subscription list.")
    print("  remove <owner/repo>   Remove a GitHub repository from the subscription list.")
    print("  fetch                 Immediately fetch updates for all subscribed repositories.")
    print("  show                  Show current subscriptions.")
    print("  help                  Show this help message.")
    print("  exit                  Exit Tech Sentinel.\n")
    print("Examples:")
    print("  add langchain-ai/langchain")
    print("  remove langchain-ai/langchain")
    print("  fetch\n")
    print("Scheduler is running in the background... Scheduled updates will be fetched automatically.\n")

def command_loop():
    print_help()  # 启动时打印帮助文档一次

    while True:
        try:
            command = input("\n>>> ").strip()
            if not command:
                continue

            if command.startswith("add "):
                repo_path = command[4:].strip()
                try:
                    if '/' not in repo_path:
                        raise ValueError("Invalid format. Use 'owner/repo'.")

                    url = f"https://github.com/{repo_path}"
                    add_subscription(url)
                    print(f"Added subscription: {url}")
                except ValueError as ve:
                    print(f"[Error] {ve}")

            elif command.startswith("remove "):
                repo_path = command[7:].strip()
                try:
                    if '/' not in repo_path:
                        raise ValueError("Invalid format. Use 'owner/repo'.")

                    url = f"https://github.com/{repo_path}"
                    remove_subscription(url)
                    print(f"Removed subscription: {url}")
                except ValueError as ve:
                    print(f"[Error] {ve}")

            elif command == "fetch":
                fetch_and_report()
 
            elif command.startswith("report "):
                repo_path = command[7:].strip()
                try:
                    if '/' not in repo_path:
                        raise ValueError("Invalid format. Use 'owner/repo'.")
                    
                    owner, repo = repo_path.split("/")
                    
                    # Step 1: 保存每日进展
                    save_daily_progress(owner, repo)

                    # Step 2: 构造日报路径
                    today = datetime.now().strftime("%Y-%m-%d")
                    progress_file = f"reports/{repo}-{today}.md"

                    # Step 3: 调用GPT生成总结
                    client = OpenAIClient()
                    generate_daily_summary(progress_file, client)

                except ValueError as ve:
                    print(f"[Error] {ve}")
                except Exception as e:
                    print(f"[Error] Failed to generate report for {repo_path}: {e}")
           
                
            elif command == "show":
                subs = load_subscriptions()
                if not subs:
                    print("No subscriptions.")
                else:
                    print("Current Subscriptions:")
                    for s in subs:
                        print(f"- {s}")

            elif command == "help":
                print_help()

            elif command == "exit":
                print("Exiting Tech Sentinel...")
                break

            else:
                print("[Error] Unknown command. Type 'help' for a list of commands.")

        except KeyboardInterrupt:
            print("\nReceived KeyboardInterrupt. Exiting...")
            break

def fetch_and_report():
    updates = {}
    subs = load_subscriptions()
    if not subs:
        print("No subscriptions found.")
        return

    for repo_url in subs:
        try:
            owner, repo = parse_repo_url(repo_url)
            events = get_repo_events(owner, repo)
            updates[repo_url] = parse_events(events)
        except Exception as e:
            print(f"[Error] Failed to fetch updates for {repo_url}: {e}")

        markdown_file_path = save_daily_progress(owner, repo)
        generate_daily_summary(markdown_file_path, openai_client)
        
    report = generate_report(updates)
    print("\n===== Update Report =====\n")
    print(report)

def parse_repo_url(repo_url: str):
    parts = repo_url.rstrip('/').split('/')
    return parts[-2], parts[-1]

def parse_events(events):
    return [f"{event['type']} by {event['actor']['login']}" for event in events]

# 创建 OpenAIClient 实例
openai_client = OpenAIClient()
    
if __name__ == "__main__":
    # 启动Scheduler在后台
    scheduler_thread = threading.Thread(target=start_scheduler_background, daemon=True)
    scheduler_thread.start()
    
    # 启动交互式命令循环
    command_loop()
