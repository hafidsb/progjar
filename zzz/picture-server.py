from __future__ import print_function
import socket, os, sys, threading

# Debugging purpose
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs) 

# Below lies client thread handler
def handleClient(client, id):
    clientConnected = True

    while clientConnected:
        try:
            # File manipulation
            with open(file_name, 'rb') as fp:
                img = fp.read()
                conn.sendall(str(file_size).encode('utf8'))
                flag_size = conn.recv(128).decode('utf8')
                print(flag_size)
                conn.sendall(img)
                flag_disconnect = conn.recv(64).decode('utf8')
                if flag_disconnect == "Disconnected":
                    #clients.pop(id)
                    pass
        finally:            
            eprint(id, " client has been disconnected")
            clientConnected = False

# Not so random var declaration
SERVER_IP = "localhost"
SERVER_PORT = 12345
SERVER_RUNNING = True

server_addr = (SERVER_IP, SERVER_PORT)
file_name = "small.jpg"
file_size = os.stat(file_name).st_size
clients = {}
client_id = 0

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
        
        eprint("first check")
        
        # Identify clients
        if client_id == 0 or client_id+1 not in clients:
            clients[client_id+1] = client_addr
            threading.Thread(target=handleClient, args=(conn, client_id,)).start()
            client_id += 1
            eprint(client_id, clients)
            
    except socket.timeout:
        SERVER_RUNNING = False
        print("\nServer timeout \nServer is shutting down ..")
    

    
