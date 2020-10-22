import socket

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("Socket creation failed with error {}".format(err))
	
port = 12345

s.connect(('127.0.0.1', port))

msg = input('Enter your message : ')
s.send(msg.encode())
print(s.recv(1024).decode())

s.close()
