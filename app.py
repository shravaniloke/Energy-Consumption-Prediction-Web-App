from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("sp.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def home():
    energy = None

    if request.method == "POST":
        # Get user input
        building = request.form["building"]
        area = float(request.form["area"])
        occ = int(request.form["occ"])
        app_used = int(request.form["app"])
        temp = float(request.form["temp"])
        day = request.form["day"]

        # Create input dataframe (same as training format)
        input_data = pd.DataFrame([{
            "Building Type": building,
            "Square Footage": area,
            "Number of Occupants": occ,
            "Appliances Used": app_used,
            "Average Temperature": temp,
            "Day of Week": day
        }])

        # One-hot encode
        input_encoded = pd.get_dummies(input_data)

        # Align columns with training data
        input_encoded = input_encoded.reindex(
            columns=model.feature_names_in_,
            fill_value=0
        )

        # Predict
        energy = model.predict(input_encoded)[0]
        energy = round(energy, 2)

    return render_template("index.html", energy=energy)

if __name__ == "__main__":
    app.run(debug=True)
