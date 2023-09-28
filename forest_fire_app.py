# Importing necessary libraries
import joblib
import pandas as pd
import streamlit as st

# Setting background image for the Streamlit app
background_image_url = "https://th.bing.com/th/id/R.ab88afce853a08a61f0854eca4b7b2be?rik=a18WPVKPT4s9VA&riu=http%3a%2f%2fmediad.publicbroadcasting.net%2fp%2fshared%2fnpr%2fstyles%2fx_large%2fnprshared%2f201507%2f421997154.jpg&ehk=PhtaV5VzC3B%2bW7pQ7%2bIi2fbV%2flF5EQ1gUU9g4tM5wG4%3d&risl=&pid=ImgRaw&r=0"
page_bg_img = f'''
<style>
.stApp {{
    background-image: url("{background_image_url}");
    background-size: cover;
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Creating a container for the Streamlit app
with st.container():
    # Loading the pre-trained model
    model = joblib.load('model.joblib')

    # Setting the title for the Streamlit app
    st.markdown("<h1 style='color: brown;'>Forest Fire Prediction App</h1>", unsafe_allow_html=True)

    # Taking user input for temperature
    st.markdown("<h3 style='font-size: 20px; font-weight:bold; color:white;'>Temperature</h3>", unsafe_allow_html=True)
    temperature = st.number_input("Celsius", step=1.0, placeholder='Please Enter a value', min_value=0.0, value=None)
    
    # Taking user input for relative humidity
    st.markdown("<h3 style='font-size: 20px; font-weight:bold; color:white;'>Relative Humidity</h3>", unsafe_allow_html=True)
    rh = st.number_input("Percentage", step=1.0, placeholder='Please Enter a value', min_value=0.0, value=None)

    # Taking user input for rainfall
    st.markdown("<h3 style='font-size: 20px; font-weight:bold; color:white;'>Rainfall</h3>", unsafe_allow_html=True)
    rain = st.number_input("Milimeter", step=0.1, placeholder='Please Enter a value', min_value=0.0, value=None)

    # Defining a function for binary classification model
    def binary_classification_model(temperature, relative_humidity, rain):
        """
        Predicts the occurrence of a forest fire based on the input parameters.

        Args:
        temperature (float): The temperature in Celsius.
        relative_humidity (float): The relative humidity in percentage.
        rain (float): The amount of rain in mm/m2.

        Returns:
        str: A string indicating whether a fire is likely to occur or not.

        This function takes in three inputs: temperature, relative humidity, and rain. It uses these inputs to predict whether a forest fire is likely to occur or not. If the prediction is that a fire is likely to occur, the function returns the string "Alert! Fire can occur". If the prediction is that a fire is not likely to occur, the function returns the string "Safe! Fire will not occur".
        """
        # Creating a dataframe with user input
        input_data = pd.DataFrame({'Temperature': [temperature], ' RH': [relative_humidity], 'Rain': [rain]})
        # Predicting the output using the pre-trained model
        prediction = model.predict(input_data)
        # Returning the output as a string
        if prediction == 1:
            return "Alert! Fire can occur"
        elif prediction == 0:
            return "Safe! Fire will not occur"

    # Creating a button to predict the output
    if st.button("Predict"):
        # Calling the binary_classification_model function with user input
        output = binary_classification_model(temperature, rh, rain)
        # Displaying the output as a heading
        st.markdown(f"<h2 style='color: blue; font-size: 24px;      text-shadow:0 0 5px #ff0000,0 0 10px #ff0000,0 0 15px #ff0000,0 0 20px #ff0000'>{output}</h2>", unsafe_allow_html=True)
