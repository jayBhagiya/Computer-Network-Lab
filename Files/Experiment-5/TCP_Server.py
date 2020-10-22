import socket

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("Socket creation failed with error {}".format(err))
	
port = 12345

s.bind(('', port))
s.listen(5)

while True:
	c, addr = s.accept()
	print("Got connection from {}".format(addr))
	msg = c.recv(1024).decode()
	print(msg)
	c.send("Ack".encode())
	c.close()


s.close()
