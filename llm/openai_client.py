import os
from openai import OpenAI



class OpenAIClient:
    def __init__(self, api_key: str = None, model_name: str = "deepseek-chat"):
        """
        Initialize OpenAI Client
        - api_key: 可以传入，也可以用环境变量 OPENAI_API_KEY
        - model_name: 默认用 gpt-4，可灵活切换 gpt-3.5-turbo 等
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY environment variable.")

        self.client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")
        self.model_name = model_name

    def chat(self, prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
        """
        Send a chat message to GPT model and get the response
        - prompt: 用户输入内容
        - system_prompt: 系统设定，影响AI回答风格
        """
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content


def test_openai_chat():
    client = OpenAIClient()
    prompt = "Summarize the importance of daily standup meetings in agile development."
    response = client.chat(prompt)
    print("\n==== GPT-4 Response ====\n")
    print(response)

if __name__ == "__main__":
    test_openai_chat()
