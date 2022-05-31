s = 'QflMn`fH,ZHVW^7c'

flag = ''

for i,c in enumerate(s):
	tmp = ord(c)
	if i < 8:
		tmp = tmp - 3 
	flag += chr(tmp+i)
print(flag)