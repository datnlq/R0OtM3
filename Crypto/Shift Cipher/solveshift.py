#Readfile

f = open("ch7.bin",'r')

cipher = f.read()

flag = "" 
for c in range(50):
	for i in cipher:
		flag += chr(ord(i)-c)
	print(flag,"\n") 
 
