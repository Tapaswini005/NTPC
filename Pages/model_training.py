import streamlit as st
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

st.title("🤖 Model Training")

if "data" not in st.session_state:
    st.warning("Please upload dataset first.")
    st.stop()

df = st.session_state["data"]

features = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

target = "Machine failure"

X = df[features]
y = df[target]

if st.button("Train Model"):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    st.success("Model Trained Successfully")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Accuracy",
            f"{accuracy:.2%}"
        )

        st.metric(
            "Precision",
            f"{precision:.2%}"
        )

    with c2:
        st.metric(
            "Recall",
            f"{recall:.2%}"
        )

        st.metric(
            "F1 Score",
            f"{f1:.2%}"
        )

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    st.subheader("Confusion Matrix")
    st.write(cm)

    joblib.dump(
        model,
        "models/maintenance_model.pkl"
    )

    st.success(
        "Model saved successfully."
    )