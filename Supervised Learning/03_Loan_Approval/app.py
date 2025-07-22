import pickle
import pandas as pd
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Loan Pro Predictor",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Load Model ---
# Use a relative path to ensure it works in different environments
try:
    with open("03_Loan_Approval/loan_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("⚠️ Model file not found. Please ensure 'loan_model.pkl' is in the same directory.")
    st.stop()

# --- CSS Styling ---
st.markdown("""
<style>
    /* --- General & Body --- */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #f8f9fa; /* Soft, light grey background */
    }

    /* --- Main Container --- */
    .stApp {
        background-color: #f8f9fa;
    }

    /* --- Title --- */
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #2c3e50; /* Dark Slate Blue */
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #7f8c8d; /* Greyish Teal */
        text-align: center;
        margin-bottom: 30px;
    }

    /* --- NEW: Style for Input Labels (Column Names) --- */
    label {
        color: #4f4f4f !important; /* Dark Grey for better contrast */
        font-weight: 600 !important; 
        font-size: 0.95rem !important;
    }

    /* --- Form Container --- */
    .stForm {
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 2rem;
        background-color: #ffffff;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
    }

    /* --- Section Headers --- */
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2980b9; /* Bright Blue */
        margin-top: 20px;
        margin-bottom: 15px;
        padding-bottom: 5px;
        border-bottom: 2px solid #e0e0e0;
    }

    /* --- Prediction Result --- */
    .prediction {
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.4rem;
        font-weight: 600;
        margin-top: 25px;
        border: 2px solid;
    }
    .approved {
        background-color: #e8f5e9; /* Light Green */
        color: #2e7d32; /* Dark Green */
        border-color: #4caf50;
    }
    .rejected {
        background-color: #ffebee; /* Light Red */
        color: #c62828; /* Dark Red */
        border-color: #f44336;
    }

    /* --- Footer --- */
    .footer {
        text-align: center;
        font-size: 0.9rem;
        margin-top: 40px;
        color: #95a5a6; /* Soft Grey */
    }

    /* --- Button --- */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #3498db, #2980b9); /* Blue Gradient */
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 14px 0;
        font-size: 1.1rem;
        border: none;
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.4);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(52, 152, 219, 0.5);
    }
    .stButton > button:active {
        transform: translateY(0);
    }

</style>
""", unsafe_allow_html=True)

# --- App Layout ---

st.markdown('<div class="main-title">🏦 Loan Pro Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A smart way to check your loan eligibility instantly.</div>', unsafe_allow_html=True)

# --- Input Form ---
with st.form("loan_application_form"):
    # --- Section: Personal Information ---
    st.markdown('<p class="section-header">👤 Personal Information</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        Gender = st.selectbox("Gender", ["Male", "Female"])
        Married = st.selectbox("Marital Status", ["Yes", "No"])
        Dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
    with col2:
        Education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
        Self_Employed = st.selectbox("Self-Employed", ["No", "Yes"])
        Property_Area = st.selectbox("Property Area", ["Semiurban", "Urban", "Rural"])

    # --- Section: Financial Details ---
    st.markdown('<p class="section-header">💰 Financial Details</p>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        ApplicantIncome = st.number_input("Applicant Income ($/month)", min_value=0, value=5400, step=100)
        CoapplicantIncome = st.number_input("Co-applicant Income ($/month)", min_value=0.0, value=0.0, step=100.0)
    with col4:
        LoanAmount = st.number_input("Loan Amount (in thousands $)", min_value=0.0, value=128.0, step=1.0)
        Loan_Amount_Term = st.selectbox("Loan Term (in months)", [12, 36, 60, 84, 120, 180, 240, 300, 360, 480],
                                        index=8)

    # --- Section: Credit History ---
    st.markdown('<p class="section-header">📊 Credit History</p>', unsafe_allow_html=True)
    Credit_History = st.selectbox(
        "Do you have a good credit history?",
        ("Yes, all debts have been paid on time.", "No, there are outstanding debts or defaults.")
    )
    credit_history_value = 1 if "Yes" in Credit_History else 0

    st.write("")

    # --- Submit Button ---
    submitted = st.form_submit_button("Check Eligibility")

# --- Prediction Logic ---
if submitted:
    # Prepare user input for the model
    dependents_mapping = {'0': 0, '1': 1, '2': 2, '3+': 3}
    property_area_mapping = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}

    user_input = pd.DataFrame({
        'Gender': [1 if Gender == "Male" else 0],
        'Married': [1 if Married == "Yes" else 0],
        'Dependents': [dependents_mapping[Dependents]],
        'Education': [0 if Education == "Graduate" else 1],
        'Self_Employed': [1 if Self_Employed == "Yes" else 0],
        'ApplicantIncome': [ApplicantIncome],
        'CoapplicantIncome': [CoapplicantIncome],
        'LoanAmount': [LoanAmount],
        'Loan_Amount_Term': [Loan_Amount_Term],
        'Credit_History': [credit_history_value],
        'Property_Area': [property_area_mapping[Property_Area]],
    })

    # Display a spinner while predicting
    with st.spinner('Analyzing your profile...'):
        try:
            prediction = model.predict(user_input)[0]
            probability = model.predict_proba(user_input)[0]

            if prediction == 1:
                prob_value = probability[1]
                st.markdown(f'<div class="prediction approved">✅ Approved! (Confidence: {prob_value:.0%})</div>',
                            unsafe_allow_html=True)
                st.balloons()
                st.success("Congratulations! Your profile meets the criteria for loan approval.", icon="🎉")
            else:
                prob_value = probability[0]
                st.markdown(f'<div class="prediction rejected">❌ Rejected (Confidence: {prob_value:.0%})</div>',
                            unsafe_allow_html=True)
                st.warning(
                    "Your application is likely to be rejected. Common reasons include a low credit score or high debt-to-income ratio.",
                    icon="📉")

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

# --- Footer ---
st.markdown('<div class="footer">Built with Streamlit & ❤️ by Omkar Arora</div>', unsafe_allow_html=True)
