
import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        online_order = int(request.form["Online Order"])
        book_table = int(request.form["Book Table"])
        votes = int(request.form["Votes"])
        location = int(request.form["Location"])
        rest_type = int(request.form["Restaurant Type"])
        cuisines = int(request.form["Cuisines"])
        cost = float(request.form["Cost"])
        menu_item = int(request.form["Menu Item"])

        features = [
            online_order,
            book_table,
            votes,
            location,
            rest_type,
            cuisines,
            cost,
            menu_item
        ]

        limits = [
            (0, 1), (0, 1), (0, 16832), (0, 87),
            (0, 72), (0, 1680), (40, 6000), (0, 5047)
        ]

        for value, (minimum, maximum) in zip(features, limits):
            if not minimum <= value <= maximum:
                return render_template(
                    "index.html",
                    prediction_text=f"Please enter values between {minimum} and {maximum}."
                )

        prediction = model.predict(np.array(features).reshape(1, -1))
        output = round(float(prediction[0]), 1)

        return render_template(
            "index.html",
            prediction_text=f"Predicted Restaurant Rating: {output}/5"
        )

    except (ValueError, KeyError):
        return render_template(
            "index.html",
            prediction_text="Invalid input. Please enter valid numerical values."
        )


if __name__ == "__main__":
    app.run(debug=True)
