import socket

# CONSTANTS
TARGET_IP = 'localhost'
TARGET_PORT = 9000
FILE_NAME = 'download1.jpg'

# create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set client timeout
sock.settimeout(5)

# send connection request
sock.sendto(("client").encode('utf8'), (TARGET_IP,TARGET_PORT))

# accept connection response
response_connection = sock.recv(128).decode('utf8')
print(response_connection)

# send image request
sock.sendto(("image").encode('utf8'), (TARGET_IP,TARGET_PORT))

# accept image response
img_size = int(sock.recv(128).decode('utf8'))
print(img_size)


# open to be written file
with open(FILE_NAME, 'wb+') as fo:
    data_written = 0

    while True:
        try:            
            img_data = sock.recv(64)
            fo.write(img_data)
            data_written += len(img_data)
            print("\r Received {} of {}".format(data_written, img_size))
            
            if data_written == img_size:
                print("Data received completely!")
                sock.close()
                break

        except socket.timeout:
            print("Client time out ..")
            print("Shuting down client ..")
            print(data_written, img_size)
            sock.close()
            break