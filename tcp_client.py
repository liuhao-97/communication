import socket
import datetime

def get_current_timestamp():
    now = datetime.datetime.now()
    return  now.strftime("%Y-%m-%d %H:%M:%S.%f")


# Server configuration (should match the server's configuration)
server_ip = '10.72.138.169'  # Replace with the server's IP address
server_port = 1236

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Send data
data = "Hello, Server!"
timestamp = get_current_timestamp()
message = f"{timestamp}: {data}"
client_socket.send(message.encode())

# Close the connection
client_socket.close()