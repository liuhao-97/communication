import socket
import datetime

def get_current_timestamp():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S.%f")

# Server configuration
server_ip = '10.72.138.169'  # Use '0.0.0.0' to accept connections on all network interfaces
server_port = 1236

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {server_ip}:{server_port}")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Receive data
timestamp = get_current_timestamp()
data = client_socket.recv(1024)
print('recieve time:',timestamp)    
print(f"Received data: {data.decode()}")

# Close the connection
client_socket.close()
server_socket.close()