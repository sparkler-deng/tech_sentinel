from fetcher.github_api import get_repo_events
from reporter.generator import generate_report

def main():
    owner = "langchain-ai"
    repo = "langchain"
    
    events = get_repo_events(owner, repo)
    
    updates = {f"https://github.com/{owner}/{repo}": parse_events(events)}
    report = generate_report(updates)
    
    print("\n===== LangChain 最新更新报告 =====\n")
    print(report)

def parse_events(events):
    parsed = []
    for event in events:
        event_type = event.get('type')
        actor = event.get('actor', {}).get('login')
        if event_type and actor:
            parsed.append(f"{event_type} by {actor}")
    return parsed

if __name__ == "__main__":
    main()
