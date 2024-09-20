import streamlit as st
import pandas as pd
import pickle

# Load the saved model
filename = 'rf_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a title for the app
st.title("Marketing Campaign Response Prediction")

# Create input fields for the user
# Replace these with the actual features from your dataset
age = st.number_input("Age", min_value=18, max_value=100, value=30)
education = st.selectbox("Education", ["Basic", "Graduation", "Master", "PhD"])
income = st.number_input("Income", min_value=0, value=50000)
# Add more input fields for other features

# Create a button to make predictions
if st.button("Predict"):
  # Create a DataFrame with the user input
  input_data = pd.DataFrame({
      "Age": [age],
      "Education": [education],
      "Income": [income],
      # Add more columns for other features
  })

  # Preprocess the input data if needed (e.g., one-hot encoding)

  # Make predictions using the loaded model
  prediction = loaded_model.predict(input_data)[0]

  # Display the prediction
  if prediction == 1:
    st.success("The customer is likely to respond to the campaign.")
  else:
    st.warning("The customer is likely not to respond to the campaign.")
