import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('best_water_quality_model.pkl')

# Set the page title and layout
st.set_page_config(page_title="💧 Water Quality Predictor", layout="centered")
st.title("💧 Water Quality Prediction App")
st.write("Enter the water quality test results below to check if the water is **safe** or **unsafe** for use.")

# Function to collect user inputs
def get_user_input():
    aluminium = st.number_input("Aluminium (mg/L)", min_value=0.0, step=0.03)
    ammonia = st.number_input("Ammonia (mg/L)", min_value=0.0, step=0.04)
    arsenic = st.number_input("Arsenic (mg/L)", min_value=0.0, step=0.03)
    barium = st.number_input("Barium (mg/L)", min_value=0.0, step=0.04)
    cadmium = st.number_input("Cadmium (mg/L)", min_value=0.0, step=0.04)
    chloramine = st.number_input("Chloramine (mg/L)", min_value=0.0, step=0.01)
    chromium = st.number_input("Chromium (mg/L)", min_value=0.0, step=0.01)
    copper = st.number_input("Copper (mg/L)", min_value=0.0, step=0.01)
    flouride = st.number_input("Fluoride (mg/L)", min_value=0.0, step=0.01)
    bacteria = st.number_input("Bacteria (CFU/100mL)", min_value=0.0, step=1.0)
    viruses = st.number_input("Viruses (CFU/100mL)", min_value=0.0, step=1.0)
    lead = st.number_input("Lead (mg/L)", min_value=0.0, step=0.01)
    nitrates = st.number_input("Nitrates (mg/L)", min_value=0.0, step=0.01)
    nitrites = st.number_input("Nitrites (mg/L)", min_value=0.0, step=0.01)
    mercury = st.number_input("Mercury (mg/L)", min_value=0.0, step=0.01)
    perchlorate = st.number_input("Perchlorate (mg/L)", min_value=0.0, step=0.01)
    radium = st.number_input("Radium (pCi/L)", min_value=0.0, step=0.01)
    selenium = st.number_input("Selenium (mg/L)", min_value=0.0, step=0.01)
    silver = st.number_input("Silver (mg/L)", min_value=0.0, step=0.01)
    uranium = st.number_input("Uranium (mg/L)", min_value=0.0, step=0.01)

    # Return input as a DataFrame
    features = pd.DataFrame([{
        'aluminium': aluminium,
        'ammonia': ammonia,
        'arsenic': arsenic,
        'barium': barium,
        'cadmium': cadmium,
        'chloramine': chloramine,
        'chromium': chromium,
        'copper': copper,
        'flouride': flouride,
        'bacteria': bacteria,
        'viruses': viruses,
        'lead': lead,
        'nitrates': nitrates,
        'nitrites': nitrites,
        'mercury': mercury,
        'perchlorate': perchlorate,
        'radium': radium,
        'selenium': selenium,
        'silver': silver,
        'uranium': uranium
    }])

    return features

# Collect input
user_input = get_user_input()

# Predict when button is clicked
if st.button("🔍 Predict Water Safety"):
    prediction = model.predict(user_input)[0]
    prob = model.predict_proba(user_input)[0]

    if prediction == 1:
        st.success(f"✅ The water is **SAFE** to use. (Confidence: {prob[1]*100:.2f}%)")
    else:
        st.error(f"⚠️ The water is **UNSAFE** to use. (Confidence: {prob[0]*100:.2f}%)")
