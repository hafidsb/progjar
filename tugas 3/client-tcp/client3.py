import socket, os, errno

# CONSTANTS
TARGET_IP = 'localhost'
TARGET_PORT = 9000
SERVER_ADDR = (TARGET_IP, TARGET_PORT)
BASE_NAME = '%s/new_%s_%s'

# variables
isConnected = True
bothConnected = True

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
sock.connect(SERVER_ADDR)

# main
try:
    while isConnected:
        response = sock.recv(128).decode('utf8')

        if response == "Server is ready":
            while bothConnected:
                request = input()
                sock.sendall(request.encode('utf8'))

                if request == "exit":
                    bothConnected = False
                    isConnected = False

                elif request == "download all":
                    sendingFiles = True
                    while sendingFiles:
                        # waiting for iamge details            
                        file_name = sock.recv(128).decode('utf8')
                        file_name = file_name.replace('storage/', '')
                        print(file_name)
                        file_size = int(sock.recv(128).decode('utf8'))

                        # image metadata
                        data_written = 0
                        print(file_size)
                        client_id = "client" + sock.recv(32).decode('utf8')
                        file_name = BASE_NAME % (client_id, client_id, file_name)
                        
                        # create directory if not exist
                        if not os.path.exists(os.path.dirname(file_name)):
                            try:
                                os.makedirs(os.path.dirname(file_name))
                            except OSError as exc:
                                if exc.errno != errno.EEXIST:
                                    raise
                        
                        # open file to be written
                        with open(file_name, 'wb+') as fopen:                            
                            file_data = sock.recv(file_size)
                            fopen.write(file_data)
                            print("Image '{}' received successfully!".format(file_name))                            

                        # receive image delivery status            
                        sending_status = sock.recv(128).decode('utf8')
                        print(sending_status)
                        if sending_status == "Masih":
                            pass
                        elif sending_status == "Kelar":
                            sock.close()
                            sendingFiles = False
                else:                    
                    print(request)
        else:
            print(response)

except KeyboardInterrupt:
    print("\nConnection interrupted ..")

finally:
    sock.close()
    print("\nShutting down client ..")  