import pandas as pd

# Load dataset
data = pd.read_csv("dataset/cleaned_zomato.csv")


def compare_restaurants(restaurant1, restaurant2):

    r1 = data[
        data["restaurant name"]
        .str.lower()
        .str.strip()
        == restaurant1.lower().strip()
    ]

    r2 = data[
        data["restaurant name"]
        .str.lower()
        .str.strip()
        == restaurant2.lower().strip()
    ]

    if r1.empty:
        return {
            "error": f"{restaurant1} not found"
        }

    if r2.empty:
        return {
            "error": f"{restaurant2} not found"
        }

    restaurant1_data = r1.iloc[0].to_dict()
    restaurant2_data = r2.iloc[0].to_dict()

    winner = {}

    # Rating Winner
    if restaurant1_data["rate (out of 5)"] > restaurant2_data["rate (out of 5)"]:
        winner["rating"] = restaurant1_data["restaurant name"]
    elif restaurant2_data["rate (out of 5)"] > restaurant1_data["rate (out of 5)"]:
        winner["rating"] = restaurant2_data["restaurant name"]
    else:
        winner["rating"] = "Tie"

    # Budget Winner (Lower cost is better)
    if restaurant1_data["avg cost (two people)"] < restaurant2_data["avg cost (two people)"]:
        winner["budget"] = restaurant1_data["restaurant name"]
    elif restaurant2_data["avg cost (two people)"] < restaurant1_data["avg cost (two people)"]:
        winner["budget"] = restaurant2_data["restaurant name"]
    else:
        winner["budget"] = "Tie"

    # Score Calculation
    score1 = 0
    score2 = 0

    # Rating Score
    if restaurant1_data["rate (out of 5)"] > restaurant2_data["rate (out of 5)"]:
        score1 += 1
    elif restaurant2_data["rate (out of 5)"] > restaurant1_data["rate (out of 5)"]:
        score2 += 1

    # Budget Score
    if restaurant1_data["avg cost (two people)"] < restaurant2_data["avg cost (two people)"]:
        score1 += 1
    elif restaurant2_data["avg cost (two people)"] < restaurant1_data["avg cost (two people)"]:
        score2 += 1

    # Overall Winner
    if score1 > score2:
        overall_winner = restaurant1_data["restaurant name"]
    elif score2 > score1:
        overall_winner = restaurant2_data["restaurant name"]
    else:
        overall_winner = "Tie"

    return {
        "restaurant1": restaurant1_data,
        "restaurant2": restaurant2_data,
        "winner": winner,
        "scores": {
            restaurant1_data["restaurant name"]: score1,
            restaurant2_data["restaurant name"]: score2
        },
        "overall_winner": overall_winner
    }


if __name__ == "__main__":

    restaurant1 = input("Enter first restaurant: ")
    restaurant2 = input("Enter second restaurant: ")

    result = compare_restaurants(
        restaurant1,
        restaurant2
    )

    print(result)