import requests
from datetime import datetime
import re


class WeatherForecast:
    API_KEY = 'YOUR_API_KEY'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast'

    def __init__(self):
        self.location = None

    def get_weather(self, city):
        try:
            params = {
                'q': city,
                'appid': self.API_KEY,
                'units': 'metric'
            }
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            self.location = data.get('name')
            if self.location:
                current_weather = {
                    'Temperature': data['main']['temp'],
                    'Humidity': data['main']['humidity'],
                    'Wind Speed': data['wind']['speed'],
                    'Description': data['weather'][0]['description']
                }
                self.display_current_weather(current_weather)
            else:
                print('Location not found. Please enter a valid city name.')
        except requests.exceptions.RequestException as e:
            print(f'Failed to fetch data: {e}')
        except KeyError as e:
            print(f'Invalid data format: {e}')

    def get_forecast(self, city):
        try:
            params = {
                'q': city,
                'appid': self.API_KEY,
                'units': 'metric'
            }
            response = requests.get(self.FORECAST_URL, params=params)
            response.raise_for_status()
            data = response.json()
            forecast = []
            for item in data['list']:
                forecast.append({
                    'Date': datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d'),
                    'Temperature High': item['main']['temp_max'],
                    'Temperature Low': item['main']['temp_min'],
                    'Description': item['weather'][0]['description']
                })
            self.display_forecast(forecast)
        except requests.exceptions.RequestException as e:
            print(f'Failed to fetch forecast data: {e}')
        except KeyError as e:
            print(f'Invalid data format: {e}')

    def display_current_weather(self, current_weather):
        print(f'Current Weather in {self.location}:')
        for key, value in current_weather.items():
            print(f'{key}: {value}')
        print()

    def display_forecast(self, forecast):
        print(f'Weather Forecast for {self.location} (Next 5 Days):')
        for item in forecast:
            print(f"Date: {item['Date']}")
            print(f"Temperature High: {item['Temperature High']}")
            print(f"Temperature Low: {item['Temperature Low']}")
            print(f"Weather: {item['Description']}")
            print()


class InputValidator:
    @staticmethod
    def validate_city(city):
        pattern = r'^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$'
        return re.match(pattern, city)


def main():
    try:
        weather_forecast = WeatherForecast()
        while True:
            city = input("Enter a city name: ").strip()
            if InputValidator.validate_city(city):
                weather_forecast.get_weather(city)
                weather_forecast.get_forecast(city)
                break
            else:
                print("Invalid city name. Please enter a valid city name.")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt: Exiting Weather Forecast App.")
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


if __name__ == "__main__":
    main()
