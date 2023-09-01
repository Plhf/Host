import socket

def main():
    host = "0.0.0.0"  # Listen on all available network interfaces
    port = 12345     # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Maximum number of queued connections

    print("Server listening on", host, "port", port)

    client_socket, client_address = server_socket.accept()
    print("Connected by", client_address)

    while True:
        data = client_socket.recv(1024).decode()  # Receive data from client
        if not data:
            break
        print("Received:", data)

        response = "Server received: " + data
        client_socket.send(response.encode())  # Send response back to client

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
