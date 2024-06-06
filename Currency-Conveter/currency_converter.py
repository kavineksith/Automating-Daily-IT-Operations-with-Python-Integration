import os
import sys
import requests

API_KEY = os.environ.get('OPEN_EXCHANGE_API_KEY')

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_currency = None
        self.target_currency = None

    def fetch_exchange_rate(self):
        try:
            url = f'https://open.er-api.com/v6/latest/{self.base_currency}'
            response = requests.get(url)
            data = response.json()
            if 'rates' in data:
                return data['rates'].get(self.target_currency)
            else:
                raise ValueError("Error: Unable to fetch exchange rate.")
        except requests.exceptions.RequestException as e:
            raise ConnectionError("Error: Unable to connect to exchange rate API.") from e
        except ValueError as ve:
            raise ValueError(ve)
    
    def convert_currency(self, amount):
        try:
            rate = self.fetch_exchange_rate()
            converted_amount = amount * rate
            return converted_amount
        except (ValueError, KeyError) as e:
            raise ValueError("Error: Unable to perform currency conversion.") from e

    def set_base_currency(self, base_currency):
        self.base_currency = base_currency.upper()

    def set_target_currency(self, target_currency):
        self.target_currency = target_currency.upper()

def main():
    try:
        print("Welcome to Currency Converter!")
        if API_KEY is None:
            raise ValueError("Error: API key not found. Please set the OPEN_EXCHANGE_API_KEY environment variable.")
        converter = CurrencyConverter(API_KEY)

        base_currency = input("Enter base currency (e.g., USD): ")
        converter.set_base_currency(base_currency)

        target_currency = input("Enter target currency (e.g., EUR): ")
        converter.set_target_currency(target_currency)

        amount = float(input("Enter amount: "))

        converted_amount = converter.convert_currency(amount)
        print(f"{amount} {converter.base_currency} equals {converted_amount:.2f} {converter.target_currency}")
    except KeyboardInterrupt:
        print("\nCurrency conversion interrupted by the user.")
        sys.exit(1)
    except ValueError as ve:
        print(ve)
    except ConnectionError as ce:
        print(ce)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    sys.exit(0)

    
