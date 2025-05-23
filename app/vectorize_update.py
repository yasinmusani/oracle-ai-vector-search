import os
import array
import torch
import oracledb
from transformers import AutoTokenizer, AutoModel

# === Configuration ===
MODEL_PATH = "/home/oracle/oracle-ai-vector-search/models/all-MiniLM-L6-v2"
ORACLE_USER = "hr"
ORACLE_PWD = "oracle"
ORACLE_DSN = "localhost/freepdb1"

# === Load tokenizer & model from local path ===
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModel.from_pretrained(MODEL_PATH)

def get_embedding(text):
    # Tokenize and get transformer outputs
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Mean pooling (basic sentence embedding)
    last_hidden = outputs.last_hidden_state
    attention_mask = inputs["attention_mask"].unsqueeze(-1).expand(last_hidden.size()).float()
    summed = torch.sum(last_hidden * attention_mask, dim=1)
    counts = torch.clamp(attention_mask.sum(dim=1), min=1e-9)
    mean_pooled = summed / counts
    return mean_pooled.squeeze().numpy().astype("float32")

# === Connect and update VECTOR column ===
with oracledb.connect(user=ORACLE_USER, password=ORACLE_PWD, dsn=ORACLE_DSN) as conn:
    cursor = conn.cursor()

    cursor.execute("""
        SELECT product_id, description FROM products
        WHERE prod_embedding IS NULL
    """)
    rows = cursor.fetchall()

    print(f"Found {len(rows)} products to embed.")

    for product_id, description in rows:
        print(f"Embedding product_id={product_id}...")

        embedding = get_embedding(description)
        vec = array.array("f", embedding)  # Oracle VECTOR expects float32 array

        cursor.execute("""
            UPDATE products
            SET prod_embedding = :1
            WHERE product_id = :2
        """, [vec, product_id])

    conn.commit()
    print("✅ All embeddings updated successfully.")

