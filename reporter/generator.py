def generate_report(updates: dict) -> str:
    report = "Project Update Report\n"
    for repo, changes in updates.items():
        report += f"\nRepository: {repo}\n"
        for change in changes:
            report += f"- {change}\n"
    return report
