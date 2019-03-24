import socket

# CONSTANTS
TARGET_IP = 'localhost'
TARGET_PORT = 9000

# create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(("client").encode('utf8'), (TARGET_IP,TARGET_PORT))

dari_server = sock.recv(128).decode('utf8')

print(dari_server)

sock.close()