import hashlib
import sqlite3
import sys
import re


class URLShortener:
    def __init__(self):
        self.conn = sqlite3.connect('url_shortener.db')
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS url_mappings (
                    short_url TEXT PRIMARY KEY,
                    long_url TEXT
                )
            ''')

    def generate_short_url(self, long_url):
        try:
            if not long_url:
                raise ValueError("URL cannot be empty.")
            hash_object = hashlib.sha512(long_url.encode())
            return hash_object.hexdigest()[:8]
        except Exception as e:
            raise ValueError(f"Error generating short URL: {e}")

    def shorten_url(self, long_url):
        try:
            short_url = self.generate_short_url(long_url)
            with self.conn:
                self.conn.execute('''
                    INSERT INTO url_mappings (short_url, long_url)
                    VALUES (?, ?)
                ''', (short_url, long_url))
            return short_url
        except sqlite3.IntegrityError:
            raise ValueError("Short URL already exists. Try another URL.")
        except Exception as e:
            raise ValueError(f"Error shortening URL: {e}")

    def redirect(self, short_url):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT long_url FROM url_mappings WHERE short_url = ?
            ''', (short_url,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            raise ValueError(f"Error redirecting URL: {e}")


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
                long_url = input("Enter the URL to shorten: ").strip()
                if not re.match(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', long_url):
                    raise ValueError("Invalid URL format. Please enter a valid URL.")
                try:
                    short_url = url_shortener.shorten_url(long_url)
                    print(f"Shortened URL: {short_url}")
                except ValueError as ve:
                    print(ve)

            elif choice == '2':
                short_url = input("Enter the short URL: ").strip()
                try:
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

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        url_shortener.conn.close()


if __name__ == "__main__":
    main()
    sys.exit(0)
