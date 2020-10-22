import socket

checksumSize = 8

def onesComplement(num):
	maxlen = len(num)
	for i in range(0, maxlen, 1):
		if(num[i] == 0):
			num[i] = 1;
		else:
			num[i] = 0;
	
	return int(''.join(map(str, num)))


def addBin(num1, num2, carry):
	ans = [None]*8
	z = ''
	maxlen = max(len(num1), len(num2))
	for i in range(maxlen - 1, -1, -1):
		sum = int(num1[i]) + int(num2[i]) + carry
		if(sum == 0):
			ans[i] = 0
			carry = 0
		elif(sum == 1):
			ans[i] = 1
			carry = 0
		elif(sum == 2):
			ans[i] = 0
			carry = 1
		elif(sum == 3):
			ans[i] = 1
			carry = 1
		else:
			pass
			
	if(carry == 1):
		ans = addBin(ans, z.zfill(maxlen), 1)
		
	return ans


def Checksum_Check(msg):
	global checksum
	
	total_parts = int(len(msg)/checksumSize)
	parts_list = []
	data_list = []
	
	for i in range(0, len(msg), 8):
		parts_list.append(msg[i:i+8])
		data_list.append(chr(int(msg[i:i+8], 2)))	
	
	data_list = data_list[:total_parts-1]
		
	error = ''
	error = error.zfill(checksumSize)
	for i in range(0, total_parts, 1):
		error = addBin(parts_list[i], error, 0)
	
	error = onesComplement(error)
	print("Error : {}".format(error))
	
	data = ''.join(map(str, data_list))
	
	return error, data

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
	error,data = Checksum_Check(msg)
	
	if(error == 0):
		print("Data received successfully")
		print("Data : {}".format(data))
		c.send("ACK".encode())
	else:
		print("Data received currepted")
		c.send("NACK".encode())
	
	c.close()


s.close()
