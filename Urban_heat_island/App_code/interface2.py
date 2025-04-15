import streamlit as st
import numpy as np
import joblib

# Load your trained model
model = joblib.load('URBAN_HEAT_model.pkl')

st.title("Urban Heat Island Prediction App")

# Input fields for user-friendly features
temperature = st.number_input("Average Temperature (°C)", min_value=-10.0, max_value=50.0, value=30.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=150.0, value=10.0)
air_quality = st.number_input("Air Quality Index", min_value=0.0, max_value=500.0, value=100.0)

if st.button("Predict Heat Island Risk"):
    # Map user-friendly names to your trained model's expected feature order
    user_input = np.array([[temperature, humidity, wind_speed, air_quality]])
    
    try:
        prediction = model.predict(user_input)
        st.success(f"Predicted Value: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
