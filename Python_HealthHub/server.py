import socket
import threading

# This function will handle individual client communication
def handle_client(client_socket):
    while True:
        try:
            # Receiving message from a client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            # Broadcasting message to all other connected clients
            for other_client in clients:
                if other_client != client_socket:
                    try:
                        other_client.sendall(message.encode('utf-8'))
                    except:
                        other_client.close()
                        # Remove client from the list if it's no longer connected
                        clients.remove(other_client)

        except ConnectionResetError:
            # Removing client from list if it's no longer connected
            clients.remove(client_socket)
            client_socket.close()
            break

# Server setup
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Bind to all network interfaces on port 12345
    server_socket.listen()

    print("Server started, waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Adding client to the clients list
        clients.append(client_socket)

        # Handling client communication in a separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# List to keep track of connected clients
clients = []

# Starting the server
server_thread = threading.Thread(target=server)
server_thread.start()