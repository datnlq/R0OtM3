#!/urs/bin/env python3.5
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from binascii import *
import base64
import binascii

cipher = int(hexlify(base64.b64decode("e8oQDihsmkvjT3sZe+EE8lwNvBEsFegYF6+OOFOiR6gMtMZxxba/bIgLUD8pV3yEf0gOOfHuB5bC3vQmo7bE4PcIKfpFGZBA")),16)
publickeyy = """-----BEGIN PUBLIC KEY-----
MGQwDQYJKoZIhvcNAQEBBQADUwAwUAJJAMLLsk/b+SO2Emjj8Ro4lt5FdLO6WHMM
vWUpOIZOIiPu63BKF8/QjRa0aJGmFHR1mTnG5Jqv5/JZVUjHTB1/uNJM0VyyO0zQ
owIDAQAB
-----END PUBLIC KEY-----"""

key = RSA.importKey(publickeyy) #https://www.dlitz.net/software/pycrypto/api/2.6/Crypto.PublicKey.RSA-module.html
n = int(key.n)
e=int(key.e) #65537
#print(n)

#Using http://factordb.com/ to find q,p from n
p=398075086424064937397125500550386491199064362342526708406385189575946388957261768583317

q=472772146107435302536223071973048224632914695302097116459852171130520711256363590397527

M=(p-1)*(q-1)

d=inverse(e,M)



plaintext = pow(cipher,d,n)
print(plaintext)


original = long_to_bytes(plaintext)
print(original) #b'\x02\x15\x9b\x07@\x1a]\xfe\x93&\xa7\xa8\xdcTq\xed\x8d?\x93\xa6V\x16\xdb\t\x16\xae\xcf\x132U\x02T\xfe\xd5Ae"h\x9eGk\x02\x14\x1d\xee`R!\x86\xe0`e\xff\xd8\xf0\x00up2l6DnaIhZgxA\n'

#up2l6DnaIhZg