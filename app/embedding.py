import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text):
    # Updated API call for OpenAI Python >= 1.0.0
    response = openai.embeddings.create(
        input=[text],
        model="text-embedding-ada-002"  # The new model name
    )
    return response['data'][0]['embedding']
