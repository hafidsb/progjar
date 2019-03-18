import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
NAMAFILE='new_data.jpg'

# creates UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# binds just made socket to defined SERVER_PORT
sock.bind((SERVER_IP, SERVER_PORT))

# opens new file to be received
fp = open(NAMAFILE,'wb+')

# flag check if file has been received completely
ditulis=0

while True:
	recv_size = int(sock.recv(128))
	data, addr = sock.recvfrom(1024)
	print data
	print "blok ", len(data), data[0:1]
	fp.write(data)
	ditulis = ditulis + 1

	if recv_size == ditulis:
		print "File sukses diterima."
		break

fp.close()