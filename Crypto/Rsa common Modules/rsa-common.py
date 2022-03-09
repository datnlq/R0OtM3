#!/bin/python


from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from binascii import *
import base64
import binascii


c1 = "BzFd4riBUZdFuPCkB3LOh+5iyMImeQ/saFLVD+ca2L8VKSz0+wtTaL55RRpHBAQdl24Fb3XyVg2N9UDcx3slT+vZs7tr03W7oJZxVp3M0ihoCwer3xZNieem8WZQvQvyNP5s5gMT+K6pjB9hDFWWmHzsn7eOYxRJZTIDgxA4k2w="
c2 = "jmVRiKyVPy1CHiYLl8fvpsDAhz8rDa/Ug87ZUXZ//rMBKfcJ5MqZnQbyTJZwSNASnQfgel3J/xJsjlnf8LoChzhgT28qSppjMfWtQvR6mar1GA0Ya1VRHkhggX1RUFA4uzL56X5voi0wZEpJITUXubbujDXHjlAfdLC7BvL/5+w="


publickey1 = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCtbdQAzdaO7GHXxUsVZ+FmcddA
Hrugq+azkVdfgnHu6teK3hDQlk0BdNz9LlQT3BoHXg5/g9FDv3bBwaulpQEQPlGM
UXEUnQAJ69KSVaLxHb5Wmb0vqX/qySKc8Hseqt5wbXklOrnZeHJ3Hm3mUeIplpWP
f19C6goN3bUGrrniwwIDAQAB
-----END PUBLIC KEY-----
"""
publickey2 = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCtbdQAzdaO7GHXxUsVZ+FmcddA
Hrugq+azkVdfgnHu6teK3hDQlk0BdNz9LlQT3BoHXg5/g9FDv3bBwaulpQEQPlGM
UXEUnQAJ69KSVaLxHb5Wmb0vqX/qySKc8Hseqt5wbXklOrnZeHJ3Hm3mUeIplpWP
f19C6goN3bUGrrniwwIDBTy3
-----END PUBLIC KEY-----
"""

mes1 = int(hexlify(base64.b64decode(c1)),16)
mes2 = int(hexlify(base64.b64decode(c2)),16)
print(mes1)
print(mes2)


key1 = RSA.importKey(publickey1)
key2 = RSA.importKey(publickey2)

n1 = int(key1.n)


e1 = int(key1.e)
e2 = int(key2.e)

print(e1)
print(e2)


#W311D0n3!