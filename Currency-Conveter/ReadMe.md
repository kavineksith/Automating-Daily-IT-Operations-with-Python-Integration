## Documentation : Currency Converter 

### Overview
This Python script provides a simple command-line interface for converting currencies using the Open Exchange Rates API. Users can specify the base currency, target currency, and amount to convert. The script fetches the latest exchange rates from the API and performs the currency conversion.

### Requirements
- Python 3.x
- `requests` library (`pip install requests`)

### Usage
1. Install the required library using `pip install requests`.
2. Set up an account with Open Exchange Rates to obtain an API key.
3. Set the `OPEN_EXCHANGE_API_KEY` environment variable with your API key.
4. Run the script and follow the prompts to perform currency conversion.

### Implementation Details
#### Constants
- `API_KEY`: Environment variable containing the API key for Open Exchange Rates.

#### Class: `CurrencyConverter`
- Methods:
  - `__init__(self, api_key)`: Initializes the CurrencyConverter object with the API key.
  - `fetch_exchange_rate(self)`: Fetches the latest exchange rate from the API based on the specified base and target currencies.
  - `convert_currency(self, amount)`: Converts the specified amount from the base currency to the target currency using the fetched exchange rate.
  - `set_base_currency(self, base_currency)`: Sets the base currency for conversion.
  - `set_target_currency(self, target_currency)`: Sets the target currency for conversion.

#### Function: `main()`
- Provides a user-friendly interface for performing currency conversion.
- Prompts the user to enter the base currency, target currency, and amount.
- Calls the `convert_currency` method to perform the conversion and displays the result.

### Conclusion
This script provides a convenient way to convert currencies using real-time exchange rates from the Open Exchange Rates API. It offers flexibility in specifying the base and target currencies, making it suitable for various currency conversion needs. With its simple command-line interface, users can quickly perform currency conversions without the need for complex setups.

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.