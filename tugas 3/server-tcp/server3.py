import socket, threading

# threads
class clientHandler(threading.Thread):
    def __init__(self, threadID, conn, sock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.conn = conn
    
    def run(self):
        print("Thread {} is running".format(self.threadID))
        handleClient(self.threadID, self.conn, sock)

# functions
def handleClient(id, conn, sock):
    conn.sendall(("Server is ready").encode('utf8'))
    bothConnected = True    

    try:
        while bothConnected:
            # while a client connects, remove socket timeout
            # sock.settimeout(None)
            
            client_request = conn.recv(128).decode('utf8')

            if client_request == "ENDCON":                
                print("Client ended the connection")
                bothConnected = False

            else: 
                print(client_request)
    
    except socket.timeout:
        print("Thread timeout ..")
    
    finally:
            print("Client disconnected ..")
            print("Closing connection with client {} ..".format(id))
            
            # after a client disconnects reset socket timeout to default            
            sock.settimeout(3)
            print(sock.gettimeout())
            conn.close()

# CONSTANTS
SERVER_IP = 'localhost'
SERVER_PORT = 9000

# variables
serverRunning = True
clientCount = 0
clients = []
flag_conn = 0

# create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set default timeout
sock.settimeout(3)

# bind socket to port
sock.bind((SERVER_IP, SERVER_PORT))
print("Starting up on {} on port {}".format(SERVER_IP, SERVER_PORT))

# limit total connection
sock.listen(0)

while serverRunning:
    try:
        # waiting for client connection
        print("Waiting for a connection ..")
        conn, client_addr = sock.accept()
        
        print("choochoo")

        # set conn status
        flag_conn = 1

        # connection established
        print("Connection from {}".format(client_addr))
        
        # client initial response check
        request = conn.recv(128).decode('utf8')
        if request == "Client":
            clients.append(clientHandler(clientCount+1, conn, sock))
            clients[clientCount].start()
            clientCount += 1
            print("Jumlah klien {}".format(clientCount))

        else:
            print("Invalid response: {}".format(request))
    
    except socket.timeout:
        if flag_conn:
            conn.close()
        sock.close()        
        serverRunning = False
        
        print("Server timeout ..")
        print("Shutting down server ..")
        


        
    
        