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
	
	data += '0'*(len(key) - 1)
	
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

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("Socket creation failed with error {}".format(err))
	
port = 12345

s.connect(('127.0.0.1', port))

key = '1001'
msg = input("Enter message to send : ")

data = ''
for i in msg:
	cr = format(ord(i), 'b')
	if len(cr)%8 != 0:
		cr = '0'*(8 - len(cr)) + cr
		
	data += cr

code = CRC_Check(data, key)
data += code
print("CRC code {}".format(code))
print("Data converted to binary with CRC code : {}".format(data))
s.send(data.encode())
print(s.recv(1024).decode())

s.close()
