import socket, threading

# CONSTANTS
SERVER_IP = 'localhost'
SERVER_PORT = 9000

# create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind socket to port
sock.bind((SERVER_IP, SERVER_PORT))

# set timeout
sock.settimeout(10)

# set infinite loop
serverRunning = True
while serverRunning:
    try:
        print("Waiting for connection ..")
        data, client_addr = sock.recvfrom(128)
        
        if data.decode('utf8') == 'client':
            sock.sendto(("halo dari server").encode('utf8'), client_addr)

    except socket.timeout:
        serverRunning = False
        print("Server timeout ..")
        sock.close()
        print("Shuting down server ..")