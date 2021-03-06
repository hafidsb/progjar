import socket, os, threading, time

# CONSTANTS
SERVER_IP = 'localhost'
SERVER_PORT = 9000
IMAGE_FORMAT = ['jpg', 'png', 'gif']
IMAGE_STASH = []

# scan image in Images folder 
with os.scandir('Images') as images:
    for img in images:
        # only scan image format
        if img.name[-3:] in IMAGE_FORMAT:
            IMAGE_STASH.append("Images/" + img.name)

# threads
class clientThread(threading.Thread):
    def __init__(self, threadID, client_addr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.client_addr = client_addr
    
    def run(self):
        print("Connection from {}".format(self.client_addr))
        handleClient(self.client_addr, self.threadID)

# functions
def handleClient(addr, id):    
    sock.sendto(("Request accepted, sending image").encode('utf8'), addr)

    for i in range(len(IMAGE_STASH)):
        with open(IMAGE_STASH[i], 'rb') as fopen:
            # send file name
            sock.sendto(IMAGE_STASH[i].encode('utf8'), addr)
            
            # send file size
            size = os.stat(IMAGE_STASH[i]).st_size
            sock.sendto(str(size).encode('utf8'), addr)

            # send client details
            sock.sendto(str(id).encode('utf8'), addr)
            
            # sending data
            data = fopen.read(5)
            data_sent = 0
            while data:
                sock.sendto(data, addr)
                data_sent += len(data)
                data = fopen.read(5)

        print("Successfully sent {} image to {}".format(i+1, addr))

        # send file sending status
        if i < len(IMAGE_STASH) - 1:
            sock.sendto("Masih".encode('utf8'), addr)

    sock.sendto("Kelar".encode('utf8'), addr)



# variables
serverRunning = True
clientCount = 0
clients = []

# create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind socket to port
sock.bind((SERVER_IP, SERVER_PORT))

# set timeout
sock.settimeout(10)

while serverRunning:
    try:
        print("Waiting for connection ..")

        # accept connection request
        request, client_addr = sock.recvfrom(128)

        if request.decode('utf8') == "client":
            # starting thread            
            clients.append(clientThread(clientCount+1, client_addr))
            clients[clientCount].start()
            clientCount += 1

        else:
            print("Invalid response: {}".format(request.decode('utf8')))

    except socket.timeout:
        serverRunning = False
        print("Server timeout ..")
        sock.close()
        print("Shutting down server ..")