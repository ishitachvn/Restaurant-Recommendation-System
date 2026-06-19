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
    location = user_data.get("location")

    results = recommend_restaurants(
        cuisine,
        budget,
        rating,
        restaurant_type,
        location
    )

    return jsonify(
        results.to_dict(orient="records")
    )


if __name__ == "__main__":
    app.run(debug=True)


from compare_restaurants import compare_restaurants

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