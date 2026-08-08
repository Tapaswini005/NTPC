import streamlit as st
import pandas as pd

st.set_page_config(page_title="Upload Dataset", page_icon="📂")

st.title("📂 Upload Predictive Maintenance Dataset")

required_columns = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Machine failure"
]

uploaded_file = st.file_uploader(
    "Upload AI4I 2020 Dataset (.csv)",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.session_state["data"] = df

        st.success("Dataset uploaded successfully!")

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        with col3:
            st.metric("Missing Values", df.isnull().sum().sum())

        missing_cols = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing_cols:
            st.error(
                f"Missing Required Columns: {missing_cols}"
            )
        else:
            st.success(
                "All required columns found."
            )

        st.subheader("Column Names")

        st.write(list(df.columns))

    except Exception as e:
        st.error(f"Error loading dataset: {e}")