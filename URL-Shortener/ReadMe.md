## Documentation : URL Shortener 

### Overview
The URL Shortener script provides a command-line interface for shortening URLs using a hashing algorithm and maintaining a mapping between the original long URLs and their corresponding shortened versions. It also allows users to redirect from a shortened URL back to the original long URL.

### Requirements
- Python 3.x

### Usage
1. Ensure Python is installed on your system.
2. Run the script and follow the menu prompts to perform URL shortening and redirection operations.
3. Provide input as requested for each operation.

### Implementation Details
#### Class: `URLShortener`
- Methods:
  - `__init__(self)`: Initializes the URLShortener object with an empty URL mapping dictionary.
  - `generate_short_url(self, long_url)`: Generates a short URL by hashing the long URL and using the first 8 characters of the hash.
  - `shorten_url(self, long_url)`: Shortens a long URL by generating a short URL and adding it to the URL mapping dictionary.
  - `redirect(self, short_url)`: Redirects from a short URL to the corresponding long URL using the URL mapping dictionary.

#### Function: `main()`
- Provides a user-friendly interface for interacting with the URL Shortener.
- Presents a menu with options for shortening and redirecting URLs.
- Handles user input and calls corresponding methods of `URLShortener`.
- Gracefully handles exceptions and interrupts.

### Conclusion
This script simplifies URL shortening and redirection through a command-line interface, providing a convenient way to create shorter versions of long URLs for sharing or embedding in messages. By utilizing a hashing algorithm, it ensures that each long URL is consistently mapped to the same short URL, enabling reliable redirection. With its intuitive menu system, users can easily interact with the URL Shortener without needing a separate application.

Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.