import socket, os

# CONSTANTS
SERVER_IP = 'localhost'
SERVER_PORT = 9000
FILE_NAME_1 = 'small.jpg'
FILE_SIZE_1 = os.stat(FILE_NAME_1).st_size
FILE_NAME_2 = 'spaghett.jpg'
FILE_SIZE_2 = os.stat(FILE_NAME_2).st_size

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

        if request_image.decode('utf8') == 'image':
            # send image_size response
            sock.sendto(str(FILE_SIZE_1).encode('utf8'), client_addr)

        with open(FILE_NAME_1, 'rb') as fp:
            data = fp.read(5)
            data_sent = 0
            
            while data:
                sock.sendto(data, client_addr)
                data_sent += len(data)
                print("\r Sent {} of {}".format(data_sent, FILE_SIZE_1))
                data = fp.read(5)

        # accept 2nd connection request
        request_connection, client_addr = sock.recvfrom(128)

        if request_connection.decode('utf8') == 'client2':
            # send 2nd connection response
            sock.sendto(("Request accepted").encode('utf8'), client_addr)

        # accept 2nd image request
        request_image2, client_addr = sock.recvfrom(128)

        if request_image2.decode('utf8') == 'image2':
            # send image_size response
            sock.sendto(str(FILE_SIZE_2).encode('utf8'), client_addr)
        
        with open(FILE_NAME_2, 'rb') as fp2:
            data = fp2.read(5)
            data_sent = 0
            
            while data:
                sock.sendto(data, client_addr)
                data_sent += len(data)
                print("\r Sent {} of {}".format(data_sent, FILE_SIZE_1))
                data = fp2.read(5)

    except socket.timeout:
        serverRunning = False
        print("Server timeout ..")
        sock.close()
        print("Shuting down server ..")
