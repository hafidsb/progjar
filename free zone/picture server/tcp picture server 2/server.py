import socket, os

SERVER_IP = "localhost"
SERVER_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((SERVER_IP,SERVER_PORT))
sock.listen(1)
sock.settimeout(10)

print("Waiting for connection")
conn, client_addr = sock.accept()
print("Connected to {}".format(client_addr))

serverRunning = True
while serverRunning:
    try:
        req = conn.recv(128).decode('utf8')

        if req == "start":
            conn.sendall(("Server service ready").encode('utf8'))

        elif req == "image":
            conn.sendall(("Here's your image").encode('utf8'))
        
        elif req == "exit":
            conn.sendall(("Closing connection").encode('utf8'))
            conn.close()
            serverRunning = False
        
        else:
            print(req)
            conn.sendall(("Request invalid").encode('utf8'))

    except socket.timeout:
        print("Server timeout")
        serverRunning = False
