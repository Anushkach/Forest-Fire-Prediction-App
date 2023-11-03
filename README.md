# Forest Fire Prediction App

The primary goal of this project was to develop a web application that displays weather information for user-specified locations and provides predictive analysis to assess the likelihood of fire incidents. To predict forest fires, we collected data on rainfall, relative humidity, and temperature, taking into account their availability and importance in the predictive modeling process. We implemented an ensemble machine learning model to improve performance by incorporating the most effective algorithms from the dataset and using a voting classifier. The web application predicts the occurrence of a forest fire based on user input for temperature, relative humidity, and rainfall, utilizing a pre-trained binary classification model.

## Installation

To run this app, you need to have Python 3.x installed on your system. You can then install the required Python packages using pip:

```
pip install -r requirements.txt
```

## Usage

To run the app in a local environment, open a terminal or command prompt in the directory where the code is saved, and run the following command:

```
streamlit run forest_fire_app.py
```

This will start the app in your default web browser. You can then enter values for temperature, relative humidity, and rain using the input boxes, and the app will predict whether a forest fire will occur based on those values.

You can also run this app from streamlit community cloud.  
https://forest-fire-prediction-app.streamlit.app/

## Code

The code for this app is written in Python, and uses the following libraries:

- `joblib`: for loading the saved machine learning model from a file
- `pandas`: for creating a DataFrame from the input values
- `streamlit`: for creating the web app and input/output boxes

The `binary_classification_model()` function takes the input values as arguments, creates a DataFrame from them, and uses the loaded machine learning model to predict whether a forest fire will occur. The result is then displayed in the output box.

## Files

- `forest_fire_app.py`: the main Python script that runs the Streamlit app
- `model.joblib`: the saved machine learning model used by the app
- `requirements.txt`: a list of required Python packages and their versions

## Contact
If you have any questions or concerns, please contact me at anushkachathuranga1998@gmail.com

