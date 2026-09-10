from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

from optimization.optimizer import quantum_inspired_optimizer


app = Flask(__name__)
CORS(app)


# Load trained fuel prediction model
model = joblib.load("prediction/fuel_model.pkl")


@app.route("/")
def home():

    return jsonify({
        "message": "GreenFleet backend is running"
    })


# ---------------------------------------------------
# FUEL PREDICTION
# ---------------------------------------------------

@app.route("/predict-fuel", methods=["POST"])
def predict_fuel():

    data = request.get_json()

    try:

        vessel_type = data.get(
            "vessel_type",
            "Container"
        )

        fuel_type = data.get(
            "fuel_type",
            "Diesel"
        )

        distance = float(
            data.get("distance", 0)
        )

        speed = float(
            data.get("speed", 0)
        )

        load = float(
            data.get("load", 0)
        )


        if distance <= 0 or speed <= 0 or load <= 0:

            return jsonify({
                "error": "Please enter valid values"
            }), 400


        input_data = pd.DataFrame({

            "vessel_type": [vessel_type],

            "fuel_type": [fuel_type],

            "distance_km": [distance],

            "speed_knots": [speed],

            "cargo_load_tonnes": [load]

        })


        prediction = model.predict(
            input_data
        )[0]


        return jsonify({

            "vessel_type": vessel_type,

            "fuel_type": fuel_type,

            "distance": distance,

            "speed": speed,

            "load": load,

            "fuel_consumption": round(
                float(prediction),
                2
            )

        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500



# ---------------------------------------------------
# FLEET OPTIMIZATION
# ---------------------------------------------------

@app.route("/optimize-fleet", methods=["POST"])
def optimize_fleet():

    data = request.get_json()

    try:

        cargo_demand = float(
            data.get("cargo_demand", 0)
        )

        max_speed = float(
            data.get("max_speed", 0)
        )


        if cargo_demand <= 0 or max_speed <= 0:

            return jsonify({
                "error": "Please enter valid values"
            }), 400


        # Run quantum-inspired optimizer
        result = quantum_inspired_optimizer(
    cargo_demand=cargo_demand,
    max_speed=max_speed,
    preferred_fuel=data.get("preferred_fuel", "Any")
)


        return jsonify(result)


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500



# ---------------------------------------------------
# START SERVER
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )