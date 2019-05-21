import socket

TARGET_IP = "localhost"
TARGET_PORT = 9000
SERVER_ADDR = (TARGET_IP, TARGET_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(SERVER_ADDR)
print("Connected")

connectedToServer = True
while connectedToServer:
    try:
        req = input()
        sock.sendall(req.encode('utf8'))

        resp = sock.recv(128).decode('utf8')
        print(resp)

        if resp == "Closing connection":
            connectedToServer = False
            sock.close()

    except KeyboardInterrupt:
        print("Client interrupted")
        connectedToServer = False
        sock.sendall(("exit").encode('utf8'))
        sock.close()
    