## Documentation : File and Folder Security Manager

### Overview
This Python script provides functionality to encrypt and decrypt files and directories using the Fernet symmetric encryption algorithm from the `cryptography` library. Users can specify input and output paths for individual files or entire directories. The script ensures data integrity and confidentiality by securely encrypting and decrypting file contents.

### Requirements
- Python 3.x
- `cryptography` library (`pip install cryptography`)

### Usage
1. Install the required library using `pip install cryptography`.
2. Run the script and follow the menu prompts to perform file encryption or decryption.
3. Provide input and output paths as required.

### Implementation Details
#### Dependencies
- `cryptography.fernet.Fernet`: Used for symmetric encryption and decryption.
- `pathlib.Path`: Provides object-oriented filesystem paths.
- `sys`: Used for system-level operations and handling exceptions.

#### Class: `FileEncryptorDecryptor`
- Methods:
  - `__init__(self, key)`: Initializes the FileEncryptorDecryptor object with a Fernet key.
  - `encrypt_file(self, input_path, output_path)`: Encrypts the contents of a file and saves the encrypted data to another file.
  - `decrypt_file(self, input_path, output_path)`: Decrypts the contents of an encrypted file and saves the decrypted data to another file.
  - `encrypt_directory(self, input_dir, output_dir)`: Encrypts all files in a directory and saves them in another directory.
  - `decrypt_directory(self, input_dir, output_dir)`: Decrypts all encrypted files in a directory and saves the decrypted files in another directory.

#### Function: `main()`
- Provides a user-friendly interface for performing file encryption and decryption.
- Options:
  - `1. Encrypt File`: Prompts the user to enter input and output file paths for encryption.
  - `2. Decrypt File`: Prompts the user to enter input and output file paths for decryption.
  - `3. Encrypt Directory`: Prompts the user to enter input and output directory paths for encrypting all files in the directory.
  - `4. Decrypt Directory`: Prompts the user to enter input and output directory paths for decrypting all encrypted files in the directory.
  - `5. Exit`: Exits the program.

### Conclusion
This script offers a convenient and secure way to encrypt and decrypt files and directories using the Fernet encryption algorithm. It can be used for protecting sensitive data stored on local filesystems, ensuring confidentiality and integrity of information. With its intuitive command-line interface, users can easily encrypt or decrypt files with minimal effort.

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.