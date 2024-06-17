import re
import sys


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def validate_input(self, text):
        # Regular expression to match printable ASCII characters (32 to 126)
        pattern = re.compile(r'^[ -~]+$')
        return pattern.match(text) is not None

    def encrypt(self, plaintext):
        if not self.validate_input(plaintext):
            raise ValueError("Input contains non-printable ASCII characters.")

        encrypted_text = []
        for char in plaintext:
            encrypted_char = chr((ord(char) - 32 + self.shift) % 95 + 32)
            encrypted_text.append(encrypted_char)
        return ''.join(encrypted_text)

    def decrypt(self, ciphertext):
        if not self.validate_input(ciphertext):
            raise ValueError("Input contains non-printable ASCII characters.")

        decrypted_text = []
        for char in ciphertext:
            decrypted_char = chr((ord(char) - 32 - self.shift) % 95 + 32)
            decrypted_text.append(decrypted_char)
        return ''.join(decrypted_text)

    def encrypt_all_shifts(self, plaintext):
        if not self.validate_input(plaintext):
            raise ValueError("Input contains non-printable ASCII characters.")

        results = {}
        for shift in range(-127, 128):
            results[shift] = self.encrypt(plaintext)
            # Update self.shift to maintain current state
            self.shift = (self.shift + 1) % 128
        return results

    def decrypt_all_shifts(self, ciphertext):
        if not self.validate_input(ciphertext):
            raise ValueError("Input contains non-printable ASCII characters.")

        results = {}
        for shift in range(-127, 128):
            results[shift] = self.decrypt(ciphertext)
            # Update self.shift to maintain current state
            self.shift = (self.shift + 1) % 128
        return results


# Function to get user choice (encryption or decryption)
def get_user_choice():
    while True:
        try:
            choice = int(input("Enter 1 for encryption, 2 for decryption, 3 for encryption with all shifts, "
                               "4 for decryption with all shifts: "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError("Invalid choice. Enter 1, 2, 3, or 4.")
            return choice
        except ValueError as ve:
            print(f"Error: {ve}. Please enter a valid choice (1, 2, 3, or 4).")
            sys.exit(1)


# Example usage:
if __name__ == "__main__":
    try:
        plaintext = input("Enter text to encrypt/decrypt: ")
        choice = get_user_choice()

        shift_amount = int(input("Enter shift amount (-127 to 127): "))
        cipher = CaesarCipher(shift_amount)

        if choice == 1:
            encrypted_text = cipher.encrypt(plaintext)
            print("Encrypted:", encrypted_text)
        elif choice == 2:
            decrypted_text = cipher.decrypt(plaintext)
            print("Decrypted:", decrypted_text)
        elif choice == 3:
            # Decryption with all shifts
            all_encryptions = cipher.encrypt_all_shifts(plaintext)
            print("\nEncryptions with all shifts:")
            for shift, encrypted_text in all_encryptions.items():
                print(f"Shift {shift}: {encrypted_text}")
        elif choice == 4:
            # Decryption with all shifts
            all_decryptions = cipher.decrypt_all_shifts(plaintext)
            print("\nDecryptions with all shifts:")
            for shift, decrypted_text in all_decryptions.items():
                print(f"Shift {shift}: {decrypted_text}")
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        sys.exit(1)
