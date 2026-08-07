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
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Select Target Column")

    target = st.selectbox(
        "Choose Failure/Maintenance Column",
        df.columns
    )

    X = df.drop(columns=[target])
    y = df[target]

    # Convert categorical columns
    le_dict = {}

    for col in X.columns:
        if X[col].dtype == 'object':
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))
            le_dict[col] = le

    if y.dtype == 'object':
        target_encoder = LabelEncoder()
        y = target_encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    st.success(f"Model Accuracy: {accuracy:.2%}")

    st.subheader("Enter Values for Prediction")

    input_data = {}

    for col in X.columns:
        input_data[col] = st.number_input(
            col,
            value=float(X[col].mean())
        )

    if st.button("Predict Maintenance"):

        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)

        if prediction[0] == 1:
            st.error("⚠ Maintenance Required")
        else:
            st.success("✅ Machine Healthy")