import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_addr = ('localhost', 1234)

print >>sys.stderr, 'Starting up on %s on port %s' % server_addr
sock.bind(server_addr)

# Listen for incoming connections(5 Max)
sock.listen(5)

while True:
	# Wait for a connection
	print >>sys.stderr, 'Waiting for a connection'

	conn, client_addr = sock.accept()
	print >>sys.stderr, 'Receiving connection from ', client_addr 

	# Receive the data in small chunks and retransmit it
	while True:
		data = conn.recv(32)

		if data:
			conn.sendall(data)
		else:
			print 'No more data'
			break
	
	# Clean up the connection
	conn.close()