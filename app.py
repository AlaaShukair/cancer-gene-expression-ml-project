
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
    "Note: This app uses selected important genes from the full RNA-seq dataset for demonstration."
)

# Create input fields
input_values = {}

for gene in selected_features:
    input_values[gene] = st.number_input(
        f"{gene} expression value",
        value=0.0,
        step=0.1
    )

# Convert input into dataframe
input_df = pd.DataFrame([input_values])

# Create full feature dataframe with all genes expected by selector
# Missing genes are filled with 0
full_features = pd.DataFrame(
    np.zeros((1, 14572)),
    columns=[f"gene_{i}" for i in range(1, 14573)]
)

# Update selected gene values
for gene in selected_features:
    if gene in full_features.columns:
        full_features[gene] = input_df[gene].values

# Apply feature selection
selected_input = selector.transform(full_features)

# Scale input
scaled_input = scaler.transform(selected_input)

# Prediction
if st.button("Predict Cancer Class"):
    prediction = model.predict(scaled_input)
    predicted_class = label_encoder.inverse_transform(prediction)

    st.success(f"Predicted Cancer Class: {predicted_class[0]}")
