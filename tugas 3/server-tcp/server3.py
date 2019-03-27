import socket, threading, os

# threads
class clientHandler(threading.Thread):
    def __init__(self, threadID, conn, sock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.conn = conn

    def run(self):
        print("Thread {} is running".format(self.threadID))
        sock.settimeout(None)
        handleClient(self.threadID, self.conn, sock)
        sock.settimeout(0)

# functions
def downloadAll():
    pass

def handleClient(id, conn, sock):
    bothConnected = True    

    try:
        while bothConnected:
            # while a client connects, remove socket timeout
            # sock.settimeout(None)
            
            client_request = conn.recv(128).decode('utf8')

            if client_request == "exit":                
                print("\nClient ended the connection")
                bothConnected = False    

            elif client_request == "ls": 
                print(client_request)
            
            elif client_request == "download all":
                for i in range(len(STORAGE)):
                    with open(STORAGE[i], 'rb') as fopen:
                        # send file name
                        conn.sendall(STORAGE[i].encode('utf8'))
                        
                        # send file size
                        size = os.stat(STORAGE[i]).st_size
                        conn.sendall(str(size).encode('utf8'))

                        # send client details
                        conn.sendall(str(id).encode('utf8'))
                        
                        # sending data
                        conn.sendall(fopen.read())
                       

                    print("Successfully sent {} image to client-{}".format(i+1, id))
                    print(len(STORAGE), i)
                    # send file sending status
                    if i < len(STORAGE) - 1:
                        conn.sendall("Masih".encode('utf8'))

                conn.sendall("Kelar".encode('utf8'))
            
            else:
                print("Request {} from client-{}".format(client_request, id))
    
    except socket.timeout:
        print("Thread timeout ..")
    
    finally:
            print("Client disconnected ..")
            print("Closing connection with client {} ..".format(id))
            conn.close()

# CONSTANTS
SERVER_IP = 'localhost'
SERVER_PORT = 9000
STORAGE = []

# scan image in Images folder 
with os.scandir('storage') as files:
    for f in files:
        STORAGE.append("storage/" + f.name)

# variables
serverRunning = True
client_count = 0
clients = {}

# create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to port
sock.bind((SERVER_IP, SERVER_PORT))
print("Starting up on {} on port {}".format(SERVER_IP, SERVER_PORT))

# set timeout
sock.settimeout(10)

# limit total connection
sock.listen(0)

while serverRunning:
    try:
        # waiting for client connection
        print("Waiting for a connection ..")
        conn, client_addr = sock.accept()
        
        # connection established
        print("Connection from {}".format(client_addr))
        
        # send initial response
        conn.sendall(("Welcome to the picture server client-{}".format(client_count+1).encode('utf8')))
        conn.sendall(("Server is ready").encode('utf8'))

        if conn not in clients:
            clients[client_count] = clientHandler(client_count+1, conn, sock)
            clients[client_count].start()
            client_count += 1
    
    except KeyboardInterrupt:
        sock.close()        
        serverRunning = False
        
        print("\nServer interrupted ..")
        print("Shutting down server ..")
    
    except socket.timeout:
        sock.close()        
        serverRunning = False
        
        print("\nServer timeout ..")
        print("Shutting down server ..")
        


        
    
        