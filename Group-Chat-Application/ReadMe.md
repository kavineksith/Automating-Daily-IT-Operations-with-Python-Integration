## Chat Application Documentation

### Overview
This chat application provides a platform for users to send encrypted messages to each other either individually or in group chats. It uses SQLite3 as the database to store user information and messages. Encryption and decryption of messages are handled using the Fernet encryption scheme provided by the `cryptography` library. The application is designed to ensure secure communication between users while maintaining data integrity.

### Usage

### User Registration
1. Upon running the application, you will be prompted to register by providing a username and a password.
2. Enter a unique username and a strong password when prompted.

### User Login
1. After registration, you will be asked to login with your username and password.
2. Enter your registered username and password to login.

### User Interaction Menu
Once logged in, you will see a menu with various options:

1. **Send a message to a user:** Send a message to another registered user by entering their username and the message content.
2. **Send a message to all users:** Broadcast a message to all registered users.
3. **Send a message to group chat:** Send a message to a group chat by specifying the group chat ID.
4. **Show all users:** Display all users currently registered in the chat application.
5. **Show received messages:** Display all messages received by the current user.
6. **Show solo chat messages:** Display messages exchanged between the current user and another user in a solo chat.
7. **Show group chat messages:** Display messages exchanged in a specific group chat.
8. **Show old messages between two users:** Display historical messages exchanged between two specific users.
9. **Show all messages received by the current user:** Display all messages received by the current user, including those from group chats.
10. **Create solo chat with user:** Start a solo chat with another user by entering their username.
11. **Create group chat:** Create a new group chat by providing a name and specifying the users to include.
12. **Join group chat:** Join an existing group chat by entering the group chat ID.
13. **Display group chats:** Display all group chats that the current user is a member of.
14. **Display group chat members:** Display all members of a specific group chat.
15. **Clear messages:** Delete all messages from the database.
16. **Exit:** Log out and exit the application.

### Security Measures

- **Encryption:** Messages are encrypted using the Fernet encryption scheme, ensuring that only the intended recipient can decrypt and read the messages.
- **Password Storage:** User passwords are securely hashed using SHA-256 and stored alongside a unique salt, preventing unauthorized access to user accounts.
- **Authentication:** User authentication is performed securely by comparing hashed passwords during login.
- **Input Validation:** User inputs, such as usernames and passwords, are validated to prevent malicious input and ensure data integrity.

### Conclusion
This chat application provides a secure and user-friendly platform for communication between users. By leveraging encryption techniques and secure storage practices, it ensures confidentiality and integrity of user data and messages.

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.