import base64
from Crypto.Cipher import AES


with open('7.txt') as fh:
	c = base64.b64decode(fh.read())

key = b'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(c)
print(plaintext)