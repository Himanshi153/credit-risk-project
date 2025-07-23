import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("credit_model.pkl")

# Web page title
st.title("💳 Creditworthiness Prediction App")

st.write("Enter the details below to check if the applicant is creditworthy:")

# Input fields
duration = st.number_input("Duration of loan (months)", 1, 72)
credit_amount = st.number_input("Credit Amount", 100, 100000)
checking_acc = st.selectbox("Checking Account Status", [0, 1, 2, 3])
credit_history = st.selectbox("Credit History", [0, 1, 2, 3, 4])
purpose = st.selectbox("Purpose", list(range(10)))
savings = st.selectbox("Savings Account", [0, 1, 2, 3, 4])
employment = st.selectbox("Years Employed", [0, 1, 2, 3, 4])
installment_rate = st.slider("Installment Rate", 1, 4)

# Sample hardcoded inputs (later will be dynamic)
input_data = np.array([[checking_acc, duration, credit_history, purpose, credit_amount,
                        savings, employment, installment_rate, 1, 1, 2, 1, 35, 1,
                        1, 1, 2, 1, 1, 1]])

# Button to predict
if st.button("Predict Creditworthiness"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Applicant is Creditworthy!")
    else:
        st.error("❌ Applicant is NOT Creditworthy.")
