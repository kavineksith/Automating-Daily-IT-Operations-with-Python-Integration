## **AES Encryption and Decryption Utility Documentation**

### **Overview**

This documentation provides a detailed description and usage guide for an AES encryption and decryption utility implemented in Python. The utility utilizes the Advanced Encryption Standard (AES) algorithm in Cipher Feedback (CFB) mode for secure encryption and decryption of text data.

### **Features**

- **Encryption**: Encrypts plaintext input using AES in CFB mode.
- **Decryption**: Decrypts AES-encrypted data provided as a hexadecimal string.
- **Password Validation**: Ensures password strength for secure key derivation.

### **Dependencies**

- **Python**: Version 3.x
- **cryptography**: Python library for cryptographic recipes and primitives.

### **Installation**

Ensure Python 3.x is installed. Install the required library using pip:

```
pip install cryptography
```

### **AESCipher Class**

#### **Initialization**

The `AESCipher` class initializes with a user-provided password for encryption and decryption operations.

#### **Methods**

- **encrypt(plaintext)**:
  - Encrypts plaintext using AES encryption in CFB mode.
  - Returns encrypted data as a hexadecimal string (salt + iv + ciphertext).

- **decrypt(encrypted_data_hex)**:
  - Decrypts AES-encrypted data provided as a hexadecimal string.
  - Returns decrypted plaintext.

#### **Password Validation Function**

#### `validate_password(password)`

Ensures the password meets specific criteria:
- Minimum length of 8 characters.
- Includes at least one lowercase letter, one uppercase letter, one digit, and one special character.

#### **User Interaction Functions**

- **get_user_choice()**:
  - Retrieves user's choice for encryption or decryption.
  - Returns 1 for encryption or 2 for decryption.

### **Example Usage**

A sample script demonstrates how to use the AES encryption and decryption utility:

1. User inputs a password.
2. User inputs text to encrypt or decrypt.
3. Based on user's choice, the script encrypts or decrypts the text using AES.

### **Error Handling**

- Handles errors such as invalid input, encryption failures, decryption failures, and unexpected errors gracefully.
- Displays appropriate error messages to guide users.

### **Conclusion**

This documentation provides a robust framework for securely encrypting and decrypting data using AES encryption with Python. It emphasizes password strength for secure key derivation and includes examples to facilitate understanding and implementation. This documentation outline covers the essential aspects of the AES encryption and decryption utility without including specific source code details, focusing instead on functionality, usage, and implementation guidance.

### **License**

This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**

Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.


