def check1(input,num):
	t = input
	for i in range(1,100):
		t = t - i
	return t
	
def check2(input,num):
	t = input
	if num % 2 == 0:
		for i in range(1,1000):
			t = t -i
		return t
	for i in range(1,1000):
		t = t + i
	return t
def check3(input,num):
	t = input
	for i in range(1,10000):
		t = t -i
	return t
	
	
target = 1835996258
for i in range(2,100):
	if 2*i%3 == 0:
		target = check1(target,i-1)
	elif 2*i%3 == 1:
		target = check2(target,i-1)
	else :
		target = check3(target,i-1)
		
print(target)