from flask import Flask, render_template, request
from recommendation_engine import recommend

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def get_recommendations():
    restaurant = request.form["restaurant"]

    results = recommend(restaurant)

    return render_template(
        "result.html",
        restaurant=restaurant,
        recommendations=results
    )

if __name__ == "__main__":
    app.run(debug=True)