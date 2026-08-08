import streamlit as st
import pandas as pd
import joblib
import os

st.title("🔍 Maintenance Prediction")

model_path = "models/maintenance_model.pkl"

if not os.path.exists(model_path):
    st.warning(
        "Train the model first."
    )
    st.stop()

model = joblib.load(model_path)

air_temp = st.number_input(
    "Air Temperature [K]",
    value=300.0
)

process_temp = st.number_input(
    "Process Temperature [K]",
    value=310.0
)

rpm = st.number_input(
    "Rotational Speed [rpm]",
    value=1500
)

torque = st.number_input(
    "Torque [Nm]",
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear [min]",
    value=100
)

if st.button("Predict"):

    input_df = pd.DataFrame(
        [[
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear
        ]],
        columns=[
            "Air temperature [K]",
            "Process temperature [K]",
            "Rotational speed [rpm]",
            "Torque [Nm]",
            "Tool wear [min]"
        ]
    )

    probability = (
        model.predict_proba(input_df)[0][1]
    )

    st.subheader(
        f"Failure Probability: {probability:.2%}"
    )

    if probability < 0.30:
        st.success(
            "✅ Healthy"
        )

    elif probability < 0.70:
        st.warning(
            "⚠️ Warning"
        )

    else:
        st.error(
            "🔴 Maintenance Required"
        )