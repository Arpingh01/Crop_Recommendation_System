import pyttsx3
import pandas as pd
from sklearn import preprocessing

from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import PySimpleGUI as sg

# Load the Excel file
excel = pd.read_excel('Crop.xlsx', header=0)
print(excel)
print(excel.shape)

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Encode crop labels
le = preprocessing.LabelEncoder()
crop = le.fit_transform(list(excel["CROP"]))

# Extract features
NITROGEN = list(excel["NITROGEN"])
PHOSPHORUS = list(excel["PHOSPHORUS"])
POTASSIUM = list(excel["POTASSIUM"])
TEMPERATURE = list(excel["TEMPERATURE"])
HUMIDITY = list(excel["HUMIDITY"])
PH = list(excel["PH"])
RAINFALL = list(excel["RAINFALL"])

# Prepare feature array
features = np.array(list(zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL)))

# Train the model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(features, crop)

# Set up the GUI layout
layout = [
    [sg.Text('Crop Recommendation System', font=("Helvetica", 30), text_color='yellow')],
    [sg.Text('Please enter the following details:', font=("Helvetica", 20))],
    [sg.Text('Nitrogen:', font=("Helvetica", 20)), sg.Input(size=(20, 1))],
    [sg.Text('Phosphorous:', font=("Helvetica", 20)), sg.Input(size=(20, 1))],
    [sg.Text('Potassium:', font=("Helvetica", 20)), sg.Input(size=(20, 1))],
    [sg.Text('Temperature (°C):', font=("Helvetica", 20)), sg.Input(size=(20, 1))],
    [sg.Text('Humidity (%):', font=("Helvetica", 20)), sg.Input(size=(20, 1))],
    [sg.Text('pH:', font=("Helvetica", 20)), sg.Input(size=(20, 1))],
    [sg.Text('Rainfall (mm):', font=("Helvetica", 20)), sg.Input(size=(20, 1))],
    [sg.Text(size=(50, 1), font=("Helvetica", 20), text_color='yellow', key='-OUTPUT1-')],
    [sg.Button('Submit', font=("Helvetica", 20)), sg.Button('Quit', font=("Helvetica", 20))]
]

window = sg.Window('Crop Recommendation System', layout)

# Main event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # Convert inputs to float
    nitrogen_content = float(values[0])
    phosphorus_content = float(values[1])
    potassium_content = float(values[2])
    temperature_content = float(values[3])
    humidity_content = float(values[4])
    ph_content = float(values[5])
    rainfall = float(values[6])

    # Prepare prediction input
    predict1 = np.array([
        nitrogen_content, phosphorus_content, potassium_content,
        temperature_content, humidity_content, ph_content, rainfall
    ]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(predict1)
    crop_name = le.inverse_transform(prediction)[0]

    # Output results
    window['-OUTPUT1-'].update(f'The best crop that you can grow: {crop_name}')
    speak(f"The best crop that you can grow is {crop_name}")

window.close()