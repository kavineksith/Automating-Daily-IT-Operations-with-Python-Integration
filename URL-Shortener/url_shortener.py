import hashlib
import sys

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def generate_short_url(self, long_url):
        try:
            hash_object = hashlib.sha256(long_url.encode())
            short_url = hash_object.hexdigest()[:8]  # Using first 8 characters of the hash as short URL
            return short_url
        except Exception as e:
            raise ValueError("Error occurred while generating short URL.") from e

    def shorten_url(self, long_url):
        try:
            short_url = self.generate_short_url(long_url)
            self.url_mapping[short_url] = long_url
            return short_url
        except Exception as e:
            raise ValueError("Error occurred while shortening URL.") from e

    def redirect(self, short_url):
        try:
            return self.url_mapping.get(short_url, None)
        except Exception as e:
            raise ValueError("Error occurred while redirecting URL.") from e

def main():
    url_shortener = URLShortener()

    try:
        while True:
            print("\nURL Shortener")
            print("1. Shorten URL")
            print("2. Redirect URL")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    long_url = input("Enter the URL to shorten: ")
                    short_url = url_shortener.shorten_url(long_url)
                    print(f"Shortened URL: {short_url}")
                except ValueError as ve:
                    print(ve)
            elif choice == '2':
                try:
                    short_url = input("Enter the short URL: ")
                    long_url = url_shortener.redirect(short_url)
                    if long_url:
                        print(f"Redirecting to: {long_url}")
                    else:
                        print("Error: Invalid short URL.")
                except ValueError as ve:
                    print(ve)
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Error: Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 3.")
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    sys.exit(0)

