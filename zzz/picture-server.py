import socket, threading

SERVER_IP = "localhost"
SERVER_PORT = 8080

server_addr = (SERVER_IP, SERVER_PORT)

# TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server's socket to port
print("Starting up on {} on port {}".format(SERVER_IP, SERVER_PORT))
sock.bind(server_addr)

# Store clients
clients = {}

# Listen for clients
sock.listen(3)