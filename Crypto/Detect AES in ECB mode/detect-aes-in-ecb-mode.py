#Hàm cout_repeat_block dùng chia ciphertext thành các khối có kích thước 16 bytes, sau đó tính tổng số các chuỗi lặp trong ciphertext
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

#Chuyển các dòng trong file detect-aes-in-ecb-mode.txt thành định dạng byte, sau đó lưu các dòng vào mảng ciphertext     
ciphertext = [bytes.fromhex(line.strip()) for line in open("detect-aes-in-ecb-mode.txt")]

count_repeat = []
line_number = 1

#Tính count_repeat_block của các phần tử trong ciphertext, cụ thể là các dòng trong file detect-aes-in-ecb-mode.txt 
for cipher in ciphertext:
    count_repeat.append(count_repeat_block(cipher, line_number))
    line_number += 1

#Phần tử có tổng số lần lặp của các khối lớn nhất có thể là ciphertext đã được encrypt với ECB mode     
max_count_repeat = sorted(count_repeat, key = lambda x:x['count'],reverse = True)[0]

#In kết quả 
print("Ciphertext {}".format(max_count_repeat['ciphertext']))
print("Number of repetitions {}".format(max_count_repeat['count']))
print("Line number {}".format(max_count_repeat['line_number']))

        
