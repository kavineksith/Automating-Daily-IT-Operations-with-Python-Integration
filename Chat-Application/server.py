import socket
import threading


# Function to handle incoming client connections
def handle_client(client_socket, clients):
    try:
        while True:
            # Receive message from client
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                # Broadcast message to all clients except the sender
                for c in clients:
                    if c != client_socket:
                        c.send(message.encode("utf-8"))
    except ConnectionResetError:
        print("Connection with client reset unexpectedly.")
    except ConnectionAbortedError:
        print("Connection with client aborted unexpectedly.")
    except OSError as e:
        print("OS error:", e)
    finally:
        # Remove client and close socket
        try:
            clients.remove(client_socket)
            client_socket.close()
        except Exception as e:
            print("An unexpected error occurred during cleanup:", e)


# Function to broadcast a message to all clients except one
def broadcast(message, clients, exclude=None):
    for client in clients:
        if client != exclude:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                print("An error occurred while broadcasting message to a client:", e)


# Main function to run the server
def main():
    # Server configuration
    host = "127.0.0.1"
    port = 5555

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("[*] Server listening on {}:{}".format(host, port))

    clients = []

    # Accept incoming connections
    try:
        while True:
            client_socket, addr = server_socket.accept()
            print("[*] Accepted connection from {}:{}".format(addr[0], addr[1]))

            # Add client to list
            clients.append(client_socket)

            # Receive username from client
            # Send the username instead of IP address
            client_name = client_socket.recv(1024).decode("utf-8") or "Unknown"

            # Notify clients about the new user, excluding the newly joined client
            broadcast("[{}] has joined the chat.".format(client_name), clients, client_socket)

            # Start a new thread to handle client communication
            client_thread = threading.Thread(target=handle_client, args=(client_socket, clients))
            client_thread.start()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt: Exiting...")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        # Close server socket
        try:
            server_socket.close()
        except Exception as e:
            print("An unexpected error occurred while closing the server socket:", e)


if __name__ == "__main__":
    main()
