import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Diabetes Predictor", layout="centered")

with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🩺 Diabetes Prediction App")
st.write("Fill the details to check your diabetes risk.")

pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose", min_value=0, max_value=200)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=140)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100)
insulin = st.number_input("Insulin", min_value=0, max_value=900)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0)
age = st.number_input("Age", min_value=1, max_value=120)

input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                        insulin, bmi, dpf, age]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High chance of diabetes.")
    else:
        st.success("✅ You are unlikely to have diabetes.")
