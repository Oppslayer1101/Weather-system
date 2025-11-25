# Weather Predictor (AIML Project)

## Overview
The Weather Predictor is a simple Python-based Machine Learning project that forecasts temperature based on humidity and air pressure. It uses a CSV dataset and a Linear Regression model to learn patterns from historical data. The project is lightweight, easy to understand, and ideal for AIML coursework.

## Features
- Loads weather data from a CSV file
- Uses Linear Regression for prediction
- Takes humidity and pressure as user input
- Predicts the expected temperature
- Includes basic input validation
- Uses minimal external libraries

## Technologies Used
- Python 3
- scikit-learn
- numpy
- csv (built-in)

## How It Works
1. The program loads the dataset (`weather_data.csv`).
2. Humidity and pressure are used as input features.
3. Temperature is used as the prediction target.
4. The Linear Regression model is trained on this data.
5. The user enters humidity and pressure values.
6. The model outputs the predicted temperature.

## Description
This project demonstrates basic AIML concepts like supervised learning, regression, data preprocessing, and prediction. It also shows Python concepts such as classes, exception handling, and file interaction. It is simple, beginner-friendly, and suitable for academic submission.

## Future Improvements
- Use more features (wind, rainfall, clouds)
- Add model comparison (Random Forest, SVR)
- Visualize predictions using matplotlib
- Add real-time weather API integration
