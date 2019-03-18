import socket
import os

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

namafile="small.jpg"
ukuran = os.stat(namafile).st_size

fp = open(namafile,'rb')
k = fp.read()
terkirim=0
for x in k:
	sock.sendto(str(ukuran), (TARGET_IP, TARGET_PORT))
	sock.sendto(x, (TARGET_IP, TARGET_PORT))
	terkirim = terkirim + 1
	print "\r terkirim {} of {} " . format(terkirim,ukuran)