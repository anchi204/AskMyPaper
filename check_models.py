
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load your environment variables (assuming you use .env)
load_dotenv()

# Initialize the client exactly as you do in your rag.py
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API") # Replace with how you load your key if different
)

print("Fetching available models from Groq...\n")

try:
    models = client.models.list()
    print("Valid Model IDs you can use:")
    for model in models.data:
        print(f"- {model.id}")
except Exception as e:
    print(f"Failed to fetch models. Error: {e}")