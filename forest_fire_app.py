import joblib
import pandas as pd
import streamlit as st

# Load the saved model from the file
# Load the model using joblib
model = joblib.load('model.joblib')


# Input boxes
st.title("Forest Fire Prediction App")

temperature = st.number_input(label="Temperature",step=1)
rh = st.number_input(label="RH",step=1)
rain = st.number_input(label="Rain",step=0.1)



# Dummy binary classification model output
def binary_classification_model(temperature, relative_humidity, rain):

    # Waiting for input
    if temperature==0 and relative_humidity==0 and rain==0:
        return "None. (Please Enter Input Data)"
    else:
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
