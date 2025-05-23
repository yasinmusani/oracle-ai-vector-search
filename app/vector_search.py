import numpy as np
import json

def search_similar_products(cursor, query_embedding):
    if isinstance(query_embedding, np.ndarray):
        query_embedding = query_embedding.astype(np.float32).tolist()

    # Convert list to string and pass as JSON
    embedding_str = json.dumps(query_embedding)

    sql = """
        SELECT product_name, description, VECTOR_DISTANCE(prod_embedding, :1) AS distance
        FROM products
        ORDER BY distance
        FETCH FIRST 5 ROWS ONLY
    """
    cursor.execute(sql, [embedding_str])
    return cursor.fetchall()

