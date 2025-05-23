from flask import Flask, request, jsonify
from db_utils import get_connection
from embedding import get_embedding
from vector_search import search_similar_products

app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")  # Getting the search query
    if not query:
        return jsonify({"error": "Query is required"}), 400  # Handle missing query

    # Get the query's embedding from Hugging Face model
    embedding = get_embedding(query)

    # Establish DB connection and execute search logic
    with get_connection() as conn:
        cursor = conn.cursor()
        results = search_similar_products(cursor, embedding)

    # Return the results in JSON format
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)

