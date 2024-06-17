from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes  # Import hashes module for SHA-256
import os
import binascii
import re
import sys


class AESCipher:
    def __init__(self, password):
        self.password = password.encode('utf-8')
        self.salt = os.urandom(16)  # Generate a random salt

    def encrypt(self, plaintext):
        try:
            # Generate key from password and salt using PBKDF2
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=self.salt,
                iterations=100000,
                backend=default_backend()
            )
            key = kdf.derive(self.password)

            # Pad the plaintext to be a multiple of 16 bytes (AES block size)
            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_plaintext = padder.update(plaintext.encode('utf-8')) + padder.finalize()

            # Generate a random IV (Initialization Vector)
            iv = os.urandom(16)

            # Encrypt the padded plaintext
            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

            # Return salt, iv, and ciphertext as hexadecimal strings
            return (binascii.hexlify(self.salt).decode('utf-8') + binascii.hexlify(iv).decode(
                'utf-8') + binascii.hexlify(ciphertext).decode('utf-8'))

        except (ValueError, TypeError) as e:
            raise RuntimeError(f"Encryption failed: {str(e)}")

    def decrypt(self, encrypted_data_hex):
        try:
            # Split encrypted data into salt, IV, and ciphertext
            salt = binascii.unhexlify(encrypted_data_hex[:32])
            iv = binascii.unhexlify(encrypted_data_hex[32:64])
            ciphertext = binascii.unhexlify(encrypted_data_hex[64:])

            # Generate key from password and salt using PBKDF2
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            key = kdf.derive(self.password)

            # Decrypt the ciphertext
            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

            # Unpad the plaintext
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

            return plaintext.decode('utf-8')

        except (ValueError, TypeError) as e:
            raise RuntimeError(f"Decryption failed: {str(e)}")

def validate_password(password):
    # Regular expression to enforce password constraints:
    # At least 8 characters long, contains at least one lowercase letter,
    # one uppercase letter, one digit, and one special character from !@#$%^&*
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$')
    if not pattern.match(password):
        raise ValueError("Password must be at least 8 characters long and include at least one lowercase letter, "
                         "one uppercase letter, one digit, and one special character from !@#$%^&*")


# Function to get user choice (encryption or decryption)
def get_user_choice():
    while True:
        try:
            choice = int(input("Enter 1 for encryption, 2 for decryption: "))
            if choice not in [1, 2]:
                raise ValueError("Invalid choice. Enter 1 or 2.")
            return choice
        except ValueError as ve:
            print(f"Error: {ve}. Please enter a valid choice (1 or 2).")
            sys.exit(1)


# Example usage:
if __name__ == "__main__":
    try:
        password = input("Enter password for encryption/decryption: ")
        validate_password(password)
        aes_cipher = AESCipher(password)

        plaintext = input("Enter text to encrypt/decrypt: ")
        choice = get_user_choice()

        if choice == 1:
            encrypted_data = aes_cipher.encrypt(plaintext)
            print("Encrypted:", encrypted_data)
        elif choice == 2:
            decrypted_text = aes_cipher.decrypt(plaintext)
            print("Decrypted:", decrypted_text)

        sys.exit(0)

    except (ValueError, RuntimeError, KeyboardInterrupt) as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        sys.exit(1)
