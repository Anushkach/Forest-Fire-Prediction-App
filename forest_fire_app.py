import joblib
import pandas as pd
import streamlit as st

# Load the saved model from the file
# Load the model using joblib
model = joblib.load('model.joblib')


# Input boxes
st.title("Forest Fire Prediction App")

temperature = st.number_input("Temperature")
rh = st.number_input("RH")
rain = st.number_input("Rain")



# Dummy binary classification model output
def binary_classification_model(temperature, relative_humidity, rain):

    #Add input values to a pandas DataFrame
    input_data = pd.DataFrame({'Temperature': [temperature], ' RH': [relative_humidity], 'Rain': [rain]})
    # Make predictions using the model
    prediction = model.predict(input_data)
    if prediction == 1:
        return "fire"
    elif prediction == 0:
        return "not fire"

# Output box

output = binary_classification_model(temperature, rh, rain)
st.markdown(f"<h2 style='color: red; font-size: 24px;'>The result is: {output}</h2>", unsafe_allow_html=True)

# print(binary_classification_model(temperature, relative_humidity, rain))
