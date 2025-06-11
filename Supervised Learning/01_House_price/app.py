import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('regression.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Set page title
st.set_page_config(page_title="California House Price Prediction", layout="centered")
st.title("🏠 California House Price Prediction")

st.markdown("Enter the house features below to estimate its price (in US dollars):")

# Input fields
medinc = st.number_input("🧾 Median Income(in 10,000s)", min_value=0.0, value=3.5)
houseage = st.number_input("🏗️ House Age", min_value=0.0, value=25.0)
averooms = st.number_input("🛏️ Average Rooms", min_value=0.0, value=5.0)
population = st.number_input("👥 Population", min_value=0.0, value=1000.0)
aveoccup = st.number_input("👨‍👩‍👧‍👦 Average Occupancy", min_value=0.0, value=3.0)
latitude = st.number_input("🌍 Latitude", min_value=32.0, max_value=42.0, value=34.0)
longitude = st.number_input("🌎 Longitude", min_value=-124.0, max_value=-114.0, value=-118.0)

# Predict button
if st.button("💡 Predict"):
    input_values = [medinc, houseage, averooms, population, aveoccup, latitude, longitude]
    input_array = np.array(input_values).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    predicted_price = model.predict(input_scaled)[0] * 100000
    st.success(f"✅ Predicted House Price: ${predicted_price:,.2f}")
