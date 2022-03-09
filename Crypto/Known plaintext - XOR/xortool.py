from PIL import Image

f = bytearray(open("ch3.bmp", "rb").read())

key = "fallen"

for i in range(len(f)):
    f[i] = f[i] ^ ord(key[i % len(key)])

f = open("ch3_out.bmp", "wb").write(f)
ima = Image.open("ch3_out.bmp") 
ima.show()