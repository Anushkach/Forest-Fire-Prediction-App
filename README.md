# Forest Fire Prediction App

This is a simple Streamlit app that predicts whether a forest fire will occur based on input values of temperature, relative humidity, and rain.

## Installation

To run this app, you need to have Python 3.11 installed on your system. You can then install the required Python packages using pip:

```
pip install pandas streamlit
```

## Usage

To run the app, open a terminal or command prompt in the directory where the code is saved, and run the following command:

```
streamlit run forest_fire_app.py
```

This will start the app in your default web browser. You can then enter values for temperature, relative humidity, and rain using the input boxes, and the app will predict whether a forest fire will occur based on those values.

## Code

The code for this app is written in Python, and uses the following libraries:

- `pickle`: for loading the saved machine learning model from a file
- `pandas`: for creating a DataFrame from the input values
- `streamlit`: for creating the web app and input/output boxes

The `binary_classification_model()` function takes the input values as arguments, creates a DataFrame from them, and uses the loaded machine learning model to predict whether a forest fire will occur. The result is then displayed in the output box.
