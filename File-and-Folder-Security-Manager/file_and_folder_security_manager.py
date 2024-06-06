from cryptography.fernet import Fernet
from pathlib import Path
import sys

class FileEncryptorDecryptor:
    def __init__(self, key):
        self.key = key

    def encrypt_file(self, input_path, output_path):
        try:
            input_path, output_path = Path(input_path), Path(output_path)
            if input_path == output_path:
                raise ValueError("Error: Input and output file paths cannot be the same.")
            if output_path.exists():
                raise FileExistsError("Error: Output file already exists.")

            with input_path.open("rb") as file:
                data = file.read()
            encrypted_data = self._encrypt_data(data)
            self._write_data(output_path, encrypted_data)
            print(f"File '{input_path}' encrypted and saved as '{output_path}'.")
        except (FileNotFoundError, FileExistsError, ValueError) as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def decrypt_file(self, input_path, output_path):
        try:
            input_path, output_path = Path(input_path), Path(output_path)
            if input_path == output_path:
                raise ValueError("Error: Input and output file paths cannot be the same.")
            if output_path.exists():
                raise FileExistsError("Error: Output file already exists.")

            with input_path.open("rb") as file:
                encrypted_data = file.read()
            decrypted_data = self._decrypt_data(encrypted_data)
            self._write_data(output_path, decrypted_data)
            print(f"File '{input_path}' decrypted and saved as '{output_path}'.")
        except (FileNotFoundError, FileExistsError, ValueError) as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def encrypt_directory(self, input_dir, output_dir):
        try:
            input_dir, output_dir = Path(input_dir), Path(output_dir)
            if input_dir == output_dir:
                raise ValueError("Error: Input and output directories cannot be the same.")
            if output_dir.exists():
                raise FileExistsError("Error: Output directory already exists.")

            output_dir.mkdir(parents=True, exist_ok=True)

            for file in input_dir.glob("**/*"):
                if file.is_file():
                    output_file = output_dir / file.relative_to(input_dir)
                    self.encrypt_file(file, output_file)
                    
            print(f"All files in directory '{input_dir}' encrypted and saved in '{output_dir}'.")
        except (FileNotFoundError, FileExistsError, ValueError) as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def decrypt_directory(self, input_dir, output_dir):
        try:
            input_dir, output_dir = Path(input_dir), Path(output_dir)
            if input_dir == output_dir:
                raise ValueError("Error: Input and output directories cannot be the same.")
            if output_dir.exists():
                raise FileExistsError("Error: Output directory already exists.")

            output_dir.mkdir(parents=True, exist_ok=True)

            for file in input_dir.glob("**/*"):
                if file.is_file():
                    output_file = output_dir / file.relative_to(input_dir)
                    self.decrypt_file(file, output_file)

            print(f"All files in directory '{input_dir}' decrypted and saved in '{output_dir}'.")
        except (FileNotFoundError, FileExistsError, ValueError) as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _encrypt_data(self, data):
        fernet = Fernet(self.key)
        return fernet.encrypt(data)

    def _decrypt_data(self, encrypted_data):
        fernet = Fernet(self.key)
        return fernet.decrypt(encrypted_data)

    def _write_data(self, file_path, data):
        with file_path.open("wb") as file:
            file.write(data)

def main():
    key = Fernet.generate_key()
    encryptor_decryptor = FileEncryptorDecryptor(key)

    while True:
        try:
            print("\nFile Encryption/Decryption")
            print("1. Encrypt File")
            print("2. Decrypt File")
            print("3. Encrypt Directory")
            print("4. Decrypt Directory")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                input_file = input("Enter input file path: ")
                output_file = input("Enter output file path: ")
                encryptor_decryptor.encrypt_file(input_file, output_file)
            elif choice == '2':
                input_file = input("Enter input file path: ")
                output_file = input("Enter output file path: ")
                encryptor_decryptor.decrypt_file(input_file, output_file)
            elif choice == '3':
                input_dir = input("Enter input directory path: ")
                output_dir = input("Enter output directory path: ")
                encryptor_decryptor.encrypt_directory(input_dir, output_dir)
            elif choice == '4':
                input_dir = input("Enter input directory path: ")
                output_dir = input("Enter output directory path: ")
                encryptor_decryptor.decrypt_directory(input_dir, output_dir)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Error: Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    sys.exit(0)

