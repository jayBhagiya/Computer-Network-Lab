import socket

udpSoc = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

destination = ('127.0.0.1', 12345)

buff = input('Enter message to send : ')
udpSoc.sendto(buff.encode(), destination)

msg = udpSoc.recvfrom(2048)
print("Received message : {}".format(str(msg)))
