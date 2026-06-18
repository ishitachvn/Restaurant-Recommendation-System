from flask import Flask, request, jsonify
from smart_recommendation import recommend_restaurants

app = Flask(__name__)


@app.route("/recommend", methods=["POST"])
def recommend():

    user_data = request.json

    cuisine = user_data.get("cuisine")
    budget = float(user_data.get("budget"))
    rating = float(user_data.get("rating"))
    restaurant_type = user_data.get("restaurant_type")

    results = recommend_restaurants(
        cuisine,
        budget,
        rating,
        restaurant_type
    )

    return jsonify(
        results.to_dict(orient="records")
    )


if __name__ == "__main__":
    app.run(debug=True)