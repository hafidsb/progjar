import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
NAMAFILE='data.jpg'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

fp = open(NAMAFILE,'wb+')
ditulis=0

while True:
	try:
		data, addr = sock.recvfrom(1024)
		print "blok ", len(data), data[0:10]
		fp.write(data)
	except KeyboardInterrupt:
		data.close()
	
fp.close()