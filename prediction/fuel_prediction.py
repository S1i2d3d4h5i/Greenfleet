import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load dataset
data = pd.read_csv("data/vessels.csv")

X = data[
    [
        "vessel_type",
        "fuel_type",
        "distance_km",
        "speed_knots",
        "cargo_load_tonnes"
    ]
]

y = data["fuel_consumption_tonnes"]

categorical_features = [
    "vessel_type",
    "fuel_type"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )
        )
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

score = model.score(X_test, y_test)

# Save trained model
joblib.dump(model, "prediction/fuel_model.pkl")

print("Fuel Prediction Model Trained Successfully")
print("Model R² Score:", round(score, 3))
print("Model saved successfully.")