## **Caesar Cipher Utility Documentation**

### **Overview**

This documentation provides a comprehensive guide for a Caesar cipher utility implemented in Python. The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

### **Features**

- **Encryption**: Encrypts plaintext using a specified shift value.
- **Decryption**: Decrypts ciphertext using the inverse shift of the encryption process.
- **Encryption with All Shifts**: Generates encrypted versions of the plaintext for all possible shifts.
- **Decryption with All Shifts**: Generates decrypted versions of the ciphertext for all possible shifts.

### **Dependencies**

- **Python**: Version 3.x
- **re**: Python library for regular expressions.
- **sys**: Python library providing access to system-specific parameters and functions.

### **CaesarCipher Class**

#### **Initialization**

The `CaesarCipher` class initializes with a shift value for encryption and decryption operations.

#### **Methods**

- **encrypt(plaintext)**:
  - Encrypts plaintext using the Caesar cipher with a specified shift.
  - Returns encrypted text.

- **decrypt(ciphertext)**:
  - Decrypts ciphertext using the Caesar cipher with the inverse of the specified shift.
  - Returns decrypted text.

- **encrypt_all_shifts(plaintext)**:
  - Generates encrypted versions of the plaintext for all possible shifts (-127 to 127).
  - Returns a dictionary mapping each shift to its corresponding encrypted text.

- **decrypt_all_shifts(ciphertext)**:
  - Generates decrypted versions of the ciphertext for all possible shifts (-127 to 127).
  - Returns a dictionary mapping each shift to its corresponding decrypted text.

### **User Interaction Functions**

- **get_user_choice()**:
  - Retrieves user's choice for encryption, decryption, encryption with all shifts, or decryption with all shifts.
  - Returns 1 for encryption, 2 for decryption, 3 for encryption with all shifts, or 4 for decryption with all shifts.

### **Example Usage**

A sample script demonstrates how to use the Caesar cipher utility:

1. User inputs text to encrypt or decrypt.
2. User selects the operation (encryption, decryption, encryption with all shifts, or decryption with all shifts).
3. Depending on the choice, the script performs the corresponding operation using the Caesar cipher.

### **Error Handling**

- Handles errors such as invalid input, encryption failures, decryption failures, and unexpected errors gracefully.
- Displays appropriate error messages to guide users.

### **Conclusion**

This documentation outlines the functionality and usage of a Python-based Caesar cipher utility. It emphasizes versatility in encryption and decryption operations, as well as demonstrates how to interactively use the utility through a command-line interface.

### **License**

This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**

Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.
