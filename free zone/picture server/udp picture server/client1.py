import socket

# CONSTANTS
TARGET_IP = 'localhost'
TARGET_PORT = 9000
FILE_NAME = 'download1.jpg'
FILE_NAME_2 = 'download2.jpg'

# create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set client timeout
sock.settimeout(5)

# send connection request
sock.sendto(("client").encode('utf8'), (TARGET_IP,TARGET_PORT))

# accept connection response
response_connection = sock.recv(128).decode('utf8')
print(response_connection)

# first image handler
with open(FILE_NAME, 'wb+') as fo:
    # send image request
    sock.sendto(("image").encode('utf8'), (TARGET_IP,TARGET_PORT))

    # accept image response
    img_size = int(sock.recv(128).decode('utf8'))
    print(img_size)

    data_written = 0

    while True:
        try:            
            img_data = sock.recv(64)
            fo.write(img_data)
            data_written += len(img_data)
            print("\r Received {} of {}".format(data_written, img_size))
            
            if data_written == img_size:
                print("First image data received completely!")
                print("Preparing for the 2nd image ..")
                break

        except socket.timeout:
            print("Client time out ..")
            print("Shuting down client ..")
            print(data_written, img_size)
            sock.close()
            break
# send 2nd connection request
sock.sendto(("client2").encode('utf8'), (TARGET_IP,TARGET_PORT))

# accept 2nd connection response
response_connection = sock.recv(128).decode('utf8')
print(response_connection)

# second image handler
with open(FILE_NAME_2, 'wb+') as fo:
    # send 2nd image request
    sock.sendto(("image2").encode('utf8'), (TARGET_IP,TARGET_PORT))

    # accept 2nd image response
    img_size2 = int(sock.recv(128).decode('utf8'))
    print(img_size2)

    data_written = 0
    
    while True:
        try:
            img_data = sock.recv(64)
            fo.write(img_data)
            data_written += len(img_data)
            print("\r Received {} of {}".format(data_written, img_size2))

            if data_written == img_size2:
                print("Secdond image data received completely!")
                print("Exiting client ..")
                sock.close()
                print("Client exited successfully!")
                break

        except socket.timeout:
            print("Client time out ..")
            print("Shuting down client ..")
            sock.close()
            break