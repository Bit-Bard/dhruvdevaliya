import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load your trained model
try:
    model = joblib.load("URBAN_HEAT_model.pkl")
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Expected Features
expected_features = [
    "climate_udel_air_temp_v501_mean.1907.max",
    "climate_udel_air_temp_v501_mean.1901.max",
    "climate_udel_air_temp_v501_mean.1912.max",
    "climate_udel_air_temp_v501_mean.1913.max",
    "climate_udel_air_temp_v501_mean.1906.max",
    "climate_udel_air_temp_v501_mean.1905.max",
    "climate_udel_air_temp_v501_mean.1910.max",
    "climate_udel_air_temp_v501_mean.1903.max"
]

st.title("🌆 Urban Heat Island Prediction App")

st.write("Input the following climatic feature values to predict urban heat presence:")

# Collect user input for all expected features
user_input = {}
for feature in expected_features:
    user_input[feature] = st.number_input(f"{feature}", min_value=-50.0, max_value=100.0, step=0.1)

# When user clicks predict
if st.button("Predict"):
    try:
        input_df = pd.DataFrame([user_input], columns=expected_features)
        prediction = model.predict(input_df)

        st.success(f"🌡️ Predicted Temperature / UHI Score: {prediction[0]:.2f}")
        
        if prediction[0] > 30:  # Example threshold
            st.warning("⚠️ High potential for Urban Heat Island effect!")
        else:
            st.info("✅ Low Urban Heat Island risk.")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
