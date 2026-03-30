import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for modern UI
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Customer Churn Prediction")
st.markdown("Predict whether a customer is likely to churn using ML model.")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👤 Customer Info")

    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Has Partner?", ["Yes", "No"])
    Dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
    tenure = st.number_input("Tenure")

with col2:
    st.markdown("### 📡 Services")

    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.markdown("### 📄 Contract Info")

    Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ])

with col4:
    st.markdown("### 💰 Charges")

    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
    TotalCharges = st.number_input("Total Charges", min_value=0.0, value=1000.0)

# Predict button
if st.button("🔍 Predict Churn"):
    
    payload = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            churn = result["churn_prediction"]
            prob = result["churn_probability"]

            st.markdown("## 📊 Prediction Result")

            if churn == 1:
                st.error(f"⚠️ High Risk of Churn ({prob:.2%})")
            else:
                st.success(f"✅ Low Risk ({prob:.2%})")

            st.progress(prob)

        else:
            st.error("API Error: Unable to get prediction")

    except Exception as e:
        st.error(f"Connection Error: {e}")