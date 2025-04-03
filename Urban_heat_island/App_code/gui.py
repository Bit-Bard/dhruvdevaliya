import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("urban_heat_rf_model.pkl")

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

# Streamlit UI
st.title("Urban Heat Island Prediction")
st.markdown("Enter the required values below. Missing values will be auto-filled.")

# Input fields
user_input = {}
for feature in expected_features:
    user_input[feature] = st.number_input(f"{feature}", value=0.0)

# Predict button
if st.button("Predict"):
    # Convert input to DataFrame
    user_data = pd.DataFrame([user_input], columns=expected_features)

    # Make prediction
    prediction = model.predict(user_data)

    # Display result
    st.success(f"Prediction: {prediction[0]}")
    if prediction[0] > 25:
        st.warning("⚠️ This area is likely to be a Heat Island!")
    else:
        st.info("✅ This area is NOT a Heat Island.")

# Run using: `streamlit run app.py`
