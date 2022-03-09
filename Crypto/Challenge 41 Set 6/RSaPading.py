#!bin/enc python3

from Crypto.Util.number import *

n = 3233
e=17
d= 413
m = 2001

c = pow(m,e,n)

#C2 = ((S**E mod N)*C) mod N => C1 = s^e mod n
c1 = pow(510,e,n)

c2 = pow((c * c1) % n, d, n)
#print(c)

pl = (c2*inverse(510,n))%n 

print(pl)#2001



