import socket

checksumSize = 8

def onesComplement(num):
	maxlen = len(num)
	for i in range(0, maxlen, 1):
		if(num[i] == 0):
			num[i] = 1;
		else:
			num[i] = 0;
	
	return ''.join(map(str, num))


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

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("Socket creation failed with error {}".format(err))
	
port = 12345

s.connect(('127.0.0.1', port))

msg = input('Enter your message : ')
nData = ''
sum1 = '0'*checksumSize

for i in msg:
	cr = format(ord(i), 'b')
	if(len(cr)%8 != 0):
		cr = '0'*(8 - (len(cr)%8)) + cr
	
	sum1 = addBin(sum1, cr, 0)
	nData += cr

sum1 = onesComplement(sum1)
nData += sum1
print("Converted Binary msg to send : {}".format(nData))

s.send(nData.encode())
print("From server : {}".format(s.recv(1024).decode("utf-8")))
s.close()

