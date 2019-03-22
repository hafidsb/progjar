import socket

SERVER_IP = "localhost"
SERVER_PORT = 8080
FILENAME = "client-1.jpg"

server_addr = (SERVER_IP, SERVER_PORT)

# creates TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connects the socket to the port where the server is listening
sock.connect(server_addr) 
print("Connected")

# gets image size
img_size = int(sock.recv(128))

# opens new file to be received
fp = open(FILENAME,'wb+')

# flag check if file has been received completely
ditulis=0
