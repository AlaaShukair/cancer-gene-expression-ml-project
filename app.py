import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved files
model = joblib.load("cancer_model.pkl")
scaler = joblib.load("scaler.pkl")
selector = joblib.load("selector.pkl")
label_encoder = joblib.load("label_encoder.pkl")
selected_features = joblib.load("selected_features.pkl")

st.title("Cancer Type Prediction Using Gene Expression Data")

st.write(
    "This web app predicts cancer class based on selected RNA-seq gene expression values."
)

st.info(
    "This app uses selected important genes from the full RNA-seq dataset for demonstration."
)

# Get original feature names from the fitted selector
all_feature_names = selector.feature_names_in_

# User inputs
input_values = {}

for gene in selected_features:
    input_values[gene] = st.number_input(
        f"{gene} expression value",
        value=0.0,
        step=0.1
    )

if st.button("Predict Cancer Class"):

    # Create full feature dataframe with correct original gene names
    full_features = pd.DataFrame(
        np.zeros((1, len(all_feature_names))),
        columns=all_feature_names
    )

    # Add user-entered values
    for gene in selected_features:
        full_features.loc[0, gene] = input_values[gene]

    # Apply feature selection
    selected_input = selector.transform(full_features)

    # Scale input
    scaled_input = scaler.transform(selected_input)

    # Predict
    prediction = model.predict(scaled_input)
    predicted_class = label_encoder.inverse_transform(prediction)

    st.success(f"Predicted Cancer Class: {predicted_class[0]}")
