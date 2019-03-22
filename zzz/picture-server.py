import socket, os

SERVER_IP = "localhost"
SERVER_PORT = 8080
SERVER_RUNNING = True
server_addr = (SERVER_IP, SERVER_PORT)

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server's socket to port
print("Starting up on {} on port {}".format(SERVER_IP, SERVER_PORT))
sock.bind(server_addr)

# Limit total connection
sock.listen(2)

while SERVER_RUNNING:
    conn, client_addr = sock.accept()
    file_name = "small.jpg"
    size = os.stat(file_name).st_size
    sock.sendall(size)

    SERVER_RUNNING = False
