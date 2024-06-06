import sqlite3
import sys
import threading
import re
import hashlib
import secrets
from datetime import datetime
from cryptography.fernet import Fernet

# Initialize SQLite3 database
conn = sqlite3.connect('chat.db')
c = conn.cursor()

# Create users table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY,
             username TEXT NOT NULL UNIQUE,
             password_hash TEXT NOT NULL,
             salt TEXT NOT NULL,
             encryption_key TEXT NOT NULL
             )''')

# Create messages table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS messages (
             id INTEGER PRIMARY KEY,
             sender_id INTEGER NOT NULL,
             receiver_id INTEGER NOT NULL,
             message TEXT NOT NULL,
             timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
             FOREIGN KEY (sender_id) REFERENCES users(id),
             FOREIGN KEY (receiver_id) REFERENCES users(id)
             )''')

# Create group chats table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS group_chats (
             id INTEGER PRIMARY KEY,
             group_name TEXT NOT NULL UNIQUE
             )''')

# Create group chat users table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS group_chat_users (
             id INTEGER PRIMARY KEY,
             group_chat_id INTEGER NOT NULL,
             user_id INTEGER NOT NULL,
             FOREIGN KEY (group_chat_id) REFERENCES group_chats(id),
             FOREIGN KEY (user_id) REFERENCES users(id)
             )''')

# Create group chat permissions table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS group_chat_permissions (
             id INTEGER PRIMARY KEY,
             group_chat_id INTEGER NOT NULL,
             user_id INTEGER NOT NULL,
             permission_level TEXT NOT NULL,
             FOREIGN KEY (group_chat_id) REFERENCES group_chats(id),
             FOREIGN KEY (user_id) REFERENCES users(id)
             )''')

conn.commit()

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt a message using a key
def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(message.encode())

# Decrypt a message using a key
def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_message).decode()

# Function to validate username with advanced regular expression
def validate_username(username):
    if re.match(r'^[a-zA-Z0-9_]+$', username):
        return True
    else:
        print("Invalid username. Usernames can only contain letters, numbers, and underscores.")
        return False

# Function to validate password with advanced regular expression
def validate_password(password):
    if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+}{":;\'?/>.<,])(?=.*[a-zA-Z]).{8,}$', password):
        return True
    else:
        print("Invalid password. Passwords must contain at least 8 characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return False

"""
# Function to encrypt password using SHA-256 with salt
def encrypt_password(password):
    salt = secrets.token_hex(16)
    password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    return password_hash, salt
"""

# Encrypt a password and return the hash and salt
def encrypt_password(password):
    salt = generate_key()
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password, salt

# Decrypt a password using the provided key
def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_password).decode()

"""
# Function to register user
def register_user(username, password):
    try:
        if validate_username(username) and validate_password(password):
            password_hash, salt = encrypt_password(password)
            c.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)", (username, password_hash, salt))
            conn.commit()
            print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")
    except Exception as e:
        print("Error:", e)
"""

# Function to register user
def register_user(username, password):
    try:
        if validate_username(username) and validate_password(password):
            password_hash, salt = encrypt_password(password)
            key = generate_key()  # Generate encryption key for the user
            encrypted_key = encrypt_message(key, password_hash)  # Encrypt key with user's password hash
            c.execute("INSERT INTO users (username, password_hash, salt, encryption_key) VALUES (?, ?, ?, ?)", (username, password_hash, salt, encrypted_key))
            conn.commit()
            print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")
    except Exception as e:
        print("Error:", e)

"""
# Function to login user
def login_user(username, password):
    try:
        c.execute("SELECT id, password_hash, salt FROM users WHERE username=?", (username,))
        user = c.fetchone()
        if user:
            user_id, stored_password_hash, salt = user
            hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
            if hashed_password == stored_password_hash:
                print("Login successful!")
                return user_id
            else:
                print("Invalid username or password.")
                return None
        else:
            print("Invalid username or password.")
            return None
    except Exception as e:
        print("Error:", e)
        return None
"""

# Function to login user and retrieve encryption key
def login_user(username, password):
    try:
        c.execute("SELECT id, password_hash, salt, encryption_key FROM users WHERE username=?", (username,))
        user = c.fetchone()
        if user:
            user_id, stored_password_hash, salt, encrypted_key = user
            hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
            if hashed_password == stored_password_hash:
                key = decrypt_password(encrypted_key, password)  # Decrypt user's encryption key
                print("Login successful!")
                return user_id, key
            else:
                print("Invalid username or password.")
                return None, None
        else:
            print("Invalid username or password.")
            return None, None
    except Exception as e:
        print("Error:", e)
        return None, None

# Function to handle user joining the chat
def join_chat(username):
    try:
        c.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        print(f"Welcome to the chat, {username}!")
    except Exception as e:
        print("Error:", e)

# Function to handle user leaving the chat
def leave_chat(username):
    try:
        c.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
        print(f"Goodbye, {username}!")
    except Exception as e:
        print("Error:", e)

# Function to send a message to a specific user
def send_message(sender_id, receiver_username, message, key):
    try:
        c.execute("SELECT id FROM users WHERE username=?", (receiver_username,))
        receiver = c.fetchone()
        if receiver:
            receiver_id = receiver[0]
            encrypted_message = encrypt_message(message, key)
            c.execute("INSERT INTO messages (sender_id, receiver_id, message) VALUES (?, ?, ?)", (sender_id, receiver_id, encrypted_message))
            conn.commit()
            print(f"Message sent to {receiver_username}.")
        else:
            print(f"User {receiver_username} not found.")
    except Exception as e:
        print("Error:", e)

# Function to send a message to all users
def send_message_to_all(sender_id, message, key):
    try:
        c.execute("SELECT id FROM users WHERE id!=?", (sender_id,))
        receivers = c.fetchall()
        for receiver_id in receivers:
            encrypted_message = encrypt_message(message, key)
            c.execute("INSERT INTO messages (sender_id, receiver_id, message) VALUES (?, ?, ?)", (sender_id, receiver_id[0], encrypted_message))
        conn.commit()
        print("Message sent to all users.")
    except Exception as e:
        print("Error:", e)

# Function to send a message to a group chat
def send_message_to_group_chat(sender_id, group_chat_id, message, key):
    try:
        # Retrieve all members of the group chat
        c.execute("SELECT user_id FROM group_chat_permissions WHERE group_chat_id=? AND permission_level='member'", (group_chat_id,))
        receivers = c.fetchall()
        # Send the message to each member of the group chat
        for receiver in receivers:
            encrypted_message = encrypt_message(message, key)
            c.execute("INSERT INTO messages (sender_id, receiver_id, message) VALUES (?, ?, ?)", (sender_id, receiver[0], encrypted_message))
        conn.commit()
        print("Message sent to group chat.")
    except Exception as e:
        print("Error:", e)

# Function to display all users in the chat
def display_users():
    try:
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        print("Users currently in the chat:")
        for user in users:
            print(user[1])
    except Exception as e:
        print("Error:", e)

# Function to retrieve and display messages for a specific user
def display_messages(username, key):
    try:
        c.execute("SELECT m.timestamp, u.username, m.message FROM messages m JOIN users u ON m.sender_id=u.id WHERE m.receiver_id = (SELECT id FROM users WHERE username=?) ORDER BY m.timestamp", (username,))
        messages = c.fetchall()
        for message in messages:
            decrypted_message = decrypt_message(message[2], key)
            print(f"{message[0]} - {message[1]}: {decrypted_message}")
    except Exception as e:
        print("Error:", e)

# Function to show old messages between two specific users
def show_old_messages(user1, user2, key):
    try:
        c.execute("SELECT m.timestamp, u1.username AS sender, u2.username AS receiver, m.message FROM messages m JOIN users u1 ON m.sender_id=u1.id JOIN users u2 ON m.receiver_id=u2.id WHERE ((u1.username=? AND u2.username=?) OR (u1.username=? AND u2.username=?)) AND (m.sender_id=? OR m.receiver_id=?) ORDER BY m.timestamp", (user1, user2, user2, user1, current_user_id, current_user_id))
        messages = c.fetchall()
        for message in messages:
            decrypted_message = decrypt_message(message[3], key)
            print(f"{message[0]} - {message[1]} to {message[2]}: {decrypted_message}")
    except Exception as e:
        print("Error:", e)

# Function to show all messages received by the current user
def show_received_messages(current_user_id, key):
    try:
        c.execute("SELECT m.timestamp, u.username AS sender, m.message FROM messages m JOIN users u ON m.sender_id=u.id WHERE m.receiver_id=? ORDER BY m.timestamp", (current_user_id,))
        messages = c.fetchall()
        for message in messages:
            decrypted_message = decrypt_message(message[2], key)
            print(f"{message[0]} - {message[1]}: {decrypted_message}")
    except Exception as e:
        print("Error:", e)

# Function to create a solo chat between two users
def create_solo_chat(current_user_id, other_username):
    try:
        c.execute("SELECT id FROM users WHERE username=?", (other_username,))
        other_user_id = c.fetchone()[0]
        if other_user_id == current_user_id:
            print("You cannot create a chat with yourself.")
            return
        c.execute("INSERT INTO solo_chats (user1_id, user2_id) VALUES (?, ?)", (current_user_id, other_user_id))
        conn.commit()
        print(f"Solo chat with {other_username} created successfully!")
    except Exception as e:
        print("Error:", e)

# Function to show a solo chat between two users
def display_solo_chat_messages(current_user_id, other_username, key):
    try:
        # Get the ID of the other user
        c.execute("SELECT id FROM users WHERE username=?", (other_username,))
        other_user_id = c.fetchone()
        if other_user_id:
            # Retrieve and display messages between the current user and the other user
            c.execute("SELECT m.timestamp, u.username, m.message FROM messages m JOIN users u ON m.sender_id=u.id WHERE (m.sender_id=? AND m.receiver_id=?) OR (m.sender_id=? AND m.receiver_id=?) ORDER BY m.timestamp", (current_user_id, other_user_id[0], other_user_id[0], current_user_id))
            messages = c.fetchall()
            print(f"Solo Chat Messages with {other_username}:")
            for message in messages:
                decrypted_message = decrypt_message(message[2], key)
                print(f"{message[0]} - {message[1]}: {decrypted_message}")
        else:
            print(f"User {other_username} not found.")
    except Exception as e:
        print("Error:", e)

# Function to create a group chat with permissions
def create_group_chat(current_user_id, group_name, users):
    try:
        c.execute("INSERT INTO group_chats (group_name) VALUES (?)", (group_name,))
        group_chat_id = c.lastrowid
        c.execute("INSERT INTO group_chat_permissions (group_chat_id, user_id, permission_level) VALUES (?, ?, 'host')", (group_chat_id, current_user_id))
        for user in users:
            c.execute("INSERT INTO group_chat_permissions (group_chat_id, user_id, permission_level) VALUES (?, ?, 'member')", (group_chat_id, user))
        conn.commit()
        print("Group chat created successfully!")
    except Exception as e:
        print("Error:", e)

# Function to join a group chat
def join_group_chat(current_user_id, group_chat_id):
    try:
        # Check if the current user has permission to join the group chat
        c.execute("SELECT permission_level FROM group_chat_permissions WHERE group_chat_id=? AND user_id=?", (group_chat_id, current_user_id))
        permission = c.fetchone()
        if permission:
            print("You are already a member of this group chat.")
            return
        # If the user has permission, add them to the group chat
        c.execute("INSERT INTO group_chat_permissions (group_chat_id, user_id, permission_level) VALUES (?, ?, 'member')", (group_chat_id, current_user_id))
        conn.commit()
        print("You have joined the group chat successfully!")
    except Exception as e:
        print("Error:", e)

# Function to display group chats the user is a member of
def display_group_chats(current_user_id):
    try:
        c.execute("SELECT gc.group_name FROM group_chats gc JOIN group_chat_permissions gcp ON gc.id=gcp.group_chat_id WHERE gcp.user_id=? AND gcp.permission_level='member'", (current_user_id,))
        group_chats = c.fetchall()
        if group_chats:
            print("Group Chats:")
            for chat in group_chats:
                print(chat[0])
        else:
            print("You are not a member of any group chats.")
    except Exception as e:
        print("Error:", e)

# Function to display group chat members
def display_group_chat_members(current_user_id, group_chat_id):
    try:
        c.execute("SELECT u.username FROM users u JOIN group_chat_permissions gcp ON u.id=gcp.user_id WHERE gcp.group_chat_id=? AND gcp.permission_level!='host'", (group_chat_id,))
        members = c.fetchall()
        if members:
            print("Group Chat Members:")
            for member in members:
                print(member[0])
        else:
            print("No members found in this group chat.")
    except Exception as e:
        print("Error:", e)

def display_group_chat_messages(current_user_id, group_chat_id, key):
    try:
        # Check if the user is a member of the group chat
        c.execute("SELECT permission_level FROM group_chat_permissions WHERE group_chat_id=? AND user_id=?", (group_chat_id, current_user_id))
        permission = c.fetchone()
        if permission:
            # Retrieve and display messages for the group chat
            c.execute("SELECT m.timestamp, u.username, m.message FROM messages m JOIN users u ON m.sender_id=u.id WHERE m.receiver_id=? ORDER BY m.timestamp", (group_chat_id,))
            messages = c.fetchall()
            print("Group Chat Messages:")
            for message in messages:
                decrypted_message = decrypt_message(message[2], key)
                print(f"{message[0]} - {message[1]}: {decrypted_message}")
        else:
            print("You are not authorized to view messages in this group chat.")
    except Exception as e:
        print("Error:", e)

# Function to clear messages from the database
def clear_messages():
    try:
        c.execute("DELETE FROM messages")
        conn.commit()
        print("All messages cleared successfully!")
    except Exception as e:
        print("Error:", e)

# Function to handle user interaction
def user_interaction(current_user_id, key):
    try:
        while True:
            print("\nChoose an option:")
            print("01. Send a message to a user")
            print("02. Send a message to all users")
            print("03. Send a message to group chat")
            print("04. Show all users")
            print("05. Show received messages")
            print("06. Show solo chat messages")
            print("07. Show group chat messages")
            print("08. Show old messages between two users")
            print("09. Show all messages received by the current user")
            print("10. Create solo chat with user")
            print("11. Create group chat")
            print("12. Join group chat")
            print("13. Display group chats")
            print("14. Display group chat members")
            print("15. Clear messages")
            print("16. Exit")
            
            choice = input("Your choice: ")

            if choice == "01":
                receiver_username = input("Enter the username of the receiver: ")
                message = input("Enter your message: ")
                send_message(current_user_id, receiver_username, message, key)
            elif choice == "02":
                message = input("Enter your message: ")
                send_message_to_all(current_user_id, message, key)
            elif choice == "03":  # Add option to send message to a group chat
                group_chat_id = input("Enter the ID of the group chat you want to send a message to: ")
                message = input("Enter your message: ")
                send_message_to_group_chat(current_user_id, group_chat_id, message, key)
            elif choice == "04":
                display_users()
            elif choice == "05":
                display_messages(username, key)
            elif choice == "06":  # Add option to view solo chat messages
                other_username = input("Enter the username of the other user: ")
                display_solo_chat_messages(current_user_id, other_username, key)
            elif choice == "07":  # Add option to view group chat messages
                group_chat_id = input("Enter the ID of the group chat you want to view messages for: ")
                display_group_chat_messages(current_user_id, group_chat_id, key)
            elif choice == "08":
                user1 = input("Enter the username of the first user: ")
                user2 = input("Enter the username of the second user: ")
                show_old_messages(user1, user2, key)
            elif choice == "09":
                show_received_messages(current_user_id, key)
            elif choice == "10":
                other_username = input("Enter the username of the other user: ")
                create_solo_chat(current_user_id, other_username)
            elif choice == "11":
                group_name = input("Enter the name of the group chat: ")
                users = input("Enter the usernames of the users separated by comma: ").split(",")
                create_group_chat(current_user_id, group_name, users)
            elif choice == "12":
                group_chat_id = input("Enter the ID of the group chat you want to join: ")
                join_group_chat(current_user_id, group_chat_id)
            elif choice == "13":
                display_group_chats(current_user_id)
            elif choice == "14":
                group_chat_id = input("Enter the ID of the group chat: ")
                display_group_chat_members(current_user_id, group_chat_id)
            elif choice == "15":
                clear_messages()
            elif choice == "16":
                leave_chat(username)
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose again.")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt: Exiting...")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
        sys.exit(0)

# Main function
if __name__ == "__main__":
    try:
        # User registration
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register_user(username, password)

        # User login
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        current_user_id, key = login_user(username, password)

        if current_user_id:
            user_interaction(current_user_id, key)
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt: Exiting...")
        sys.exit(1)
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")
