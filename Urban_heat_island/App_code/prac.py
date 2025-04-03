import joblib

# Load the trained model
model = joblib.load("urban_heat_rf_model.pkl")

# Get the expected feature names
expected_features = model.feature_names_in_  # This will show the features used during training
print("Expected Features:", expected_features)

import numpy as np
import pandas as pd
import joblib

# Load trained model


# Define the expected feature names
expected_features = [
    'climate_udel_air_temp_v501_mean.1907.max',
    'climate_udel_air_temp_v501_mean.1901.max',
    'climate_udel_air_temp_v501_mean.1912.max',
    'climate_udel_air_temp_v501_mean.1913.max',
    'climate_udel_air_temp_v501_mean.1906.max',
    'climate_udel_air_temp_v501_mean.1905.max',
    'climate_udel_air_temp_v501_mean.1910.max',
    'climate_udel_air_temp_v501_mean.1903.max'
]

# Example user input (only a few values are provided)
user_input = {
    'climate_udel_air_temp_v501_mean.1907.max': 25.0,
    'climate_udel_air_temp_v501_mean.1901.max': 26.5,
    'climate_udel_air_temp_v501_mean.1912.max': 24.8,
}

# Fill missing values with zero
for feature in expected_features:
    if feature not in user_input:
        user_input[feature] = 0  # Default value for missing features

# Convert to DataFrame and ensure correct order
user_data = pd.DataFrame([user_input], columns=expected_features)

# Now, make prediction
prediction = model.predict(user_data)
print("Prediction:", prediction)
