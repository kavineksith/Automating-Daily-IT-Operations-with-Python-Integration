class CaesarCipher:
    def __init__(self, text):
        self.text = text

    def encrypt(self, shift):
        cipher = ''
        for char in self.text:
            if char.isalpha():
                code = ord(char) + shift
                if char.isupper():
                    first = ord('A')
                else:
                    first = ord('a')
                code -= first
                code %= 26
                cipher += chr(first + code)
            else:
                cipher += char
        return cipher

    def decrypt(self, shift=None):
        if shift is not None:
            decrypted_text = ''
            for char in self.text:
                if char.isalpha():
                    code = ord(char) - shift
                    if char.isupper():
                        first = ord('A')
                    else:
                        first = ord('a')
                    code -= first
                    code %= 26
                    decrypted_text += chr(first + code)
                else:
                    decrypted_text += char
            return decrypted_text
        else:
            decrypted_texts = []
            for shift in range(1, 26):
                decrypted_text = ''
                for char in self.text:
                    if char.isalpha():
                        code = ord(char) - shift
                        if char.isupper():
                            first = ord('A')
                        else:
                            first = ord('a')
                        code -= first
                        code %= 26
                        decrypted_text += chr(first + code)
                    else:
                        decrypted_text += char
                decrypted_texts.append(decrypted_text)
            return decrypted_texts


def main():
    text = input("Enter message: ")
    choice = input("Do you want to encrypt or decrypt the message? (encrypt/decrypt): ").lower()

    if choice == 'encrypt':
        while True:
            try:
                shift = int(input("Enter the cipher shift value (1..25): "))
                if shift not in range(1, 26):
                    raise ValueError("Shift value must be between 1 and 25.")
                break
            except ValueError as e:
                print(f"Error: {e}")

        cipher = CaesarCipher(text)
        encrypted_text = cipher.encrypt(shift)
        print("Encrypted:", encrypted_text)

    elif choice == 'decrypt':
        option = input("Do you have the shift value? (yes/no): ").lower()
        if option == 'yes':
            while True:
                try:
                    shift = int(input("Enter the cipher shift value (1..25): "))
                    if shift not in range(1, 26):
                        raise ValueError("Shift value must be between 1 and 25.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            cipher = CaesarCipher(text)
            decrypted_text = cipher.decrypt(shift)
            print("Decrypted:", decrypted_text)
        elif option == 'no':
            cipher = CaesarCipher(text)
            decrypted_texts = cipher.decrypt()
            print("Possible Decrypted Messages:")
            for i, decrypted_text in enumerate(decrypted_texts):
                print(f"Shift {i+1}: {decrypted_text}")
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()
