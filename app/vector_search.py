import numpy as np

def search_similar_products(cursor, query_embedding):
    # Ensure the embedding is converted to a list of floats
    if isinstance(query_embedding, np.ndarray):
        query_embedding = query_embedding.tolist()

    sql = """
        SELECT product_name, description
        FROM products
        ORDER BY VECTOR_DISTANCE(prod_embedding, :1)
        FETCH FIRST 5 ROWS ONLY
    """
    cursor.execute(sql, [query_embedding])
    return cursor.fetchall()

