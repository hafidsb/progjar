import socket, os

SERVER_IP = "localhost"
SERVER_PORT = 12345
SERVER_RUNNING = True

server_addr = (SERVER_IP, SERVER_PORT)
file_name = "small.jpg"
file_size = os.stat(file_name).st_size

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server's socket to port
print("Starting up on {} on port {}".format(SERVER_IP, SERVER_PORT))
sock.bind(server_addr)

# Limit total connection
sock.listen(2)

# Set timeout
sock.settimeout(10)

while SERVER_RUNNING:
    try:
        # Waiting for client connection
        print("Waiting for a connection ..")
        conn, client_addr = sock.accept()
        
        # Connection established
        print("Connected to {}".format(client_addr))

        # File manipulation
        with open(file_name, 'rb') as fp:
            img = fp.read()
            conn.sendall(str(file_size).encode('utf8'))
            flag_size = conn.recv(128).decode('utf8')
            print(flag_size)
            conn.sendall(img)
    
    except socket.timeout:
        SERVER_RUNNING = False
        print("\nServer timeout \nServer is shutting down ..")
    

    
