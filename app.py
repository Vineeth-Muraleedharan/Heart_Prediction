<<<<<<< HEAD
import streamlit as st
import joblib
import numpy as np

st.markdown("""
<style>
.stApp {
    background-image: url("https://static.vecteezy.com/system/resources/thumbnails/006/852/869/small/abstract-blue-neon-color-light-effect-horizontal-on-black-background-free-vector.jpg");
    background-size: cover;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
label, .stSlider, .stNumberInput, .stSelectbox {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
.block-container {
    background: rgba(0, 0, 0, 0.5);
    padding: 2rem;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)




# Load the trained model and scaler
heart_model = joblib.load('heart_failure_model.pkl')
heart_scaler = joblib.load('scaler.pkl')


st.title("Heart Failure Prediction App")

st.image("https://www.ultromics.com/hubfs/AdobeStock_707051168-1.jpeg",
         caption="Heart Failure Prediction",
         use_container_width=True)

age = st.slider("Age", 20, 95, 60)
anaemia = st.selectbox("Anaemia", [0, 1])
creatinine = st.number_input("Creatinine Phosphokinase", min_value=0, max_value=10000, value=500)
diabetes = st.radio("Diabetes", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
ejection_fraction = st.number_input("Ejection Fraction", min_value=10, max_value=80, value=30)
hbp = st.radio("High Blood Pressure", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
platelets = st.number_input("Platelets", min_value=0, max_value=1000000, value=250000)
serum_creatinine = st.number_input("Serum Creatinine", min_value=0.0, max_value=20.0, value=1.0)
serum_sodium = st.number_input("Serum Sodium", min_value=100, max_value=150, value=135)
sex = st.radio("Sex", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
smoking = st.selectbox("Smoking", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
time = st.slider("Time (Follow-up period in days)", min_value=0, max_value=300, value=100)

if st.button("Predict"):
    heart_input = np.array([[age, anaemia, creatinine, diabetes, ejection_fraction, hbp, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])
    scaled = heart_scaler.transform(heart_input)
    result = heart_model.predict(scaled)
    if result[0] == 1:
        st.error("Risk of heart failure! Please consult a doctor.")
    else:
        st.success("You are Safe!")

import streamlit as st
import joblib
import numpy as np

# Load the trained model and scaler
heart_model = joblib.load('heart_failure_model.pkl')
heart_scaler = joblib.load('scaler.pkl')


st.title("Heart Failure Prediction App")

age = st.slider("Age", 20, 95, 60)
anaemia = st.selectbox("Anaemia", [0, 1])
creatinine = st.number_input("Creatinine Phosphokinase", min_value=0, max_value=10000, value=500)
diabetes = st.radio("Diabetes", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
ejection_fraction = st.number_input("Ejection Fraction", min_value=10, max_value=80, value=30)
hbp = st.radio("High Blood Pressure", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
platelets = st.number_input("Platelets", min_value=0, max_value=1000000, value=250000)
serum_creatinine = st.number_input("Serum Creatinine", min_value=0.0, max_value=20.0, value=1.0)
serum_sodium = st.number_input("Serum Sodium", min_value=100, max_value=150, value=135)
sex = st.radio("Sex", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
smoking = st.selectbox("Smoking", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
time = st.slider("Time (Follow-up period in days)", min_value=0, max_value=300, value=100)

if st.button("Predict"):
    heart_input = np.array([[age, anaemia, creatinine, diabetes, ejection_fraction, hbp, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])
    scaled = heart_scaler.transform(heart_input)
    result = heart_model.predict(scaled)
    if result[0] == 1:
        st.error("Risk of heart failure! Please consult a doctor.")
    else:
        st.success("You are Safe!")
        

