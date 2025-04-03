import joblib
import json

import pickle

# Load the trained Random Forest model
with open("urban_heat_rf_model.pkl", "rb") as file:
    model = pickle.load(file)


# Save model
joblib.dump(model, "urban_heat_rf_model.pkl")

# Save expected feature names
expected_features = [
    "climate_udel_air_temp_v501_mean.1907.max",
    "climate_udel_air_temp_v501_mean.1901.max",
    "climate_udel_air_temp_v501_mean.1912.max",
    "climate_udel_air_temp_v501_mean.1913.max",
    "climate_udel_air_temp_v501_mean.1906.max",
    "climate_udel_air_temp_v501_mean.1905.max",
    "climate_udel_air_temp_v501_mean.1910.max",
    "climate_udel_air_temp_v501_mean.1903.max",
]

with open("feature_columns.json", "w") as f:
    json.dump(expected_features, f)
