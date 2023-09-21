import socket
import os

# Set the server host and port
SERVER_HOST = "0.0.0.0"  # Listen on all available network interfaces
SERVER_PORT = 12345  # Use any available port you prefer

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to the specified host and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"Listening on {SERVER_HOST}:{SERVER_PORT}...")

while True:
    # Accept client connections
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive the filename
    filename = client_socket.recv(1024).decode()
    if not filename:
        continue

    # Specify the directory where files will be stored
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    # Create the file on the server and receive the data
    file_path = os.path.join(upload_dir, filename)
    with open(file_path, "wb") as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print(f"Received '{filename}' from {client_address}")
    client_socket.close()

server_socket.close()
