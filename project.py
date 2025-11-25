import csv
import numpy as np
from sklearn.linear_model import LinearRegression

class WeatherSystem:
    def __init__(self, file_name):
        self.file_name = file_name
        self.all_input_data = []
        self.all_output_data = []
        self.weather_model = LinearRegression()

    def load_weather_file(self):
        print("Trying to load the dataset...")

        try:
            file = open(self.file_name, "r")
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                # Taking humidity and pressure as inputs
                h = float(row["humidity"])
                p = float(row["pressure"])
                temp = float(row["temp"])

                # Appending to lists
                self.all_input_data.append([h, p])
                self.all_output_data.append(temp)

            file.close()

            # Converting to numpy arrays (required by sklearn)
            self.all_input_data = np.array(self.all_input_data)
            self.all_output_data = np.array(self.all_output_data)

            print("Weather data loaded successfully.\n")

        except Exception as e:
            print("Something went wrong while reading the file:", e)

    def train_weather_model(self):
        print("Training machine learning model...")

        try:
            # Train using Linear Regression
            self.weather_model.fit(self.all_input_data, self.all_output_data)
            print("Model trained! It should work now.\n")
        except Exception as e:
            print("Model training failed:", e)

    def predict_temp(self, humi, press):
        # Predicting the temperature for given values
        try:
            result = self.weather_model.predict([[humi, press]])
            return result[0]
        except:
            print("Could not predict due to wrong inputs.")
            return None


def main():
    # Create object of weather system
    ws = WeatherSystem("weather_data.csv")

    # Load data
    ws.load_weather_file()

    # Train model
    ws.train_weather_model()

    print("---------- Weather Predictor ----------")
    try:
        hum_input = input("Enter humidity (%): ")
        press_input = input("Enter pressure (hPa): ")

        hum_input = float(hum_input)
        press_input = float(press_input)

        predicted = ws.predict_temp(hum_input, press_input)

        if predicted is not None:
            print("\nBased on these values, the temperature is expected to be around:")
            print(f"{predicted:.2f} °C")
        else:
            print("Could not get prediction.")

    except:
        print("Invalid entry. Please enter numeric values only.")

    print("\nThank you for using the Weather Predictor!")


if __name__ == "__main__":
    main()