from llm.openai_client import OpenAIClient
import os
from datetime import datetime

# GPT-4 系统提示词，可以在此处调整输出风格
SYSTEM_PROMPT = (
    "You are a professional assistant. "
    "You help summarize progress reports based on open issues and pull requests. "
    "The summary should be concise, formal, and focus on the main topics."
)

def generate_daily_summary(markdown_file_path: str, openai_client: OpenAIClient) -> str:
    """
    生成项目日报：读取 markdown 文件内容并通过 GPT-4 生成正式日报
    :param markdown_file_path: 每日进展的 Markdown 文件路径
    :param openai_client: OpenAIClient 实例，用于调用 GPT-4 API
    :return: GPT-4 返回的日报总结
    """

    # 读取 Markdown 文件
    with open(markdown_file_path, "r", encoding="utf-8") as file:
        progress_report = file.read()

    # 拼接最终 prompt
    prompt = f"Here is the progress report for {markdown_file_path.split('-')[0]}:\n\n{progress_report}\n\nPlease summarize it concisely and professionally."

    # 调用 GPT-4 获取总结
    summary = openai_client.chat(prompt, system_prompt=SYSTEM_PROMPT)

    # 构建日报文件名和路径
    today = datetime.now().strftime("%Y-%m-%d")
    summary_filename = markdown_file_path.replace('.md', f'-summary-{today}.md')
    
    # 保存生成的正式日报
    with open(summary_filename, "w", encoding="utf-8") as summary_file:
        summary_file.write(f"# {today} - {markdown_file_path.split('-')[0]} Project Daily Report\n\n")
        summary_file.write(summary)
    
    print(f"[OK] Daily summary saved as: {summary_filename}")
    return summary
