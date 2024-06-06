import string
import secrets
import random
import os
import time
import sys

class ScreenManager:
    def __init__(self):
        self.clear_command = 'cls' if os.name == 'nt' else 'clear'

    def clear_screen(self):
        try:
            os.system(self.clear_command)
        except OSError as e:
            print(f"Error clearing the screen: {e}")
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

class CharacterLake:
    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.special_chars = string.punctuation

    def get_characters(self):
        return self.letters + self.digits + self.special_chars

class PasswordGenerator:
    def __init__(self):
        self.character_lake = CharacterLake()

    def generate_password(self, length, secure=False):
        characters = self.character_lake.get_characters()
        if secure:
            password = ''.join(secrets.choice(characters) for _ in range(length))
        else:
            password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def generate_secure_password(self, length):
        digits = self.character_lake.digits
        special_chars = self.character_lake.special_chars

        while True:
            password = self.generate_password(length, secure=True)
            if (any(char in special_chars for char in password) and sum(char in digits for char in password) >= 5):
                break
        return password

    @staticmethod
    def get_pwd_length():
        try:
            length = input('Password Length: ')
            if length.lower() == "clear":
                ScreenManager().clear_screen()
                main()
            
            if length.lower() == "exit":
                print("Script Terminated...!!")
                time.sleep(2)
                ScreenManager().clear_screen()
                sys.exit(0)
            
            length = int(length)  # Convert to integer after checking for "clear"
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")
        except ValueError as ve:
            if str(ve) != "invalid literal for int() with base 10: 'clear'":
                print("Invalid input:", ve)
            sys.exit(1)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)

        return length

    @staticmethod
    def get_pwd_category():
        try:
            value = input('Password Category (1 for Normal, 2 for Secure): ')
            if value.lower() == "clear":
                ScreenManager().clear_screen()
                main()

            if value.lower() == "exit":
                print("Script Terminated...!!")
                time.sleep(2)
                ScreenManager().clear_screen()
                sys.exit(0)
            
            value = int(value)  # Convert to integer after checking for "clear"
            if value not in [1, 2]:
                raise ValueError("Password category must be either 1 or 2.")
        except ValueError as ve:
            if str(ve) != "invalid literal for int() with base 10: 'clear'":
                print("Invalid input:", ve)
            sys.exit(1)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)

        return value

def main():
    password_generator = PasswordGenerator()

    try:
        if password_generator.get_pwd_category() == 1:
            password = password_generator.generate_password(password_generator.get_pwd_length())
        elif password_generator.get_pwd_category() == 2:
            password = password_generator.generate_secure_password(password_generator.get_pwd_length())
        else:
            raise ValueError("Invalid password category.")
    except ValueError as ve:
        print("Error generating password:", ve)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Process interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
    sys.exit(0)    
