
import streamlit as st
import pandas as pd
import joblib

# Load saved files
model = joblib.load("cancer_model.pkl")
scaler = joblib.load("scaler.pkl")
selector = joblib.load("selector.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("Cancer Type Prediction Using Gene Expression Data")

st.write(
    "Upload a CSV file containing gene expression values to predict the cancer class."
)

st.info(
    "The uploaded file should contain the same gene columns used during model training."
)

# Get expected feature names
expected_features = list(selector.feature_names_in_)

uploaded_file = st.file_uploader(
    "Upload gene expression CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    input_df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data Preview")
    st.dataframe(input_df.head())

    # Remove Id column if present
    if "Id" in input_df.columns:
        input_df = input_df.drop(columns=["Id"])

    # Check missing columns
    missing_cols = [
        col for col in expected_features
        if col not in input_df.columns
    ]

    if len(missing_cols) > 0:

        st.error(
            "The uploaded file is missing some required gene columns."
        )

        st.write(
            "Example missing columns:",
            missing_cols[:10]
        )

    else:

        # Arrange columns correctly
        input_df = input_df[expected_features]

        # Apply feature selection
        selected_input = selector.transform(input_df)

        # Scale input
        scaled_input = scaler.transform(selected_input)

        # Predict
        prediction = model.predict(scaled_input)

        predicted_class = label_encoder.inverse_transform(prediction)

        st.subheader("Prediction Result")

        st.success(
            f"Predicted Cancer Class: {predicted_class[0]}"
        )
