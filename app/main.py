from flask import Flask, request, jsonify
from db_utils import get_connection
from embedding import get_embedding
from vector_search import search_similar_products

app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Query is required"}), 400

    embedding = get_embedding(query)

    with get_connection() as conn:
        cursor = conn.cursor()
        results = search_similar_products(cursor, embedding)

    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)
