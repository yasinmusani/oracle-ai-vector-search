import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np  # Add at the top

# Load environment variables
load_dotenv()

# Absolute path to the local model directory
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "../models/all-MiniLM-L6-v2")

# Ensure the model path exists
if not os.path.isdir(model_path):
    raise FileNotFoundError(f"Model path not found: {model_path}")

# Load tokenizer and model from local directory
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModel.from_pretrained(model_path, local_files_only=True)



#def get_embedding(text):
#    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
#    with torch.no_grad():
#        outputs = model(**inputs)
#    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy().astype(np.float32)  # Ensure float32
#    return embeddings


def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy().astype(np.float32)
    
    print(f"🔍 Embedding for '{text}': {embeddings[:5]}...")  # Check the first few values
    return embeddings




# Test block
if __name__ == "__main__":
    test_text = "This is a test sentence."
    print(get_embedding(test_text))

