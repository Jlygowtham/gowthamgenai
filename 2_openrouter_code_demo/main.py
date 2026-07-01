from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv('OPEN_ROUTER_API'),
# )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="", #paste your api key here
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b:free",
    messages=[{"role": "user", "content": "Why do LLMs hallucinate?"}],
    max_tokens = 1000
)

print(response.choices[0].message.content)
