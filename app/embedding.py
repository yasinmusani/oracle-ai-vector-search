import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModel
import torch

# Load environment variables
load_dotenv()

# Load the Hugging Face model and tokenizer
model_name = "sentence-transformers/all-MiniLM-L6-v2"  # A popular sentence embedding model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_embedding(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    # Forward pass through the model
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get the embeddings from the model's output (pooling the output from all tokens)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()  # Pooling strategy: mean of token embeddings

    return embeddings

# Example usage
if __name__ == "__main__":
    text = "This is a test sentence."
    embedding = get_embedding(text)
    print(embedding)
