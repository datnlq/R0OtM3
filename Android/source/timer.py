def is2(n):
	if(n <= 3):
		if (n > 1):
			return True
		return False
	elif (n % 2 == 0 or n % 3 ==0):
		return False
	else:
		i = 5 
		while (i * i <= n):
			if(n % i == 0 or n % (i + 2) == 0):
				return False
			i += 6
		return True
		
time = 200000
k = 0 
while time > 0:
	if is2(time):
		k += 100
	else:
		k-= 1
	time -= 1

print(k)
		
