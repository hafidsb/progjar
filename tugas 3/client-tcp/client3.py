import socket

# CONSTANTS
TARGET_IP = 'localhost'
TARGET_PORT = 9000
SERVER_ADDR = (TARGET_IP, TARGET_PORT)

# variables
clientRunning = True

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set client timeout
sock.settimeout(5)

# Connect the socket to the port where the server is listening
sock.connect(SERVER_ADDR)

# initiate client connection
sock.sendall(("Client").encode('utf8'))

# main
try:
    response = sock.recv(128).decode('utf8')

    if response == "Server is ready":
        clientRunning = True
        while clientRunning:
            request = input()              
            sock.sendall(request.encode('utf8'))

            if request == "ENDCON":
                clientRunning = False

except socket.timeout:
    print("Connection timed out ..")
    print("Shutting down client ..")
    sock.close()
    clientRunning = False

except KeyboardInterrupt:
    print("Connection interrupted ..")
    print("Shutting down client ..")
    sock.close()
    clientRunning = False

finally:
    sock.close()
    print("Shutting down client ..")  