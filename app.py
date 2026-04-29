import streamlit as st
import pickle
import pandas as pd

# Load saved model
model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Churn Prediction System")

st.write("Enter Customer Details")

Age = st.number_input("Age")
FrequentFlyer = st.number_input("Frequent Flyer (0 or 1)")
AnnualIncomeClass = st.number_input("Annual Income Class")
ServicesOpted = st.number_input("Services Opted")
AccountSyncedToSocialMedia = st.number_input("Account Synced To Social Media (0 or 1)")
BookedHotelOrNot = st.number_input("Booked Hotel Or Not (0 or 1)")

input_data = pd.DataFrame([[Age, FrequentFlyer, AnnualIncomeClass,
                            ServicesOpted, AccountSyncedToSocialMedia,
                            BookedHotelOrNot]])

if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer Will Churn")
    else:
        st.success("Customer Will Stay")