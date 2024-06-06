import socket
import threading
import sys
import re


# Function to validate username using regular expression
def validate_username(username):
    try:
        # Regular expression pattern for username validation
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return bool(re.match(pattern, username))
    except Exception as e:
        print(f"An unexpected error occurred while validating username: {e}")
        return False


# Function to check username and validations
def character_username():
    try:
        while True:
            username = input("Enter your username: ")
            if validate_username(username):
                return username
            else:
                print("Invalid username. Please enter a username containing only letters, numbers, and underscores, "
                      "between 3 and 20 characters long.")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Function to print prompt with username
def print_prompt(username):
    print("\r{}>> ".format(username), end='', flush=True)


# Function to handle receiving messages from the server
def receive_messages(client_socket, current_username):
    try:
        while True:
            # Receive message from server
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                if ":" in message:
                    sender, msg = message.split(":", 1)
                    if sender.strip() != current_username:
                        print("\n" + message)  # Print incoming messages on a new line
                    print_prompt(current_username)  # Show message input prompt immediately
                else:
                    print("\n" + message)  # Print incoming messages on a new line
                    print_prompt(current_username)  # Show message input prompt immediately
    except ConnectionError:
        # print("Connection error:", e)
        print("Connection error")
        client_socket.close()
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt: Exiting...")
        client_socket.close()
        sys.exit(1)
    except OSError as e:
        if e.errno == 10038:
            print("An unexpected error occurred: The socket is not valid.")
        elif e.errno == 10053:
            print("An unexpected error occurred: The connection was aborted by the host.")
        else:
            print("An unexpected error occurred:", e)
        client_socket.close()
        sys.exit(1)
    except Exception as e:
        print("An unexpected error occurred:", e)
        client_socket.close()
        sys.exit(1)


# Main function to run the client
def main():
    # Client configuration
    host = "127.0.0.1"
    port = 5555

    # Connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except ConnectionRefusedError:
        print("Connection error: Connection refused. Please ensure the server is running.")
        sys.exit(1)
    except Exception as e:
        print("An unexpected error occurred while connecting to the server:", e)
        sys.exit(1)

    # Get username from user
    username = character_username()

    # Send username to server
    try:
        client_socket.send(username.encode("utf-8"))
    except Exception as e:
        print("An unexpected error occurred while sending username:", e)
        client_socket.close()
        sys.exit(1)

    # Start a thread to receive messages from server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket, username))
    receive_thread.start()

    # Main loop to send messages
    try:
        while True:
            print_prompt(username)
            message = input("")  # Prompt with username

            # Check for exit command
            if message.strip().lower() == "/exit":
                try:
                    print("You have left the chat.")  # Notify locally
                    # Notify clients about the user leaving
                    exit_message = "[{}] has left the chat.".format(username)
                    client_socket.send(exit_message.encode("utf-8"))  # Notify server about exit
                except Exception as e:
                    print("An unexpected error occurred while sending exit command:", e)
                break  # Exit loop

            if message.strip():  # Check if message is not empty
                # Send message to server
                try:
                    client_socket.send("{}: {}".format(username, message).encode("utf-8"))
                except Exception as e:
                    print("An unexpected error occurred while sending message:", e)
                    client_socket.close()
                    sys.exit(1)
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt: Exiting...")
        client_socket.close()
        sys.exit(1)
    finally:
        client_socket.close()  # Close connection
        sys.exit(0)  # Exit program


if __name__ == "__main__":
    main()
