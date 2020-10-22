import socket

def XOR(num1, num2):
	result = ''
	for i in range(0, len(num2)):
		s = int(num1[i]) + int(num2[i])
		
		if s == 0 or s == 2:
			result += '0'
		else:
			result += '1'
	
	count = 0
	for i in range(0, len(result)):
		if result[i] == '0':
			count += 1
		else:
			break
			
	return result[count:]


def CRC_Check(data, key):
	counter = len(key)
	new_index = 0
	prev_index = 0
	
	ans = XOR(data[:counter], key)
	
	while counter <= len(data):
		
		if ((len(key) - len(ans)) > (len(data) - counter)):
			ans += data[counter:]
			break
		else:
			prev_index = counter
			new_index = prev_index + (len(key) - len(ans))
			ans = ans + data[prev_index:new_index]
			ans = XOR(ans, key)
			counter = new_index
				
		#print("New Term......")
		#print("Ans : {}".format(ans))
		#print("New index : {} \nPrev Index : {}".format(new_index,prev_index))
		#print("Counter : {}".format(counter))
		
	if(len(ans) != (len(key) - 1)):
		ans = '0'*(len(key) - 1 - len(ans)) + ans
	
	return ans

def decode_data(data):
	global key
	result = []
	data = data[:len(data)-(len(key) - 1)]
	
	for i in range(0, len(data), 8):
		result.append(chr(int(data[i:i+8], 2)))
	
	return ''.join(map(str, result))

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("Socket creation failed with error {}".format(err))
	
port = 12345

s.bind(('', port))
s.listen(5)

key = '1001'

while True:
	c, addr = s.accept()
	print("Got connection from {}".format(addr))
	msg = c.recv(1024).decode()
	print("Binary Data : {}".format(msg))
	error = CRC_Check(msg, key)
	print("Error status : {}".format(error))
	data = decode_data(msg)
	print("Received decoded data : {}".format(data))
	c.send("Ack".encode())
	c.close()

s.close()
