import socket
import threading


def handle_client(client_socket):
    while True:
        try:

            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break


            for other_client in clients:
                if other_client != client_socket:
                    try:
                        other_client.sendall(message.encode('utf-8'))
                    except:
                        other_client.close()

                        clients.remove(other_client)

        except ConnectionResetError:

            clients.remove(client_socket)
            client_socket.close()
            break


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen()

    print("Server started, waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")


        clients.append(client_socket)


        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


clients = []


server_thread = threading.Thread(target=server)
server_thread.start()