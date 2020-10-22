import socket

udpSoc = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

conn = ('', 12345)

udpSoc.bind(conn)
print("UDP socket is created and listening")

while(True):
	data,(sourceIP, port) = udpSoc.recvfrom(2048)
	print("Received Data from : {}".format(str(sourceIP)))  
	print("Received Data : {}".format(str(data)))        
	udpSoc.sendto("Data received successfully.".encode(), (sourceIP, port))
	
