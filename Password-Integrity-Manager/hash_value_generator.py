import hashlib
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

class ChecksumPWD:
    def __init__(self, password, hashing_algorithm):
        self.usr_password = password
        self.select_algorithm = hashing_algorithm.lower()

    def passwordHashing(self):
        try:
            hash_value = hashlib.new(self.select_algorithm, self.usr_password.encode()).hexdigest()
            print(f'Your Password : {self.usr_password}\nHashing Value : {hash_value}')
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)
        
def get_usr_password():
    while True:
        user_pwd = input('User Password : ')

        if user_pwd.lower() == "clear":
            ScreenManager().clear_screen()
            main()

        if user_pwd.lower() == "exit":
            print("Script Terminated...!!")
            time.sleep(2)
            ScreenManager().clear_screen()
            sys.exit(0)

        if user_pwd:
            return user_pwd
        elif user_pwd is None:
            print('Password is required...!!')
        else:
            print('Password is invalid...!!')

def get_checksum_method():
    while True:
        method = input('Checksum Method (sha1, sha224, sha256, sha384, sha512, md5): ')

        if method.lower() == "clear":
            ScreenManager().clear_screen()
            main()

        if method.lower() == "exit":
            print("Script Terminated...!!")
            time.sleep(2)
            ScreenManager().clear_screen()
            sys.exit(0)

        if method.lower() in hashlib.algorithms_guaranteed:
            return method
        elif method is None:
            print('Checksum method required...!!')
        else:
            print('Checksum method invalid...!!')

def main():
    usr_password = get_usr_password()
    checksum_method = get_checksum_method()

    checksum_generator = ChecksumPWD(usr_password, checksum_method)
    checksum_generator.passwordHashing()

if __name__ == "__main__":
    main()
    sys.exit(0)
