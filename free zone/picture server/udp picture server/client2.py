import socket, os, errno

# CONSTANTS
TARGET_IP = 'localhost'
TARGET_PORT = 9000
FILE_NAME = 'download1.jpg'
FILE_NAME_2 = 'download2.jpg'
BASE_NAME = '%s/new_%s'

# variables
clientRunning = True

# create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set client timeout
sock.settimeout(5)

# initiate client connection
sock.sendto(("client").encode('utf8'), (TARGET_IP,TARGET_PORT))

while clientRunning:
    try:
        response = sock.recv(128).decode('utf8')

        if response == "Request accepted, sending image":
            sendingImage = True
            while sendingImage:
                # waiting for iamge details            
                file_name = sock.recv(128).decode('utf8')
                file_size = int(sock.recv(128).decode('utf8'))

                print(file_name, file_size)
                data_written = 0
                client_id = "client" + sock.recv(32).decode('utf8')
                image_name = BASE_NAME % (client_id, file_name)
                
                if not os.path.exists(os.path.dirname(image_name)):
                    try:
                        os.makedirs(os.path.dirname(image_name))
                    except OSError as exc:
                        if exc.errno != errno.EEXIST:
                            raise
                
                with open(image_name, 'wb+') as fopen:
                    while True:
                        img_data = sock.recv(64)
                        fopen.write(img_data)
                        data_written += len(img_data)

                        if data_written == file_size:
                            print("Image '{}' received successfully!".format(file_name))                            
                            break
                sending_status = sock.recv(128).decode('utf8')
                if sending_status == "Masih":
                    pass
                elif sending_status == "Kelar":
                    sock.close()
                    sendingImage = False

            print("All images received successfully!")
            print("Shutting down client ..")
            clientRunning = False
        else:
            print(response)

    except socket.timeout:
        print("Connection timed out ..")
        print("Shutting down client ..")
        clientRunning = False