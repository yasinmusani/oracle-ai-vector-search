from flask import Flask, request, jsonify
from flasgger import Swagger
from db_utils import get_connection
from embedding import get_embedding
from vector_search import search_similar_products

app = Flask(__name__)
swagger = Swagger(app)  # ✅ Initialize Swagger

@app.route("/search", methods=["POST"])
def search():
    """
    Search similar products based on query vector
    ---
    tags:
      - Search
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - query
            properties:
              query:
                type: string
                example: "Watch"
    responses:
      200:
        description: A list of matched products with distances
        content:
          application/json:
            schema:
              type: object
              properties:
                results:
                  type: array
                  items:
                    type: array
                    items:
                      oneOf:
                        - type: string
                        - type: number
                  example:
                    - ["Smartwatch", "Fitness tracking with heart rate monitor", 0.81]
                    - ["Smartphone", "Latest model with AI camera features", 0.82]
      400:
        description: Query is required
    """
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

