cipher = open('cipher.crypt','rb').read()
def bruteforce(srand):
  bytearr = b''
  val = srand
  key = [None]*32

  charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
  for i in range(32):
    val = (val*214013+2531011) & 0xffffffff    
    ext = (val >> 16)&0x7fff
    key[i] = ord(charset[ext%61])

  for i in range(len(cipher)):
    c = key[i%32] ^ cipher[i]
    #if c > 128: return None
    if i == 0 and c != 66: return None
    if i == 1 and c != 90: return None
    if i == 2 and c != 104: return None

    bytearr += bytes([c])
  plain = open(str(srand)+'.bz2','wb')
  plain.write(bytearr)
  plain.close()
  return True
T = 1354003999
while True:

  if brute(T): print("get ", T)
  T += 1
  if (T-1354003998) % 100000 == 0:
    print(T-1354003998) 
