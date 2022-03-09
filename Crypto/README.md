# WriteUp Rootme.org 
     
                                     ██▒ ▒██░    
                                 ░███░ █ █ ░███▒    
                             ░███░        ▓     ███░    
                           ▓█▓       ▓█░  ▓       ▓███    
                         ██▒     ░▓█▓███  ▓   ██  █▒ ░██    
                        ██  ███  ▒░       ▓░████░██    ▓█░    
                       ██   ▒██      ███      ░▓██      ▒█    
                      ██             ░█░      ░██        ▓█    
                     ░█████████████    █     ██░          █▓    
                     ██                 █ ░██             ██    
                     ██      ░         ░██▓               ██    
                     ██  ███    ░██▓░███                 ███    
                     ▒█          ▓██▓                  ░████    
                      █▓    ░████                    ░██ ▒█    
                      ▓█████░                      ███ ███▓    
                      ▓███                      █████░ ████    
                       ▓█     ░██▓░         ▒████████░  ██    
                       ▓█      ██░▒██████████████████░  ██    
                       ▓█       ███▓██▒  ░██████████░   ██    
                       ▓█                  ░████▒       ██    
                        ░██▓           ▒█▓           ▒██░    
                           ▒██░       ██ ▒█        ██▓    
                              █▒                  █    
                              █▒  ░█    █░   █▓   █    
                              █████████████████████    
     
 ████████████▄                             ██    ███             ███    
 ██          ██  ▄████████▄   ▄████████▄  ██████ ████           ████  ▄████████▄  
 ██          ██ ██        ██ ██        ██  ██    ██  ██       ██  ██ ██        ██  
 ████████████▀  ██        ██ ██        ██  ██    ██   ██     ██   ██ ████████████ 
 ██    ███      ██        ██ ██        ██  ██    ██     ██ ██     ██ ██    
 ██       ████   ▀████████▀   ▀████████▀   ██    ██       █       ██  ▀██████████ 


----------------------------------------------------------------------------------------------------------
# 1. Challenge : Shift Cipher
//Chall : https://www.root-me.org/en/Challenges/Cryptanalysis/Shift-cipher?lang=en 

Author: Dt

Source cho chúng ta những ký tự đặc biệt trong thật rõ ràng shift cipher sẽ dời khoảng n từ 1-25 để tạo thành cipher 
=> brute force 26 lần 


## FLAG : Yolaihu




# 2. Challenge : RSA - Modules communs
//Chall : https://www.root-me.org/fr/Challenges/Cryptanalyse/RSA-Modules-communs

Author: Dt

Source của đề cho là 2 mess và 2 publicKey.
Tên challenge cũng khá rõ đây là Common Modulus Attack ....Sau khi search 7749 trang web thì tuyệt vời chúng ta đã có 1 tool hỗ trợ : RSHack :vv //https://github.com/zweisamkeit/RSHack

Việc còn lại là chúng ta chỉ cần tìm ra -n -e1 -e2 -c1 -c2 nữa thôi :<< 
Thế là chúng ta lại sử dụng thư viện 
Crypto.PublicKey :  from Crypto.PublicKey import RSA
Chúng ta sử dụng hàm importKey(publickey)  //https://www.kite.com/python/docs/Crypto.PublicKey.RSA.importKey
Chúng ta sẽ có được n,e

Sau đó sử dụng tool RSHack

## FLAG: W311D0n3!


# 3 .Challenge : RSA - Factorisation 
//Chall : https://www.root-me.org/fr/Challenges/Cryptanalyse/RSA-Factorisation

Author: Dt

Như chúng ta thấy thì chall cho chúng ta cipher: e8oQDihsmkvjT3sZe+EE8lwNvBEsFegYF6+OOFOiR6gMtMZxxba/bIgLUD8pV3yEf0gOOfHuB5bC3vQmo7bE4PcIKfpFGZBA


Publickey :-----BEGIN PUBLIC KEY-----
MGQwDQYJKoZIhvcNAQEBBQADUwAwUAJJAMLLsk/b+SO2Emjj8Ro4lt5FdLO6WHMM
vWUpOIZOIiPu63BKF8/QjRa0aJGmFHR1mTnG5Jqv5/JZVUjHTB1/uNJM0VyyO0zQ
owIDAQAB
-----END PUBLIC KEY-----

Trong python đã có hỗ trợ thư viện Crypto.PublicKey :  from Crypto.PublicKey import RSA
Chúng ta sử dụng hàm importKey(publickey)  //https://www.kite.com/python/docs/Crypto.PublicKey.RSA.importKey
Chúng ta sẽ có được n,e => q,p từ factordb 


M=(p-1)*(q-1)

d=inverse(e,M)


Cuối cùng dùng :pow(cipher,d,n) để tính toán ra flag 


Nhưng đang ở dạng long thế nên convert long_to_bytes(plaintext) 
## FLAG: up2l6DnaIhZg




# 4. Challenge: System Android lock patter
Chall: https://www.root-me.org/en/Challenges/Cryptanalysis/System-Android-lock-pattern

Author: thune
## STATEMENT
Having doubts about the loyalty of your wife, you’ve decided to read SMS, mail, etc in her smarpthone. Unfortunately it is locked by schema. In spite you still manage to retrieve system files.

You need to find this test scheme to unlock smartphone.

NB : validation password is a number (archive sha256 is 525daa911d4dddb7f3f4b4ec24bff594c4a1994b2e9558ee10329144a6657f98)

File attach: **ch17.tbz2** 

## SOLUTION
Dowdload file **ch17.tbz2** and extract it. Then, we have folder **android**.

Open terminal Linux and find the **.key** file:
> find -name "*.key"

After that, we have the path of the **gesture.key** file:
> ./data/system/gesture.key

Use **xxd** to create a hex dump of **gesture.key**
> xxd -ps ./data/system/gesture.key

And we have the hash string:
> 2c3422d33fb9dd9cde87657408e48f4e635713cb

Put this string in the https://hashes.com/en/decrypt/hash tool to decrypt SHA256. And we have 
> 2c3422d33fb9dd9cde87657408e48f4e635713cb:$HEX[010405020603070800]\
> 0`1`0`4`0`5`0`2`0`6`0`3`0`7`0`8`0`0`

## FLAG
> 145263780

# 5. Challenge: Pixel Madness
Chall: https://www.root-me.org/en/Challenges/Cryptanalysis/Pixel-Madness-86

Author: thune
## STATEMENT
> 0x3+1x1+0x1+0x1+0x7+1x2+0x15+1x1+0x8+1x1+0x8+1x1+0x1+1x1+0x1+1x1+0x1+1x1+0x1+1x1+0x3+1x1+0x1+1x1+0x3+1x1+0x1+1x4+0x2+1x1+0x25
> 0x2+1x1+0x4+1x1+0x4+1x3+0x1+1x2+0x2+1x8+0x11+1x4+0x1+1x3+0x6+1x2+0x4+1x1+0x4+1x2+0x7+1x4+0x4+1x2+0x7+1x2+0x3+1x2+0x3
> 0x3+1x1+0x2+1x1+0x2+1x1+0x11+1x2+0x2+1x3+0x7+1x1+0x4+1x2+0x2+1x2+0x7+1x1+0x6+1x1+0x2+1x1+0x4+1x3+0x1+1x1+0x4+1x1+0x2+1x1+0x2+1x1+0x3+1x1+0x2+1x3+0x2+1x2+0x3
>1x1+0x2+1x1+0x4+1x1+0x2+1x1+0x1+1x1+0x2+1x1+0x2+1x1+0x1+1x2+0x2+1x2+0x1+1x2+0x3+1x1+0x3+1x1+0x2+1x2+0x1+1x3+0x3+1x1+0x2+1x1+0x4+1x2+0x1+1x1+0x4+1x1+0x3+1x2+0x12+1x2+0x1+1x1+> 0x3+1x7+0x3
> 0x3+1x1+0x7+1x1+0x1+1x1+0x4+1x1+0x2+1x2+0x2+1x2+0x4+1x1+0x2+1x1+0x1+1x2+0x1+1x8+0x1+1x1+0x4+1x1+0x5+1x1+0x3+1x2+0x2+1x1+0x1+1x2+0x2+1x1+0x3+1x2+0x9+1x1+0x1+1x2+0x2+1x3+0x2+1x1                
> 0x7+1x1+0x4+1x1+0x4+1x1+0x1+1x1+0x1+1x7+0x3+1x1+0x1+1x2+0x3+1x1+0x1+1x6+0x1+1x1+0x3+1x1+0x2+1x1+0x14+1x2+0x8+1x1+0x10+1x2+0x3+1x2+0x1+1x1+0x1
> 0x6+1x5+0x4+1x1+0x7+1x1+0x2+1x1+0x3+1x2+0x4+1x1+0x8+1x1+0x3+1x2+0x1+1x2+0x3+1x1+0x8+1x1+0x2+1x2+0x1+1x1+0x3+1x7+0x5+1x2+0x2+1x1+0x2+1x2+0x3
> 0x1+1x1+0x2+1x1+0x1+1x2+0x5+1x1+0x6+1x2+0x3+1x1+0x2+1x1+0x1+1x2+0x20+1x8+0x1+1x1+0x1+1x1+0x4+1x2+0x3+1x1+0x2+1x2+0x3+1x2+0x7+1x2+0x3+1x2+0x4
> 0x2+1x1+0x3+1x5+0x5+1x2+0x7+1x1+0x4+1x2+0x2+1x1+0x2+1x2+0x1+1x1+0x3+1x1+0x6+1x2+0x2+1x2+0x3+1x2+0x2+1x3+0x1+1x1+0x6+1x3+0x3+1x5+0x3+1x1+0x4+1x1+0x5
> 0x4+1x2+0x3+1x2+0x3+1x1+0x5+1x2+0x2+1x1+0x1+1x1+0x1+1x1+0x1+1x2+0x9+1x1+0x3+1x1+0x2+1x1+0x1+1x1+0x2+1x1+0x1+1x2+0x2+1x1+0x2+1x1+0x1+1x1+0x4+1x3+0x1+1x1+0x2+1x2+0x3+1x2+0x3+1> x1+0x5+1x1+0x4+1x1+0x2
> 0x6+1x5+0x4+1x1+0x1+1x1+0x2+1x2+0x6+1x1+0x1+1x7+0x4+1x3+0x3+1x1+0x4+1x1+0x2+1x2+0x4+1x1+0x6+1x1+0x6+1x8+0x3+1x1+0x5+1x1+0x7
> 0x2+1x1+0x3+1x6+0x4+1x1+0x1+1x3+0x4+1x1+0x2+1x2+0x4+1x1+0x5+1x1+0x2+1x1+0x3+1x2+0x3+1x1+0x2+1x3+0x1+1x1+0x2+1x2+0x3+1x3+0x2+1x3+0x9+1x1+0x4+1x2+0x7+1x2

> ###### Clue :
> 0 = #FFFFFF\
> 1 = #000000

(Submit password in CAPITAL LETTERS)

## SOLUTION

Based on Clue: 
> 0 = #FFFFFF\
> 1 = #000000

Convert pixels to corresponding color . Example: *0x6* have 0 => write 6 pixels ###### White 
```
pixels = []

for row in ImageP:
    row = row.split('+')
    step = 0
    for colum in row:
        colum = colum.split('x')
        # Drawing White color 
        if colum[0] == '0':
            for i in range(int(colum[1])):
                step += 1
                pixels.append((255,255,255))
                if step == 100:
                    break
            
                
        #Drawing Black color
        else:
            for i in range(int(colum[1])):
                step += 1
                pixels.append((0,0,0))
```
Export and show the picture:
```
image_out = Image.new("RGB", (100, len(ImageP)), "white")
image_out.putdata(pixels)
image_out.save('Solve.png')
image_out.show()
```
Use the code in [**pixel.py**](https://github.com/AnhDungDoan/Cryptanalysis/blob/main/Pixel%20Madness/Pixel_Madness.py) to gain plaintext.

## FLAG
![Test Image ](https://github.com/AnhDungDoan/Cryptanalysis/blob/main/Pixel%20Madness/Solve.png)
> SOLUTION

# 6. Monoalphabetic substituation - Caesar
Chall: https://www.root-me.org/en/Challenges/Cryptanalysis/Monoalphabetic-substitution-Caesar

Author: thune

## STATEMENT

We just caught the messenger of the Emperor. He transmitted a coded message to his son. This could be an important message. You’ve to decrypt it ! To validate, you must enter the concatenation of the first letters of each line followed by the concatenation of the last letters of each line (for example : tfhqdlhfpkmeokgq).

tm bcsv qolfp\
f'dmvd xuhm exl tgak\
hlrkiv sydg hxm\
qiswzzwf qrf oqdueqe\
dpae resd wndo\
liva bu vgtokx sjzk\
hmb rqch fqwbg\
fmmft seront sntsdr pmsecq

## SOLUTION

Use the https://www.dcode.fr/caesar-cipher tool to brute-force attack. Then, we have 26 different plaintexts. Copy all of plaintext to https://translate.google.com/. Some words are discovered to be French. And we can see no one plaitext of 26 plaintext is a clear plaintext. But, some words of each plaintext can translate to French. Gather all of those words together. Go to Google, search and we can relize it is a novel - **Un, deux, trois**

**U**n, deux, troi**s**, \
**j**'irai dans les boi**s**\
**Q**uatre, cinq, si**x**,\
**c**ueillir des cerise**s**.\
**S**ept, huit, neu**f**,\
**d**ans un panier neu**f**.\
**D**ix, onze, douz**e**,\
**e**lles seront toutes rouge**s**.

## FLAG
> ujqcsddessxsffes

# 7. Encoding - UU
https://www.root-me.org/fr/Challenges/Cryptanalyse/Encodage-UU \
Author: gnudnaod

## SOLUTION

```
/*
    author: gnudnaod
    create: ..............
*/

#include <bits/stdc++.h>
#define F(i,a,b) for (int i = a; i <= b; i++)
#define _F(i,a,b) for (int i = a; i >= b; i--)
#define ll long long
#define push_back pb

using namespace std;

const int maxn = 100;

int base = 32;
char cipher[200];

void solve()
{
    int n = strlen(cipher);
    int c = 0;
    for (int i = 1; i < n; i += 4)
    {
        char x, y, z;
        x = ((cipher[i] - base) << 2) + ((cipher[i + 1] - base) >> 4);
        y = ((cipher[i + 1] - base) << 4) + ((cipher[i + 2] - base) >> 2);
        z = ((cipher[i + 2] - base) << 6) + ((cipher[i + 3] - base));

        cout << x << y << z;
        c += 3;
        if (c > (cipher[0] - base)) return;
    }
}

int main()
{
    // please remove all space in ciphertext before decode 

    cout << "Enter ciphertext to decode: ";
    cin >> cipher;
    solve();
    return 0;
}
```

## FLAG
> ULTRASIMPLE


# 8. Encoding - ASCII
https://www.root-me.org/en/Challenges/Cryptanalysis/Encoding-ASCII \
Author: gnudnaod

## SOLUTION
convert plaintext from hex code to ascii code, use ascii table to find flag! \

```
/*
    author: gnudnaod
    create: ..............
*/

#include <bits/stdc++.h>
#define F(i,a,b) for (int i = a; i <= b; i++)
#define _F(i,a,b) for (int i = a; i >= b; i--)
#define ll long long
#define push_back pb

using namespace std;

const int maxn = 100;

int n;
char plain[100];
int num[300];

int phepthuatwinxenchantic(char x)
{
    if (x >= '0' && x <= '9') return int(x) - 48; else return int(x) - 55;
}

void solve()
{

    int len = strlen(plain); 
    for (int i = 0; i < len; i+=2)
    {
        int asc = phepthuatwinxenchantic(plain[i]) * 16 + phepthuatwinxenchantic(plain[i + 1]);
        cout << char(asc);
    }
    
}

int main()
{  
    cin >> plain;
    solve();
    return 0;
}
```

## FLAG
> 2ac376481ae546cd689d5b91275d324e

# 9. Known plaintext - XOR
https://www.root-me.org/en/Challenges/Cryptanalysis/Known-plaintext-XOR \
Author: gnudnaod \

Use `xor tool` to find the key: 'fallen'

```
from PIL import Image

f = bytearray(open("ch3.bmp", "rb").read())

key = "fallen"

for i in range(len(f)):
    f[i] = f[i] ^ ord(key[i % len(key)])

f = open("ch3_out.bmp", "wb").write(f)
ima = Image.open("ch3_out.bmp") 
ima.show()
```

## FLAG
> ICONOCLASTE

# 10. File - Insecure storage 1 
https://www.root-me.org/en/Challenges/Cryptanalysis/File-Insecure-storage-1 \
Author: gnudnaod

## SOLUTION
Pull [this](https://github.com/unode/firefox_decrypt) to decrypt. \
Prerequisites: your computer is installed Mozilla \

## FLAG 
> F1rstP4sSw0rD


# 11. Service - Timing attack
https://www.root-me.org/en/Challenges/Cryptanalysis/Monoalphabetic-substitution-Polybe \
Author: gnudnaod \

## SOLUTION
Approach: when compare a correct char, time increase ~ 0,5s
```
from pwn import *
import time, string
st = time.time()
p = remote("challenge01.root-me.org", 51015)
print(p.recvline())


def timing_test(s):
    st = time.time()
    p.sendline(s)
    p.recvline()
    return time.time()-st


key = ''
for i in range(12):
    for c in string.printable:
        print(c)
        if timing_test(key+c) >= 0.5*(len(key)+1):
            if timing_test(key+c) >= 0.5*(len(key)+1):
                if timing_test(key+c) >= (len(key)+1):
                    key += c
                    break
    print(key)
```
## FLAG
> 30467-132630

# 12. Polyalphabetic substitution - Vigenère
Challenge: https://www.root-me.org/en/Challenges/Cryptanalysis/Polyalphabetic-substitution-Vigenere \
Author: nh4ttruong

## SOLUTION
- Sử dụng https://dcode.fr/vigenere-cipher ta được:
+ KEY = THEMENTOR
+ PLAINTEXT: "THEMENTOR THEHACKERMANIFESTOUNAUTRESESTFAITPRENDREAUJOUR...."
- Sử dụng phương pháp OSINT bằng cách kết hợp một vài từ khóa quan trọng trong output và key (thehackerman, thementor) và KEY để kiểm tra các tác phẩm, các bài báo,.... và nhận thấy tác phẩm "Hacker Manifesto" của tác giả Loyd Blankenship phù hợp với những gì suy đoán
- Kiểm thử thấy đúng

## FLAG
> Loyd Blankenship

# 13. Transposition - Rail Fence
Challenge: https://www.root-me.org/en/Challenges/Cryptanalysis/Transposition-Rail-Fence \
Author: nh4ttruong

## SOLUTION
- Như tên của challenge, ta thấy được challenge sử dụng Rail Fence Cipher
- Sử dụng https://www.dcode.fr/rail-fence-cipher để brute-force
- Nhận thấy RAIL = 8
- Kiểm thử thấy đúng 

## FLAG
> Will invade Kentucky on October the eighth. signal is "Frozen chicken".

# 14. ELF64 - PID encryption
Challenge: https://www.root-me.org/en/Challenges/Cryptanalysis/ELF64-PID-encryption \
Author: gnudnaod

## SOLUTION
- In process code, we can guess that if we print an interger equal to pid in os, we can access to server bash
- Run this command:
```
./ch21 $(python -c 'import os,crypt; print crypt.crypt(str(os.getpid()+1), "$1$awesome")')
```
then ls -a to cat the psswd

## FLAG
> -/q2/a9d6e31D

# 15.Initialisation Vector
Challenge: https://www.root-me.org/en/Challenges/Cryptanalysis/Initialisation-Vector
Authỏ: gnudnaod

## SOLUTION
In AES CBC mode:

Decryption mode :

P[i] = Dk(C[i]) XOR C[i-1]
C[0] = IV

=> C[0] = IV = Dk(C[1]) XOR P[1].
```
from Crypto.Cipher import AES
import base64
Plain = 'Marvin: "I am at a rough estimat' #first 32 bytes
Cipher = base64.b64decode('cY1Y1VPXbhUqzYLIOVR0RhUXD5l+dmymBfr1vIKlyqD8KqHUUp2I3dhFXgASdGWzRhOdTj8WWFTJPK0k/GDEVUBDCk1MiB8rCmTZluVHImczlOXEwJSUEgwDHA6AbiCwyAU58e9j9QbN+HwEm1TPKHQ6JrIOpdFWoYjS+cUCZfo/85Lqi26Gj7JJxCDF8PrBp/EtHLmmTmaAVWS0ID2cJpdmNDl54N7tg5TFTrdtcIplc1tDvoCLFPEomNa5booC')[:32]
Key = base64.b64decode('AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRqrHB0eHyA=')
aes = AES.new(Key, AES.MODE_ECB)
estimate = aes.decrypt(Cipher)
print(estimate)
for i in range(32):
  print(chr(estimate[i]^ord(Plain[i])),end='')

"""
In AES CBC mode:

Decryption mode :

P[i] = Dk(C[i]) XOR C[i-1]
C[0] = IV

=> C[0] = IV = Dk(C[1]) XOR P[1].
"""
```
# FLAG
> I_l0v3_Crypt0_:)

# 16. Monoalphabetic substitution - Polybe
Challenge: https://www.root-me.org/en/Challenges/Cryptanalysis/Monoalphabetic-substitution-Polybe \
Author: nh4ttruong

## SOLUTION
- Polybius Tool -> Monoalphabetic Tool (sử dụng https://dcode.fr)
- Thử dịch và sắp xếp các chữ cái thấy không có gì đặc biệt. Tuy nhiên, khi lướt xuống cuối challenge thấy có 1 dòng đơn và có ký tự "\" nên thử dịch thử bằng tiếng Pháp.
- Được dòng chữ PASSMOTDEPASSECPAAOURBHPYPGFO
- Phân tích theo tiếng Pháp 7749 lần ta được dòng có nghĩa: PASS MOT DE PASSE: CPAAOURBHPYPGFO
- Kiểm thử thấy không đúng, thử convert sang lower => đúng =)))

## FLAG
> cpaaourbhpypgfo

# 17. Challenge 1 Set 1 - The Cryptopals Crypto Challenges
Challenge: https://cryptopals.com/sets/1/challenges/1 \
Author: nh4ttruong

## SOLUTION:
- Convert HEX to BASE64

## FLAG
> SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

# 18. Challenge 2 Set 1 - The Cryptopals Crypto Challenges
Challenge: https://cryptopals.com/sets/1/challenges/2 \
Author: gnudnaod

## SOLUTION:
- Xor it!
```
def fixed_xor(buf1: bytes, buf2: bytes) -> bytes:
    if len(buf1) != len(buf2):
        raise ValueError

    xored = bytearray()
    for x,y in zip(buf1, buf2):
        xored.append(x^y)

    return bytes(xored)
```
### FLAG
> 746865206b696420646f6e277420706c6179 = "hit the bull's eye", "the kid don't play"

# 19. Challenge 3 Set 1 - The Cryptopals Crypto Challenges
Challenge: https://cryptopals.com/sets/1/challenges/3 \
Author: nh4ttruong

## SOLUTION:
- Sử dụng XOR CipherDecoder (dcode.fr) brute-force

## FLAG
> "Cooking MC's like a pound of bacon"

# 20. Challenge 4 Set 1 - The Cryptopals Crypto Challenges
Challenge: https://cryptopals.com/sets/1/challenges/4 \
Author: gnudnaod

## SOLUTION:
- In challenge 3, i found the key with score by frequency table keys is "x", so we can reuse the same code to score the possible plaintexts obtained from all the ciphertexts.
- Key = 35(in hex) -> 53(in dec)
```
import sys
import binascii

f = open("s1c4.txt", "r")
d = f.read().splitlines()

sys.stdout = open("out.txt", "w")

def single_byte_xor(text: bytes, key: int) -> bytes:

    return bytes([b ^ key for b in text])

for line in d:
    #hexline = bytearray.fromhex(line)
    print(single_byte_xor(bytearray.fromhex(line), 53))
```

## FLAG:
> Now that the party is jumping

# 21. Challenge 5 Set 1 - The Cryptopals Crypto Challenges
Challenge: https://cryptopals.com/sets/1/challenges/5 \
Author: nh4ttruong


## SOLUTION:
- Sử dụng XOR CipherDecoder (dcode.fr) 
- KEY = ICE
- plaintext output là HEX

## FLAG:
> 0B 36 37 27 2A 2B 2E 63 62 2C 2E 69 69 2A 23 69 3A 2A 3C 63 24 20 2D 62 3D 63 34 3C 2A 26 22 63 24 27 27 65 27 2A 28 2B 2F 20 43 0A 65 2E 2C 65 2A 31 24 33 3A 65 3E 2B 20 27 63 0C 69 2B 20 28 31 65 28 63 26 30 2E 27 28 2F

# 22. Challenge : Code - Pseudo Random Number Generator
//Chall : https://www.root-me.org/en/Challenges/Cryptanalysis/Code-Pseudo-Random-Number-Generator 

Author: Dt

 Khi tải source challenge về ta thấy có 2 file 1 file là code c 1 file là cipher đã được mã hóa. Sau khi đọc qua code và tham khảo 1 số writeup trên mạng thì mình nhận ra là đây là thuật toán random dựa vào thời gian nên search ra 1 tool giúp chúng ta quy đổi dễ dàng hơn :https://www.epochconverter.com/ 
 
 

## SOLUTION:
 
 Với thuật toán random như này thì mình không nghĩ ra được cách gì ngoài bruteforce :< 
 
 
![Test Image 4](https://github.com/AnhDungDoan/Cryptanalysis/blob/main/Code%20-%20Pseudo%20Random%20Number%20Generator/solution.png)
 




## FLAG : xXxootHiSiStH3K3yooxXx


#  23. RSA - Continued fractions
Chall : https://www.root-me.org/en/Challenges/Cryptanalysis/RSA-Continued-fractions

Author: Dt

Đề cho chúng ra giá trị hex của E và N 
## SOLUTION:
Chúng ta có thể tìm ra PrivateKey từ những giữ kiện trên :


```
#!/urs/bin/env python3.5
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from binascii import *
import base64
import binascii


E = "0xf70b3bd74801a25eccbde24e01b077677e298391d4197b099a6f961244f04314da7de144dd69a8aa84686bf4ddbd14a6344bbc315218dbbaf29490a44e42e5c4a2a4e76b8101a5ca82351c07b4cfd4e08038c8d5573a827b227bce515b70866724718ec2ac03359614cdf43dd88f1ac7ee453917975a13c019e620e531207692224009c75eaef11e130f8e54cce31e86c84e9366219ae5c250853be145ea87dcf37aa7ece0a994195885e31ebcd8fe742df1cd1370c95b6684ab6c37e84762193c27dd34c3cf3f5e69957b8338f9143a0052c9381d9e2ecb9ef504c954b453f57632705ed44b28a4b5cbe61368e485da6af2dfc901e45868cdd5006913f338a3"
N = "0x0207a7df9d173f5969ad16dc318496b36be39fe581207e6ea318d3bfbe22c8b485600ba9811a78decc6d5aab79a1c2c491eb6d4f39820657b6686391b85474172ae504f48f02f7ee3a2ab31fce1cf9c22f40e919965c7f67a8acbfa11ee4e7e2f3217bc9a054587500424d0806c0e759081651f6e406a9a642de6e8e131cb644a12e46573bd8246dc5e067d2a4f176fef6eec445bfa9db888a35257376e67109faabe39b0cf8afe2ca123da8314d09f2404922fc4116d682a4bdaeecb73f59c49db7fa12a7fc5c981454925c94e0b5472e02d924dad62c260066e07c7d3b1089d5475c2c066b7f94553c75e856e3a2a773c6c24d5ba64055eb8fea3e57b06b04a3"



e = int(E,16)
n = int(N,16)


print(e) #31186400897019474935110647285445503673131446580681275776311671951414114788622345838774311877965990786720764658784947421898983517760738477784602362371051561562206808351224503093181667456617648598165647915091757078611302190825934535904283579772712691438112230134828980258111970295516689690256373292215340475163958923723790536805165847711775268441953305309821252180479573636847217520184023025127620891001593596764466667387987683667801953315782130313468664428515728986226452261450588569245373362702725469848655817202090205940445626402571508469590603334162227644680600619967899413710405809040986903674088539812272861821091
print(n) 
#65600461780989803766848392425426887870434366488494962966900808777432584484088221195303017908185765416426865541330492621828385095208401835694398180740583580467731175837961973916562100612373134902716587868046427380223327738540114777241641014871790815133235867909646828092331690444703436170746272569822738659402858823786521460740789564170287308513292418939316054128834222945338106076073139265530198099998748944323883371406422653204889570690803132164330855565516333393423122237578933112127930186731899656475860444002021681839995303291028010312901432208049210885186720776201994911765956299022808044735625894648965241701539


//factordb
q = 240235037993086647490360091251920509660926008787784163933134217892938306866733942789677346753386227305733054945882967240289722901543973488715609201686292184661845932338700104193843036687863902362262743558762135191383008370605906319072352806840967443808455667223189470493469726348267326087313303773058894562037
p = 273067835270880086905225991495379768025497181071655465691068234751894433419924689398578343149876505032891110212422075482294849988417876098468455656340271714411918145829343178315564694346337087829483997746033122936265729805143582391157953230943745740375876718066059315171626227510845447370568918599985468283447


phi = (q-1)*(p-1)
d = inverse(e,phi)



k = RSA.construct((n,e,d,p,q))
print(k.exportKey())
```

## FLAG
"""-----BEGIN RSA PRIVATE KEY-----\nMIIEXgIBAAKCAQECB6ffnRc/WWmtFtwxhJaza+Of5YEgfm6jGNO/viLItIVgC6mB\nGnjezG1aq3mhwsSR621POYIGV7ZoY5G4VHQXKuUE9I8C9+46KrMfzhz5wi9A6RmW\nXH9nqKy/oR7k5+LzIXvJoFRYdQBCTQgGwOdZCBZR9uQGqaZC3m6OExy2RKEuRlc7\n2CRtxeBn0qTxdv727sRFv6nbiIo1JXN25nEJ+qvjmwz4r+LKEj2oMU0J8kBJIvxB\nFtaCpL2u7Lc/WcSdt/oSp/xcmBRUklyU4LVHLgLZJNrWLCYAZuB8fTsQidVHXCwG\na3+UVTx16FbjoqdzxsJNW6ZAVeuP6j5XsGsEowKCAQEA9ws710gBol7MveJOAbB3\nZ34pg5HUGXsJmm+WEkTwQxTafeFE3WmoqoRoa/TdvRSmNEu8MVIY27rylJCkTkLl\nxKKk52uBAaXKgjUcB7TP1OCAOMjVVzqCeyJ7zlFbcIZnJHGOwqwDNZYUzfQ92I8a\nx+5FOReXWhPAGeYg5TEgdpIiQAnHXq7xHhMPjlTM4x6GyE6TZiGa5cJQhTvhReqH\n3PN6p+zgqZQZWIXjHrzY/nQt8c0TcMlbZoSrbDfoR2IZPCfdNMPPP15plXuDOPkU\nOgBSyTgdni7LnvUEyVS0U/V2MnBe1EsopLXL5hNo5IXaavLfyQHkWGjN1QBpE/M4\nowJAZr7ln9D/ONqkfSGco4N7gQRoITmyrj9/XhF7MZQYzV6ZVN7TPUF8E5W7c2ha\nhxw128jwHLJZTwa+dlS76h86IwKBgQGE3IuaqynPUZNHJCbpIWPkEXBjdYOx6ixQ\nrgRROuQuZCgaUYONIAUaXb0aa9PiGQaCj3doytCyCjrx7Yrx/Wm3TlPI2U0AJ3Tv\nRjt4clWL+ntxMV0pvAJo9fYHAfR6wke8X8cTrTmfV51k3OpIXBZUQyd9oGJoicuE\nqwOIcKQaNwKBgQFWGyYVufNaqQjJfMW/Jx6IWUL87CjAcchmDsbzwKbscQ6Fogva\naJV2s0bJF9+HgvQ9fswYl6JzpsSbniX+9LXHLzFxNdyX9VSx0bIs8CayjiYJQANG\njS7MEnFeKtArzDcf0nZrOjxmfIaFZmmjDJz1ytEXTgyWgHDtvKufI2KC9QJAZr7l\nn9D/ONqkfSGco4N7gQRoITmyrj9/XhF7MZQYzV6ZVN7TPUF8E5W7c2hahxw128jw\nHLJZTwa+dlS76h86IwJAZr7ln9D/ONqkfSGco4N7gQRoITmyrj9/XhF7MZQYzV6Z\nVN7TPUF8E5W7c2hahxw128jwHLJZTwa+dlS76h86IwKBgH4kCjHhK3h5ZZKtvIQ4\nzQtypJkw+IlkzlDzO8+9X3mStmpHlDjSYmgrb4kvMAp3WqBNMZvtLqYQcydsEwoh\nmyU5l7eqWqEHsno2iCXu+vS9DwrxcpgwcXFroI4D7awt5lHKPniFNQKXmE3uVYGd\nLrNAfTJRPszGn8TE7wJV6dw7\n-----END RSA PRIVATE KEY-----"""


# 24. Challenge RSA - Multiple recipients
Chall : https://www.root-me.org/en/Challenges/Cryptanalysis/RSA-Multiple-recipients?action_solution=voir&debut_affiche_solutions=2#pagination_affiche_solutions

Author: Dt

Đề cho chúng ta 3 cipher cùng 3 publickey :<<<

## Solution
Đọc sơ qua thì chúng ta có thể nhận thấy rằng chúng ta sẽ có n1 n2 n3 và e1 e2 e3 từ 3 publickey cho trước , ta check thì thấy 3 e giống nhau = > Hastad Attack (https://github.com/ashutosh1206/Crypton/tree/master/RSA-encryption/Attack-Hastad-Broadcast) 

Thật là tuyệt vời nếu cứ theo Hastad Attack mà tấn công thì sẽ mất rất nhiều thời gian và chúng ta có tool để giải quyết việc đó RSHack (https://github.com/zweisamkeit/RSHack)


Sau khi ngồi viết đoạn source code thì và bỏ vào tool thì chúng ta có đáp án sau:

![Test Image ](https://github.com/AnhDungDoan/Cryptanalysis/blob/main/RSA%20-%20Multiple%20recipients/hastad-attack.png)

## FLag  NoSpamMoreRSA!


# 25. Challenge 7 Set 1 AES in ECB mode
Chall :https://cryptopals.com/sets/1/challenges/7

Author : Dt

Do ECB sử dụng lại encryptor/decryptor mà không có IV (hay IV toàn null bytes, nên chúng ta có thể khởi đầu trước):

## Solution

May thay AES được hỗ trợ trong thư viện Crypto.Cipher : 
```
import base64
from Crypto.Cipher import AES


with open('7.txt') as fh:
	c = base64.b64decode(fh.read())

key = b'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(c)
print(plaintext)
```

## Flag 

![Test Image ](https://github.com/AnhDungDoan/Cryptanalysis/blob/main/Challenge%207%20Set%201/Poem.png)


# 26. Challenge 33 Set 5 Implement Diffie-Hellman
Chall :https://cryptopals.com/sets/5/challenges/33

Author : Dt

Bài này đã được hướng dẫn rất cặn kẽ, chúng ta chỉ việc làm theo hướng dẫn : 
## Solution

```
import random

p = int("0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff",16)

g = 2

a = random.randint(0, p - 1)
A = pow(g, a, p)

b = random.randint(0, p - 1)
B = pow(g, b, p)

s = pow(B, a, p)
assert s == pow(A, b, p)

print(s)
```

## Flag 
2014647760836070607509901427608157854670150742266208004593761916757845509196706716253564871197512535881040617354657028128000953752110146644406771388436960666242577075655710457120201387327934424759385486397302847711596522156365638962486054195463490947892004087967874151003110801649722755319818794383184049700715341284771635132449413457156017002750306509055558060591806692197673330516297134549372050766962507285121854050933376585940239638822978985316428006866164322


# 27. Challenge 8 Set 1: Detect AES in ECB mode
Chall: https://cryptopals.com/sets/1/challenges/8

Author: thune

## STATEMENT
[In this file](https://github.com/AnhDungDoan/Cryptanalysis/blob/main/Detect%20AES%20in%20ECB%20mode/detect-aes-in-ecb-mode.txt) are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

## SOLUTION
Đầu tiên, muốn làm được bài này chúng ta cần đọc kỹ đề bài: Đề bài cho chúng ta "a bunch of hex-encoded ciphertexts" tức file này không phải là một chuỗi string dài mà là nhiều chuỗi string. Do vậy, "One of them has been encrypted with ECB" tức là một trong những chuỗi string, cụ thể là một trong các dòng trong file trên đó được encrypt bởi AES mode ECB.

Trong mode ECB, ciphertext được thành nhiều khối, cụ thể như trong đề là các khối 16 bytes, sau đó các khối sẽ cùng đồng thời được mã hóa với key. Vì vậy sẽ dẫn đến tình trạng các khối plaintext giống sẽ tạo ra ciphertext giống nhau. Vì vậy, chúng ta sẽ sử dụng đặc điểm này để phát hiện dòng nào được encrypt bởi ECB mode.

Viết một hàm để chia ciphertext thành các khối có kích thước 16 bytes, sau đó tính toán tổng lần lặp của các khối đó trong ciphertext. 
```
def count_repeat_block(ciphertext, line_number):
    block = []
    #Chia khối
    for i in range(0, len(ciphertext), 16):
        block.append(ciphertext[i:i+16])
    #Tính toán lặp
    #len(set(block)) là tập hợp các phần tử của block nhưng mỗi phần tử chỉ xuất hiện một lần
    count = len(block) - len(set(block))
    #Kết quả được lưu vào một bộ gồm ciphertext, số lần lặp các khối trong ciphertext đó và số thứ tự dòng của ciphertext
    results = {
    'ciphertext' : ciphertext,
    'count' : count,
    'line_number' : line_number
    }
    return results   
```
Tính toán tổng số lần lặp của các khối cho từng dòng trong file. Dòng nào có tổng lần lặp nhiều nhất, dòng đó có thể là ciphertext được encrypt bởi ECB mode.
```
for cipher in ciphertext:
    count_repeat.append(count_repeat_block(cipher, line_number))
    line_number += 1

#Phần tử có tổng số lần lặp của các khối lớn nhất có thể là ciphertext đã được encrypt với ECB mode     
max_count_repeat = sorted(count_repeat, key = lambda x:x['count'],reverse = True)[0]

```
[Vào đây](https://github.com/AnhDungDoan/Cryptanalysis/blob/main/Detect%20AES%20in%20ECB%20mode/detect-aes-in-ecb-mode.py) để xem source code bài này @@
## FLAG
> Ciphertext: b'\xd8\x80a\x97@\xa8\xa1\x9bx@\xa8\xa3\x1c\x81\n=\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xe2\xdd\x05/kd\x1d\xbf\x9d\x11\xb04\x85B\xbbW\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x94u\xc9\xdf\xdb\xc1\xd4e\x97\x94\x9d\x9c~\x82\xbfZ\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x97\xa9>\xab\x8dj\xec\xd5fH\x91Tx\x9ak\x03\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xd4\x03\x18\x0c\x98\xc8\xf6\xdb\x1f*?\x9c@@\xde\xb0\xabQ\xb2\x993\xf2\xc1#\xc5\x83\x86\xb0o\xba\x18j'
> 
> Number of repetitions 3
> 
> Line number 133

![Test Image ](https://github.com/AnhDungDoan/Cryptanalysis/blob/main/Detect%20AES%20in%20ECB%20mode/flag.PNG)

# 28. File - PKZIP
Chall: https://www.root-me.org/en/Challenges/Cryptanalysis/File-PKZIP

Author: gnudnaod

## SOLUTION
- Install `fcrackzip` : 'apt install fcrackzip'
- Use: 'fcrackzip -h' to show how to use:
```
USAGE: fcrackzip
          [-b|--brute-force]            use brute force algorithm
          [-D|--dictionary]             use a dictionary
          [-B|--benchmark]              execute a small benchmark
          [-c|--charset characterset]   use characters from charset
          [-h|--help]                   show this message
          [--version]                   show the version of this program
          [-V|--validate]               sanity-check the algorithm
          [-v|--verbose]                be more verbose
          [-p|--init-password string]   use string as initial password/file
          [-l|--length min-max]         check password with length min to max
          [-u|--use-unzip]              use unzip to weed out wrong passwords
          [-m|--method num]             use method number "num" (see below)
          [-2|--modulo r/m]             only calculcate 1/m of the password
          file...                    the zipfiles to crack

methods compiled in (* = default):

 0: cpmask
 1: zip1
*2: zip2, USE_MULT_TAB

```
- Then:
```
	root@DESKTOP-FT1E413:/mnt/d/NT219.L21/rootme/File - PKZIP# fcrackzip -b -c 1 -l 4-5 -u ch5.zip

	PASSWORD FOUND!!!!: pw == 14535
```

## FLAG
> 14535

# 29. Implement PKCS#7 padding
Chall: https://cryptopals.com/sets/2/challenges/9

Author: gnudnaod

## SOLUTION
 - Easy padding.
 ```
 def pkcs7(s: bytes, length: int) -> bytes:
    diff = length - len(s)
    return s + bytes([diff] * diff)


#print(pkcs7(b"YES", 16))
 if pkcs7(b"YELLOW SUBMARINE", 20) == b"YELLOW SUBMARINE\x04\x04\x04\x04":
     print("SUCCESS")
 ```
 
 ## FLAG
 > YELLOW SUBMARINE\x04\x04\x04\x04

# 30. Hash - Message Digest 5
Chall: https://www.root-me.org/fr/Challenges/Cryptanalyse/Hash-Message-Digest-5

Author: hoang

## SOLUTION
Hàm hash "7ecc19e1a0be36ba2c6f05d06b5d3058" có 32 kí tự nên đây là 1 loại mã MD5.
Dùng tool có sẵn trên mạng "https://md5decrypt.net/" để giải mã.

## FLAG
> weak

# 31. Hash - SHA-2
Chall: https://www.root-me.org/fr/Challenges/Cryptanalyse/Hash-SHA-2

Author: hoang

## SOLUTION
đoạn mã được cho: "96719db60d8e3f498c98d94155e1296aac105ck4923290c89eeeb3ba26d3eef92"
trong hệ thập lục phân, các kí tự dạng số là từ 0 -> 9, chữ là từ a -> f, mà ta
nhận thấy được trong đoạn mã được cho có 1 chữ k đặt sai nên ta phải xóa chữ k trong đoạn mã
Sau khi xóa thì ta bỏ đoạn code vào tool có sẵn :"http://online.crackmyhash.com/" và crack dưới dạng SHA256.

## FLAG
> 4dM1n

# 32. Challenge 10 Set 2 Implement CBC mode
Chall : https://cryptopals.com/sets/2/challenges/10

Author : Dt

Để yêu cầu chúng ta thực hiện chế độ CBC bằng tay bằng cách sử dụng hàm ECB bạn đã viết trước đó, làm cho nó mã hóa thay vì giải mã (xác minh điều này bằng cách giải mã bất kỳ thứ gì bạn mã hóa để kiểm tra) và sử dụng hàm XOR của bạn từ bài tập trước để kết hợp chúng.

# Solution
 Nhưng tại vì mình không làm liền mạch các chall nên mình sẽ tự viết lại 2 hàm trên và sử dụng thư viện hỗ trợ : from Crypto.Cipher import AES
 
 Đề có lưu ý iv = 0 nên mình sẽ tạo iv gồm 16 byte 0: 
 
 ```
 from Crypto.Cipher import AES
import base64


def xor(b1: bytes, b2: bytes):
    return bytes(x ^ y for x, y in zip(b1, b2))


def Decrypt(key: bytes, cipher: bytes, mode: str):
    cryptor = AES.new(key, AES.MODE_ECB)
    iv = b'\x00' * 16
    decrypted = b''
    for i in range(0, len(c), 16):
        decrypted += xor(cryptor.decrypt(cipher[i : i + 16]), iv)
        if mode == 'cbc':
            iv = c[i : i + 16]
    return decrypted

f = open("10.txt",'r')

c = f.read()
c = base64.b64decode(c)
#print(c)

print(Ddecrypt(b'YELLOW SUBMARINE', c, 'cbc'))
```

#Flag
```"I'm back and I'm ringin' the bell \nA rockin' on the mike while the fly girls yell \nIn ecstasy in the back of me \nWell that's my DJ Deshay cuttin' all them Z's \nHittin' hard and the girlies goin' crazy \nVanilla's on the mike, man I'm not lazy. \n\nI'm lettin' my drug kick in \nIt controls my mouth and I begin \nTo just let it flow, let my concepts go \nMy posse's to the side yellin', Go Vanilla Go! \n\nSmooth 'cause that's the way I will be \nAnd if you don't give a damn, then \nWhy you starin' at me \nSo get off 'cause I control the stage \nThere's no dissin' allowed \nI'm in my own phase \nThe girlies sa y they love me and that is ok \nAnd I can dance better than any kid n' play \n\nStage 2 -- Yea the one ya' wanna listen to \nIt's off my head so let the beat play through \nSo I can funk it up and make it sound good \n1-2-3 Yo -- Knock on some wood \nFor good luck, I like my rhymes atrocious \nSupercalafragilisticexpialidocious \nI'm an effect and that you can bet \nI can take a fly girl and make her wet. \n\nI'm like Samson -- Samson to Delilah \nThere's no denyin', You can try to hang \nBut you'll keep tryin' to get my style \nOver and over, practice makes perfect \nBut not if you're a loafer. \n\nYou'll get nowhere, no place, no time, no girls \nSoon -- Oh my God, homebody, you probably eat \nSpaghetti with a spoon! Come on and say it! \n\nVIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino \nIntoxicating so you stagger like a wino \nSo punks stop trying and girl stop cryin' \nVanilla Ice is sellin' and you people are buyin' \n'Cause why the freaks are jockin' like Crazy Glue \nMovin' and groovin' trying to sing along \nAll through the ghetto groovin' this here song \nNow you're amazed by the VIP posse. \n\nSteppin' so hard like a German Nazi \nStartled by the bases hittin' ground \nThere's no trippin' on mine, I'm just gettin' down \nSparkamatic, I'm hangin' tight like a fanatic \nYou trapped me once and I thought that \nYou might have it \nSo step down and lend me your ear \n'89 in my time! You, '90 is my year. \n\nYou're weakenin' fast, YO! and I can tell it \nYour body's gettin' hot, so, so I can smell it \nSo don't be mad and don't be sad \n'Cause the lyrics belong to ICE, You can call me Dad \nYou're pitchin' a fit, so step back and endure \nLet the witch doctor, Ice, do the dance to cure \nSo come up close and don't be square \nYou wanna battle me -- Anytime, anywhere \n\nYou thought that I was weak, Boy, you're dead wrong \nSo come on, everybody and sing this song \n\nSay -- Play that funky music Say, go white boy, go white boy go \nplay that funky music Go white boy, go white boy, go \nLay down and boogie and play that funky music till you die. \n\nPlay that funky music Come on, Come on, let me hear \nPlay that funky music white boy you say it, say it \nPlay that funky music A little louder now \nPlay that funky music, white boy Come on, Come on, Come on \nPlay that funky music \n\x04\x04\x04\x04"
```
Plaintext của bài đó là toàn bộ lyrics của bài "Play That Funky Music" của Vanilla Ice.

# 33. Challenge 41 Set 6 Implement unpadded message recovery oracle
Chall : https://cryptopals.com/sets/6/challenges/41 
Author : Dt

```
This turns out to be trivially breakable:

Capture the ciphertext C
Let N and E be the public modulus and exponent respectively
Let S be a random number > 1 mod N. Doesn't matter what.
Now:
C' = ((S**E mod N) C) mod N
Submit C', which appears totally different from C, to the server, recovering P', which appears totally different from P
Now:
          P'
    P = -----  mod N
          S
```
Đây là yêu cầu của đề bài yêu cầu chúng ta tận dụng lỗi sau ; 
#Solution
```
c2 = ((S**e mod n)*c) mod n = > c1 = S^e mod n 
c2 = (c1*c)mod n 

= > P = (c2*inverse(s,n))%n
```
Dựa vào lý thuyết đó ta có code : 
```
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
```

# Flag
2001 

# 34. Challenge 39 Set 5 Implement RSA 
Chall : https://cryptopals.com/sets/5/challenges/39

Author : Dt

Tóm tắt yêu cầu như sau : Chúng ta phải viết 2 hàm egcd() , inverse():

# Solution

```

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
```

# Flag
> 2001

# 35. Challenges 6 Set 1: Break repeating-key XOR
Chall: https://cryptopals.com/sets/1/challenges/6

Author: thune

## SOLUTION
Đề bài đã liệt kê và chỉ ra cho chúng ta các bước để phá mã XOR với key lặp lại.

Bước 1: Độ dài KEYSIZE sẽ từ 2-40

Bước 2: Viết 1 function để tính toán [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance#:~:text=In%20information%20theory%2C%20the%20Hamming,the%20corresponding%20symbols%20are%20different.) của 2 số dưới dạng dãy byte. Sau đó XOR 2 dãy byte lại và tính toán số lượng bit 1 xuất hiện trong kết quả (chính là số lượng bit khác nhau giữa 2 dãy byte)
```
def calculate_hamming_distance(input_bytes_1, input_bytes_2):
    hamming_distance = 0
    for b1, b2 in zip(input_bytes_1, input_bytes_2):
        difference = b1 ^ b2

        # Count the number of differences ('1's) and add to the hamming distance
        hamming_distance += sum([1 for bit in bin(difference) if bit == '1'])
    return hamming_distance
```
Bước 3: Đối với mỗi KEYSIZE, chia ciphertext dưới dạng  trong [ciphertext.txt](https://github.com/AnhDungDoan/Cryptanalysis/blob/main/Challenges%206%20Set%201%20Break%20repeating-key%20XOR/ciphertext.txt) thành các dãy byte có độ dài bằng KEYSIZE. Sau đó, với mỗi dãy byte, lấy 1 byte đầu của dãy và 1 byte thứ hai của dãy để tính Hamming distance giữa chúng. Sau đó, tính trung bình của tất cả các Hamming distance.
```
 average_distances = []

    for keysize in range(2,41):

        distances = []

        chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
        
        while True:
            try:
                chunk_1 = chunks[0]
                chunk_2 = chunks[1]
                distance = calculate_hamming_distance(chunk_1, chunk_2)

                distances.append(distance/keysize)

                del chunks[0]
                del chunks[1]

            except Exception as e:
                break
        result = {
            'key': keysize,
            'avg distance': sum(distances) / len(distances)
            }
        average_distances.append(result)
```
Bước 4: Giá trị KEYSIZE với Hamming distance trung bình nhỏ nhất có thể là KEY. Nên ta chọn KEYSIZE đó (vẫn chưa biết kí tự trong đó là gì) để tìm KEY.
```
possible_key_lengths = sorted(average_distances, key=lambda x: x['avg distance'])[0]
```
Bước 5,6,7,8: Theo như ví dụ mô phỏng sau với plaintetx = 'the cat in the het' and key = ICE
> the cat in the hat
>
> ICEICEICEICEICEICE

Do độ dài key nhỏ hơn độ dày plaintext nên key phải được lặp đi lặp lại cho bằng độ dài plaintext rồi mới XOR. Ta thấy rằng, đối với mỗi chữ I trong key sau khi XOR với ký tự plaintext tương ứng tạo ra ciphertext tương ứng. Và cũng biết rằng, do key được lặp lại nên có thể tạo ra ciphertext giống nhau với plaintext giống nhau. Do vậy, chúng ta chia ciphertext thành nhiều khối có kích thước KEYSIZE vừa tìm được, sau đó lại lấy tuần tự các bit thứ i (i<KEYSIZE) gộp thành một khối, mỗi khối tương ứng với một chữ cái (như trong ví dụ, nếu chia ciphertext thành các khối có 3 ký tự, rồi lấy ký tự thứ i của mỗi khối gộp lại, ta được các khối có plaintext khi XOR tương ứng với các ký tự I, C, E). Tuy nhiên, ta không biết được khối nào trong các khối đó là một ký tự thuộc KEY và ký tự đó là ký tự nào. Do đó, ta XOR mỗi khối với tất cả các ký tự trong bảng ASCII (bao gồm chữ cái, số và cả những ký tự khác). Về cơ bản, bước này giống khi XOR ngược lại ciphertext với KEY để tìm ra plaintext. Ứng với mỗi khối, ta tính toán số lượng chữ cái có trong kết quả vừa XOR. Chữ cái tương ứng  với kết quả có số lượng chữ cái cao nhất sẽ rất có khả năng là một ký tự trong KEY.
```
import base64


def get_english_score(input_bytes):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def single_char_xor(input_bytes, char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes


def bruteforce_single_char_xor(ciphertext):
    potential_messages = []
    for key_value in range(256):
        message = single_char_xor(ciphertext, key_value)
        score = get_english_score(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
            }
        potential_messages.append(data)
    return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]
```
Làm theo như yêu cầu đề bài, ta có được đoạn code [Break-repeating-key-XOR.py](https://github.com/AnhDungDoan/Cryptanalysis/blob/main/Challenges%206%20Set%201%20Break%20repeating-key%20XOR/Break-repeating-key-XOR.py)

# 36. AES - CBC - Bit-Flipping Attack
Chall: https://www.root-me.org/fr/Challenges/Cryptanalyse/AES-CBC-Bit-Flipping-Attack?action_solution=voir&debut_affiche_solutions=4#pagination_affiche_solutions

Author: hoang

## SOLUTION
Đầu vào của AES - CBC là plaintext 48 bytes chia ra làm 3 khối, mỗi khối 16 bytes vậy nên sau khi thử nhiều cách tạo tên khác nhau thì nhận thấy phải đặt username có độ dài 48 bytes
Username như sau: 01234567abcdefghABCDEFGH01234567abcdefghABCDEFGH
mail thì đặt sao cũng được: test
đoạn plaintext được tạo ra là:[id=546815648;name=01234567abcdefghABCDEFGH01234567abcdefghABCDEFGH;is_member=false;mail=test;pad=0000000000000] độ dài: 112 bytes

Nhận ra rằng để lấy được flag, ta cần là thành viên của nhóm hack này, tức là is_member = true.

Token: ''

Decode token về dưới dạng hex:

```
import base64

token = 'IRZjBh6GxjeYI7YZvxwfBD1RaarKZvDEFU00ebc/9ADuZIXv5vk6QMoHInn4AaaJKF+x5/ZxcEyznNQElMgsqAUTgXV3k7vVK1K5471br0p/zdOI9yxwDEjeGugWdZZfoBwjLjsrN3r3NT4UiR/DUA=='

t = base64.b64decode(token)

for i in t:
    print(hex(i), end = ' ')
tmp = bytearray(t)
```
Đầu tiên ta thử sửa 1 bit bất kì với câu lệnh: tmp[17] ^= 0x01
Sau khi sửa và gửi về server, ngay lập tức server phát hiện có kí tự lạ và tự động out khỏi chương trình

Sau nhiều lần thử, phát hiện ra ;is_member=true] là đoạn input ta cần truyền vào và thật trùng hợp ... nó có độ dài là 16 bytes.

ta sẽ tiến hành chèn 16 chữ a vào sau đó sửa thành ;is_member=true] vào 16 bytes cuối của đoạn plaintext.
```
import base64

token = 'IRZjBh6GxjeYI7YZvxwfBD1RaarKZvDEFU00ebc/9ADuZIXv5vk6QMoHInn4AaaJKF+x5/ZxcEyznNQElMgsqAUTgXV3k7vVK1K5471br0p/zdOI9yxwDEjeGugWdZZfoBwjLjsrN3r3NT4UiR/DUA=='

t = base64.b64decode(token)

for i in t:
  print(hex(i), end = ' ')
tmp = bytearray(t)


tmp += bytearray('a'.encode()*16)
expected = bytearray(';is_member=true]'.encode())
current = bytearray(b'+\x10\xb1\r\x8c\xd3\x99\x05\x0f\xfa\xed\x0e\xdc\x94\xc8\x1b')
print(len(current),len(expected))
for i in range(16):
  tmp[96+i] ^= (expected[i]^current[i])

print('\n',base64.b64encode(tmp))
```

## FLAG
> Gr3@t_CBC_Tr1ck_15n't_1t?

# 37. ECB cut-and-paste

Chall: https://cryptopals.com/sets/2/challenges/13

## SOLUTION
Đây là một bài về mã hóa AES_ECB, nên đầu tiên ta cần hàm tạo khóa và hàm pad cho plaintext
```
def create_value(length:int = 16) -> bytes:
  return bytes([random.randint(0, 255) for _ in range(length)])

def pkcs7_pad(s: bytes, block_length: int) -> bytes:
    num_to_pad = block_length - (len(s) % block_length)
    return s + bytes([num_to_pad]) * num_to_pad
```
Tiếp theo, ta bắt đầu triển khai hàm biến cookie string thành dictionary và 1 hàm dịch ngược lại. Với hàm dịch thuận thì ta lấy các chữ cái ra từ chuỗi mà đề cho trước và loại bỏ các kí tự nằm ở bên ngoài format của đề (ví dụ như khoảng trắng ở đầu và ở cuối chuỗi), hàm dịch ngược thì ghép kí tự '&' và '=' lại vào trong chuỗi theo format ban đầu bằng cách dùng join().
```
def cookie_to_dict(s: str) -> dict:
    return dict(map(lambda x: x.split('='), s.strip('&').split('&')))

assert cookie_to_dict('foo=bar&baz=qux&zap=zazzle') == {'foo': 'bar','baz': 'qux','zap': 'zazzle'}

def dict_to_cookie(d: dict) -> str:
    # assume all k-v are strings
    return '&'.join(map('='.join, d.items()))

assert dict_to_cookie({'foo': 'bar','baz': 'qux','zap': 'zazzle',}) == 'foo=bar&baz=qux&zap=zazzle'
```
Và như thường lệ, muốn mã hóa thì phải có hàm mã hóa, cụ thể là AES_ECB.
```
key = create_value()

def AES_ECB(byte_string: bytes, key: bytes, encrypt: bool = False) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    if encrypt:
        return cipher.encrypt(byte_string)
    else:
        return cipher.decrypt(byte_string)
```
Tiếp theo là 2 hàm mã hóa và giải mã profile của user, vì role=admin và role=user nó kh có cùng length nên ta phải thêm pad cho nó mới làm được
```
def encrypt_profile(email: str) -> bytes:
    s = profile_for(email).encode()
    s = pkcs7_pad(s, len(s) + 16 - (len(s) % 16))
    return AES_ECB(s, key, encrypt = True)

def decrypt_profile(s: bytes) -> dict:
    return cookie_to_dict(pkcs7_unpad(AES_ECB(s, key, encrypt = False)).decode())
```
Cuối cùng, ta tạo 1 format email chiếm đủ 1 block là có thể lấy được cipher rồi. Ở đây em chọn là 'A' * 10 + 'admin' + '\x0b' * 11. Sau đó sẽ tạo ra được khối 32 bytes là: 
email=AAAAAAAAAA
admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b
Xong rồi thì ta lấy khối block thứ 2 là được 
```
poison = encrypt_profile('A' * 10 + 'admin' + '\x0b' * 11)
user = encrypt_profile('bad@email.com')
crafted = user[:-16] + poison[16:32]
print(decrypt_profile(crafted))
```

# FLAG
>{'email': 'aaa@email.com', 'uid': '10', 'role': 'admin'}


# 38. CBC Bitflipping Attack

Chall: https://cryptopals.com/sets/2/challenges/16

Author: hoang

## SOLUTION
Các thư viện được sử dụng: Crypto.Cipher, Random, Commonprefix.

Đầu tiên, cần tạo key, IV, hàm XOR và Pad để phục vụ cho việc mã hóa
```
block_size = 16
def create_key(length:int = 16) -> bytes:
  return bytes([random.randint(0, 255) for _ in range(length)])


def pkcs7_pad(s: bytes, block_length: int) -> bytes:
    num_to_pad = block_length - (len(s) % block_length)
    return s + bytes([num_to_pad]) * num_to_pad


IV = create_key(block_size)
key = create_key(block_size)


def xor(buffer1: bytes, buffer2: bytes) -> bytes:
   return bytes([(b1 ^ b2) for b1, b2 in zip(buffer1, buffer2)])
```
Tiếp theo là build hàm CBC mà em đã làm trước khi em làm lại Set 2 Challenge 10
```
def AES_ECB(byte_string: bytes, key: bytes, encrypt: bool = False) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    if encrypt:
        return cipher.encrypt(byte_string)
    else:
        return cipher.decrypt(byte_string)


## CBC Mode
def AES_CBC(byte_string: bytes, key: bytes, IV: bytes, encrypt: bool = True) -> bytes:
    if encrypt: 
        previous_block = IV
        cipher_text = b''
        for i in range(0, len(byte_string), len(key)):
            plain_text = xor(pkcs7_pad(byte_string[i: i + len(key)], len(key)),
                                   previous_block)
            previous_block = AES_ECB(plain_text, key, encrypt=True)
            cipher_text += previous_block
        return cipher_text
    else:
        previous_block = IV
        plain_text = b''
        for i in range(0, len(byte_string), len(key)):
            cipher_text = byte_string[i: i + len(key)]
            plain_text += xor(AES_ECB(cipher_text, key, encrypt=False), previous_block)
            previous_block = cipher_text
        return plain_text
```
Đề bài yêu cầu ta trích dẫn dấu ";" và "=" nên ta sẽ dùng replace(), sau đó ghép 2 đoạn plaintext đề cho vào cùng 1 chuỗi và 1 biến bool encrypt để kiểm tra trước khi mã hóa để kiểm tra có cần padding hay không và admin đã = true hay chưa, khi truyền vào hàm check.
```
def CBC_Flip_Bit(byte_string: bytes, encrypt = True)->bytes:
  if encrypt:
    b1 = b'comment1=cooking%20MCs;userdata='
    b2 = b';comment2=%20like%20a%20pound%20of%20bacon'
    s = (b1 + byte_string + b2).replace(b';',b'";"').replace(b'=',b'"="')
    return AES_CBC(pkcs7_pad(s, block_size), key, IV, encrypt = True)
  else: 
    return AES_CBC(byte_string, key, IV, encrypt = False)

def CBC_Flip_Bit_Check(byte_string: bytes) -> bool:
  decrypted = CBC_Flip_Bit(byte_string, encrypt = False)
  if b';admin=true;' in decrypted:
    return True
  else:
    return False
```
Khi thay đổi một giá trị ở 1 ô trong 1 khối thì các khối tiếp theo cũng sẽ bị ảnh hưởng ở cùng 1 ô. Quay lại câu hỏi,ta thêm 1 dãy các chữ "A" (gọi là tiền tố) vào chuỗi để đảm bảo rằng kích thước khối là bội số của 16 (kích thước mặc dịnh của AES_CBC),sau đó, ta nhập 1 đoạn string là xadminxtruex và biến các giá trị "x" thành ";" và "=". có thể thấy , những ô ta cần thay đổi trong chuỗi nằm ở vị trí {0, 6, 11}.
```
def CBC_Flip_Bit_Attack(encrypt, check):
  num_prefix_blocks = len(commonprefix([encrypt(b''), encrypt(b'A')])) // block_size + 1 
  encrypt_string = [encrypt(b'A'*0)]
  min_add = None
  for i in range(1, block_size):
    encrypt_string.append(encrypt(b'A'*i))
    length_prefix = len(commonprefix(encrypt_string))
    if length_prefix == num_prefix_blocks*block_size:
      min_add = i - 1
      break
    encrypt_string = [encrypt_string[-1]]
  assert min_add is not None

  encrypted = encrypt(b'A'*min_add + b'xadminxtruex')
  previous_block = [p for p in encrypted[(num_prefix_blocks - 1)*block_size: num_prefix_blocks*block_size]]
  previous_block[0] ^= ord(b'x') ^ ord(b';')
  previous_block[6] ^= ord(b'x') ^ ord(b'=')
  previous_block[11] ^= ord(b'x') ^ ord(b';')
  previous_block = bytes(previous_block)
  admin_string = encrypted[:(num_prefix_blocks - 1)*block_size] +previous_block + encrypted[num_prefix_blocks * block_size:]
  return check(admin_string)

CBC_Flip_Bit_Attack(CBC_Flip_Bit, CBC_Flip_Bit_Check)
```
Kết quả: True

## FLAG
> True

# 39. An ECB/CBC detection oracle

Chall: https://cryptopals.com/sets/2/challenges/11

Author: hoang

## SOLUTION

Thư viện sử dụng: Crypto.Cipher, random

Đầu tiên, để phục vụ cho việc mã hóa AES, ta cần có hàm tạo giá trị ngẫu nhiên (16 bytes) cho key và vector khởi tạo (IV), hàm tạo pad cho plaintext và hàm XOR, cùng với đó là 2 hàm AES_ECB và AES_CBC mà em đã làm ở các challenge trước. Đánh số MODE_ECB là 0 và CBC là 1.
```
block_size = 16
MODE_ECB = 0
MODE_CBC = 1

## Tạo Key
def create_value(length:int = 16) -> bytes:
  return bytes([random.randint(0, 255) for _ in range(length)])

##Tạo Pad
def pkcs7_pad(s: bytes, block_length: int) -> bytes:
    num_to_pad = block_length - (len(s) % block_length)
    return s + bytes([num_to_pad]) * num_to_pad

##XOR
def xor(buffer1: bytes, buffer2: bytes) -> bytes:
   return bytes([(b1 ^ b2) for b1, b2 in zip(buffer1, buffer2)])

IV = create_value(block_size)
key = create_value(block_size)

## Mode ECB
def AES_ECB(byte_string: bytes, key: bytes, encrypt: bool = False) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    if encrypt:
        return cipher.encrypt(byte_string)
    else:
        return cipher.decrypt(byte_string)

##Mode CBC
def AES_CBC(byte_string: bytes, key: bytes, IV: bytes, encrypt: bool = True) -> bytes:
    if encrypt: 
        previous_block = IV
        cipher_text = b''
        for i in range(0, len(byte_string), len(key)):
            plain_text = xor(pkcs7_pad(byte_string[i: i + len(key)], len(key)),
                                   previous_block)
            previous_block = AES_ECB(plain_text, key, encrypt=True)
            cipher_text += previous_block
        return cipher_text
    else:
        previous_block = IV
        plain_text = b''
        for i in range(0, len(byte_string), len(key)):
            cipher_text = byte_string[i: i + len(key)]
            plain_text += xor(AES_ECB(cipher_text, key, encrypt=False), previous_block)
            previous_block = cipher_text
        return plain_text
```
Quan sát đề bài, họ bảo ta chọn ngẫu nhiên các mode, tương đương với việc random giữa 0 và 1 tương ứng với MODE_ECB và MODE_CBC và trước khi mã hóa thì đầu plaintext và cuối plaintext phải được cộng thêm từ 5 -> 10 bytes ngẫu nhiên (random). Qua đó ta có code:
```
def enc_oracle(byte_string: bytes) -> tuple:
    append_before = create_value(random.randint(5,10))
    append_after = create_value(random.randint(5,10))
    plaintext = pkcs7_pad(append_before + byte_string + append_after, block_size)
    choice = random.randint(0,1)
    if choice == MODE_ECB:
        return AES_ECB(plaintext, key, encrypt = True), MODE_ECB
    else:
        return AES_CBC(plaintext, key, IV, encrypt = True), MODE_CBC
```
Sau đó. họ yêu cầu làm 1 hàm xác định (Detect) số lần xuất hiện của các mode, ở đây ta chỉ cần làm 1 hàm xác định MODE_ECB và MODE_CBC là các trường hợp còn lại. Vì với MODE_ECB, các khối plaintext giống nhau sẽ cho ra các ciphertext khác nhau, nên ta chỉ cần tạo plaintext sao cho plaintext giữa các khối giống nhau là được, ở đây em dùng 3 khối plaintext chữ b (tức là 48 bytes) và xét trong khoảng 16 bytes giữa các block plaintext. Sau khi xác định xong thì e sẽ dùng 1 hàm count và 1 vòng lặp từ i đến 10 và lần lượt random số lần xuất hiện của 2 mode.
```
def Detect_ECB(byte_string: bytes, block_length: int) -> bool:
    byte_blocks = [byte_string[i*block_length: (i+1)*block_length]
                   for i in range(int(len(byte_string) / block_length))]
    unique_blocks = set(byte_blocks)
    return len(unique_blocks)/len(byte_blocks) < 1

def dec_oracle(encryptor)-> bool:
    plaintext = b'b'*(block_size*3)
    enc_string, mode = encryptor(plaintext)
    if (Detect_ECB(enc_string, block_size)):
        predict_mode = MODE_ECB
        print('Using ECB')
    else:def create_value(length:int = 16) -> bytes:
  return bytes([random.randint(0, 255) for _ in range(length)])

def pkcs7_pad(s: bytes, block_length: int) -> bytes:
    num_to_pad = block_length - (len(s) % block_length)
    return s + bytes([num_to_pad]) * num_to_pad
`

        predict_mode = MODE_CBC
        print('Using CBC')
    return predict_mode == mode

count = 0
for i in range(10):
    if dec_oracle(enc_oracle):
        count += 1

print('Total enc time:', count)
```

## FLAG
> 10


# 40. PKCS#7 padding validation

Chall: https://cryptopals.com/sets/2/challenges/15

Author: hoang

## SOLUTION

Kiểm tra tuần tự từ cuối chuỗi đến hết giá trị padding, sai thì xuất ra "Bad Padding"
```
def pkcs7_unpad(msg:str):
    padding = int(msg[-1])
    tmp = len(msg) - 1
    p = len(msg) - padding
    for c in range(p, tmp):
        if msg[c] != padding:
            raise ValueError(f"Bad Padding")
    return msg[:-padding]

pkcs7_unpad(b"ICE ICE BABY\x04\x04\x04\x04")
```

## FLAG
> ICE ICE BABY
