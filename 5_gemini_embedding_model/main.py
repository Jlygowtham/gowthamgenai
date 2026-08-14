from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

#Load the api key from .env fileg
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Assign the api key Directly to the client (not recommended for production)
#client = genai.Client(api_key ="")


result = client.models.embed_content(
        model="gemini-embedding-2",
        contents="What is the Gemini embedding model?"
)

print(result.embeddings[0].values)
print(f"Embedding length: {len(result.embeddings[0].values)}")