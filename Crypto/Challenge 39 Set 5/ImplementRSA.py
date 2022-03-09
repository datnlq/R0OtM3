#!/bin/env/ python 3

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

#Sau do RSA Implement

p = 47 
q = 53 
n = p * q
phi = (p - 1) * (q - 1)
e = 3
d = inverse(e, phi)


s = 2001
encrypted = pow(s, e, n)
decrypted = pow(encrypted, d, n)
assert decrypted == s