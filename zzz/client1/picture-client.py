import socket

SERVER_IP = "localhost"
SERVER_PORT = 12345

file_name = "client-1.jpg"

server_addr = (SERVER_IP, SERVER_PORT)

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
sock.connect(server_addr) 
print("Connected")
    
try:
    # Open file to be ovwerwritten
    with open(file_name, 'wb+') as fp:
        file_size = sock.recv(128).decode('utf8')        
        print(file_size)

        sock.sendall(("Size recieved").encode('utf8'))
        img_file = sock.recv(int(file_size)) 

        fp.write(img_file)
        print("Image successfully received")

finally:
    sock.close()

