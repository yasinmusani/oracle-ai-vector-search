def create_vector_index(cursor):
    cursor.execute("""
        CREATE INDEX prod_vec_idx ON products(prod_embedding)
        INDEXTYPE IS VECTOR_SEARCH
    """)

def search_similar_products(cursor, query_embedding):
    sql = """
        SELECT product_name, description
        FROM products
        ORDER BY VECTOR_DISTANCE(prod_embedding, :1)
        FETCH FIRST 5 ROWS ONLY
    """
    cursor.execute(sql, [query_embedding])
    return cursor.fetchall()
