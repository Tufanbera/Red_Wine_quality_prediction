import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Wine Quality Predictor",
    page_icon="🍷",
    layout="centered"
)

# load model
model = joblib.load("xgb_final_pipeline.pkl")
st.title("🍷 Wine Quality Prediction")
st.divider()

# Session state for autofill
if "auto_fill" not in st.session_state:
    st.session_state.auto_fill = False

if st.button("🔁 Autofill Example (Good Wine)"):
    st.session_state.auto_fill = True

# Default values
defaults = {
    "fixed acidity": 8.8,
    "volatile acidity": 0.37,
    "citric acid": 0.40,
    "residual sugar": 2.26,
    "chlorides": 0.073,
    "free sulfur dioxide": 11.7,
    "total sulfur dioxide": 27.0,
    "density": 0.9957,
    "pH": 3.28,
    "sulphates": 0.75,
    "alcohol": 11.65
}

# Input layout
st.subheader("🔬 Wine Chemical Properties")

col1, col2 = st.columns(2)

with col1:
    fixed_acidity = st.number_input(
        "Fixed Acidity",
        value=defaults["fixed acidity"] if st.session_state.auto_fill else 7.0,
        step=0.1
    )

    volatile_acidity = st.slider(
        "Volatile Acidity",
        0.1, 1.6,
        defaults["volatile acidity"] if st.session_state.auto_fill else 0.5
    )

    citric_acid = st.slider(
        "Citric Acid",
        0.0, 1.0,
        defaults["citric acid"] if st.session_state.auto_fill else 0.3
    )

    residual_sugar = st.number_input(
        "Residual Sugar",
        value=defaults["residual sugar"] if st.session_state.auto_fill else 2.0,
        step=0.1
    )

    chlorides = st.slider(
        "Chlorides",
        0.01, 0.2,
        defaults["chlorides"] if st.session_state.auto_fill else 0.08
    )

with col2:
    free_sulfur = st.number_input(
        "Free Sulfur Dioxide",
        value=defaults["free sulfur dioxide"] if st.session_state.auto_fill else 15.0,
        step=1.0
    )

    total_sulfur = st.number_input(
        "Total Sulfur Dioxide",
        value=defaults["total sulfur dioxide"] if st.session_state.auto_fill else 45.0,
        step=1.0
    )

    density = st.slider(
        "Density",
        0.990, 1.005,
        defaults["density"] if st.session_state.auto_fill else 0.996
    )

    pH = st.slider(
        "pH",
        2.8, 4.0,
        defaults["pH"] if st.session_state.auto_fill else 3.3
    )

    sulphates = st.slider(
        "Sulphates",
        0.3, 2.0,
        defaults["sulphates"] if st.session_state.auto_fill else 0.6
    )

alcohol = st.slider(
    "Alcohol (%)",
    8.0, 15.0,
    defaults["alcohol"] if st.session_state.auto_fill else 10.0
)

# Prepare input dataframe

input_df = pd.DataFrame([[
    fixed_acidity, volatile_acidity, citric_acid,
    residual_sugar, chlorides, free_sulfur,
    total_sulfur, density, pH,
    sulphates, alcohol
]], columns=[
    "fixed acidity", "volatile acidity", "citric acid",
    "residual sugar", "chlorides", "free sulfur dioxide",
    "total sulfur dioxide", "density", "pH",
    "sulphates", "alcohol"
])

input_df = input_df[model.feature_names_in_]

# Prediction

st.divider()

if st.button("🔍 Predict Wine Quality", use_container_width=True):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.success("🍷 **Good Quality Wine**")
    else:
        st.error("❌ **Bad Quality Wine**")
