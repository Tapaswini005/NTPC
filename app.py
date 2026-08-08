import streamlit as st

st.set_page_config(
    page_title="Predictive Maintenance System",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 AI-Based Predictive Maintenance System")

st.markdown("""
Welcome to the Predictive Maintenance System.

### Workflow

1. Upload Dataset
2. Analyze Dataset
3. Train Machine Learning Model
4. Predict Maintenance Status

### Dataset Required
AI4I 2020 Predictive Maintenance Dataset

### Technologies
- Python
- Streamlit
- Scikit-Learn
- Pandas
- Plotly
""")

st.success("Use the left sidebar to navigate through the pages.")