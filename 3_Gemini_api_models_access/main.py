from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

response = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input="Explain how AI internally works in a 100 words"
)

print("="*100)
print("Response:",'\n')
print(response.output_text)
print("="*100)