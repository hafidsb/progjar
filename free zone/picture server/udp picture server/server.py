import socket, os

# CONSTANTS
SERVER_IP = 'localhost'
SERVER_PORT = 9000
FILE_NAME = 'small.jpg'
FILE_SIZE = os.stat(FILE_NAME).st_size

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
        # accept connection request
        request_connection, client_addr = sock.recvfrom(128)
        
        if request_connection.decode('utf8') == 'client':
            # send connection response
            sock.sendto(("Request accepted").encode('utf8'), client_addr)
        
        # accept image request
        request_image, client_addr = sock.recvfrom(128)

        if request_connection.decode('utf8') == 'client':
            # send image_size response
            sock.sendto(str(FILE_SIZE).encode('utf8'), client_addr)

        with open(FILE_NAME, 'rb') as fp:
            data = fp.read()
            data_sent = 0
            
            for x in data:
                sock.sendto(x, client_addr)
                data_sent += len(x)
                print("\r Sent {} of {}".format(data_sent, FILE_SIZE))

    except socket.timeout:
        serverRunning = False
        print("Server timeout ..")
        sock.close()
        print("Shuting down server ..")
