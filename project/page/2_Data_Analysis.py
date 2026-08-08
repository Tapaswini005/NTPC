import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Data Analysis Dashboard")

if "data" not in st.session_state:
    st.warning("Please upload dataset first.")
    st.stop()

df = st.session_state["data"]

st.subheader("Dataset Statistics")

st.dataframe(df.describe())

st.subheader("Machine Failure Distribution")

failure_counts = df["Machine failure"].value_counts()

fig = px.pie(
    values=failure_counts.values,
    names=["Healthy", "Failure"],
    title="Failure Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Feature Correlation")

numeric_df = df[
    [
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]",
        "Machine failure"
    ]
]

corr = numeric_df.corr()

heatmap = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Correlation Heatmap"
)

st.plotly_chart(
    heatmap,
    use_container_width=True
)

st.subheader("Feature Statistics")

st.dataframe(
    numeric_df.describe().T
)