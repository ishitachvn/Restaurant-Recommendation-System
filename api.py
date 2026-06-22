from flask import Flask, request, jsonify

from smart_recommendation import recommend_restaurants
from compare_restaurants import compare_restaurants

app = Flask(__name__)


@app.route("/recommend", methods=["POST"])
def recommend():

    user_data = request.json

    city = user_data.get("city")
    cuisine = user_data.get("cuisine")
    budget = float(user_data.get("budget"))
    min_rating = float(user_data.get("min_rating"))
    restaurant_type = user_data.get("restaurant_type")

    results = recommend_restaurants(
        city,
        cuisine,
        budget,
        min_rating,
        restaurant_type

    )

    return jsonify(
        results.to_dict(orient="records")
    )


@app.route("/compare", methods=["POST"])
def compare():

    user_data = request.json

    restaurant1 = user_data.get("restaurant1")
    restaurant2 = user_data.get("restaurant2")

    results = compare_restaurants(
        restaurant1,
        restaurant2
    )

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)