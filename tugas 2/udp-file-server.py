import socket

# sets constants
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
NAMAFILE='new_data.jpg'

# creates UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# binds just made socket to defined SERVER_PORT
sock.bind((SERVER_IP, SERVER_PORT))

# opens new file to be received
fp = open(NAMAFILE,'wb+')

print ("Waiting")

# flag check if file has been received completely
ditulis=0

# gets image size
recv_size = int(sock.recv(128))

while True:
	# gets chunks of image data and sender address
	data, addr = sock.recvfrom(2048)

	# prints received data
	print ("blok ", len(data), data)

	# adds received image data
	fp.write(data)

	# increments written data image
	ditulis = ditulis + len(data)

	if recv_size == ditulis:
		print ("File received comletely.")
		break

fp.close()