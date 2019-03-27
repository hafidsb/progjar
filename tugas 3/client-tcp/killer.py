import socket

# CONSTANTS
TARGET_IP = 'localhost'
TARGET_PORT = 9000
SERVER_ADDR = (TARGET_IP, TARGET_PORT)

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
sock.connect(SERVER_ADDR)

# initiate client connection
sock.sendall(("Kill server").encode('utf8'))
print("Target taken down successfully!")
sock.close()