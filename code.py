import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Predictive Maintenance System")

st.title("🔧 Predictive Maintenance System")
st.write("Upload your maintenance dataset and predict machine failures.")

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)