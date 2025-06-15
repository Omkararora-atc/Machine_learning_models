import streamlit as st
import numpy as np
import pickle

# Set page config
st.set_page_config(page_title="Diabetes Predictor", page_icon="🩺", layout="centered")

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Custom CSS
st.markdown("""
    <style>
        .title {
            font-size:48px;
            font-weight:700;
            background: linear-gradient(90deg, #00C9FF, #92FE9D);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }
        .subtitle {
            font-size:20px;
            text-align:center;
            color: #555;
        }
        .stButton>button {
            background: linear-gradient(to right, #00c6ff, #0072ff);
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🩺 Diabetes Risk Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter your health information below to check your diabetes risk.</div>',
            unsafe_allow_html=True)
st.write("---")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("👶 Pregnancies", min_value=0, max_value=20, value=1)
    glucose = st.number_input("🍬 Glucose Level", min_value=0, max_value=300, value=120)
    blood_pressure = st.number_input("💉 Blood Pressure", min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input("🧪 Skin Thickness", min_value=0, max_value=100, value=20)

with col2:
    insulin = st.number_input("💉 Insulin", min_value=0, max_value=900, value=80)
    bmi = st.number_input("⚖️ BMI", min_value=0.0, max_value=70.0, value=25.0)
    dpf = st.number_input("🧬 Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("🎂 Age", min_value=1, max_value=120, value=30)

st.write("")

# Predict Button
if st.button("Predict My Risk 🚀"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)

    st.write("---")
    if prediction[0] == 1:
        st.markdown("### 😟 You may be at **high risk** of diabetes.")
        st.error("Please consult a doctor for a full diagnosis.")
    else:
        st.markdown("### 😄 You are likely at **low risk** of diabetes.")
        st.success("Keep up the healthy habits!")

