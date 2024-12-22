# Crop Recommendation System

## Overview
The Crop Recommendation System is a desktop application designed to help farmers determine the most suitable crop to grow based on specific environmental and soil conditions.
By leveraging machine learning, the system provides tailored crop suggestions to optimize agricultural productivity.

## Features
- **Machine Learning Model**: Utilizes a K-Nearest Neighbors (KNN) classifier to recommend crops based on user-provided data.
- **User-Friendly Interface**: Built with PySimpleGUI to provide an intuitive and visually appealing interface.
- **Text-to-Speech Integration**: Reads out the recommended crop using the `pyttsx3` library for added accessibility.

## Input Parameters
The application requires the following input parameters:
1. **Nitrogen Content (mg/kg)**
2. **Phosphorus Content (mg/kg)**
3. **Potassium Content (mg/kg)**
4. **Temperature (°C)**
5. **Humidity (%)**
6. **pH Level**
7. **Rainfall (mm)**

## Output
The application predicts and displays the best crop to grow based on the provided inputs. 
It also uses text-to-speech functionality to announce the recommendation.

## Technologies Used
- **Python Libraries**:
  - `pyttsx3`: For text-to-speech functionality.
  - `pandas`: For data handling and preprocessing.
  - `sklearn`: For machine learning (K-Nearest Neighbors model).
  - `numpy`: For numerical computations.
  - `PySimpleGUI`: For building the graphical user interface.
- **Dataset**: An Excel file (`Crop.xlsx`) containing data on crops and their associated environmental and soil parameters.

## Future Enhancements
- Integration with online databases for real-time weather data.
- Support for multiple languages in the text-to-speech feature.
- Improved machine learning model with additional parameters for higher accuracy.

