import socket

# Set the server host and port
SERVER_HOST = "server_ip_or_hostname"  # Replace with the actual server IP or hostname
SERVER_PORT = 12345  # Use the same port as the server

# Specify the file to upload
filename = "anarchitect"  # Updated filename

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Send the filename to the server
    client_socket.send(filename.encode())

    # Open the file and send its contents to the server
    with open(filename, "rb") as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)

    print(f"Uploaded '{filename}' to the server")

except Exception as e:
    print(f"Error: {e}")

finally:
    client_socket.close()
