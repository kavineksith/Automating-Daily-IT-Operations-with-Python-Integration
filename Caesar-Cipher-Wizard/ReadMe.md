# Caesar Cipher Encryption and Decryption

## Introduction

This Python program implements a Caesar Cipher, a simple encryption technique that shifts each letter in the plaintext by a fixed number of positions down the alphabet. It provides functionality for both encryption and decryption of messages.

## Usage

To use the program, follow these steps:

1. **Input Message**: Enter the message you want to encrypt or decrypt when prompted.

2. **Choose Operation**: Select whether you want to encrypt or decrypt the message.

    - For encryption, provide a shift value between 1 and 25.
    
    - For decryption, you have two options:
    
        - If you know the shift value used for encryption, provide it when prompted.
        
        - If you don't know the shift value, select "no" when asked, and the program will attempt to decrypt the message using all possible shift values.

3. **View Results**: The program will display the encrypted or decrypted message.

## Error Handling

The program incorporates error handling to ensure smooth execution even in case of invalid inputs. Here's how it handles errors:

- **Invalid Shift Value**: If the user provides a shift value outside the valid range (1 to 25) or non-numeric input, the program prompts the user to enter a valid shift value.

- **Invalid Operation**: If the user inputs an invalid choice for encryption or decryption, the program informs the user and asks for a valid choice.

## Implementation Details

The program is implemented using object-oriented programming principles, with the following classes and methods:

- **CaesarCipher Class**:
    - Constructor: Initializes the text to be encrypted or decrypted.
    - `encrypt(shift)`: Encrypts the text using the specified shift value.
    - `decrypt(shift=None)`: Decrypts the text using the specified shift value if provided, otherwise tries all possible shift values.

- **Main Function** (`main()`):
    - Accepts user input for the message and operation (encryption or decryption).
    - Depending on the operation, prompts the user for the shift value or whether they know the shift value for decryption.
    - Calls the appropriate methods of the `CaesarCipher` class and displays the results.

## Example

Here are examples demonstrating encryption and decryption with and without shift values:

### Encryption with Shift Value:

#### Input:
```
Enter message: Hello, World!
Do you want to encrypt or decrypt the message? (encrypt/decrypt): encrypt
Enter the cipher shift value (1..25): 3
```

#### Output:
```
Encrypted: Khoor, Zruog!
```

### Decryption with Shift Value:

#### Input:
```
Enter message: Khoor, Zruog!
Do you want to encrypt or decrypt the message? (encrypt/decrypt): decrypt
Do you have the shift value? (yes/no): yes
Enter the cipher shift value (1..25): 3
```

#### Output:
```
Decrypted: Hello, World!
```

### Encryption without Shift Value:

#### Input:
```
Enter message: Hello, World!
Do you want to encrypt or decrypt the message? (encrypt/decrypt): encrypt
Enter the cipher shift value (1..25): 3
```

#### Output:
```
Encrypted: Khoor, Zruog!
```

### Decryption without Shift Value:

#### Input:
```
Enter message: Khoor, Zruog!
Do you want to encrypt or decrypt the message? (encrypt/decrypt): decrypt
Do you have the shift value? (yes/no): no
```

#### Output:
```
Possible Decrypted Messages:
Shift 1: Jgnnq, Asvph!
Shift 2: Ifmmq, Zrugm!
Shift 3: Hello, World!
...
Shift 25: Zknnq, Vnqkc!
``` 

These examples demonstrate the functionality of the Caesar Cipher program for both encryption and decryption, with and without providing the shift value.

## Conclusion

This Python program offers a simple yet effective implementation of the Caesar Cipher encryption and decryption technique. It provides a user-friendly interface and robust error handling, making it suitable for secure communication where basic encryption is sufficient.

