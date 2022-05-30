## Easy RE



![image](https://user-images.githubusercontent.com/77602549/171031052-21c497ea-5213-4bb2-a756-689558d0b3cb.png)


![image](https://user-images.githubusercontent.com/77602549/171032491-ce483dd4-2c5a-480a-a0b1-524ddc75a208.png)


![image](https://user-images.githubusercontent.com/77602549/171032931-a4ca839b-46e5-4e0d-b807-e02f3b558a50.png)


![image](https://user-images.githubusercontent.com/77602549/171034525-228935b8-c0f0-4f3d-b1c6-669f176020d8.png)

## LoopAndLoop

![image](https://user-images.githubusercontent.com/77602549/171035225-5454473c-8897-4a02-8a01-26f16f7302de.png)

![image](https://user-images.githubusercontent.com/77602549/171035292-60524fd0-6993-4013-a326-3ffa35f1c1dc.png)

![image](https://user-images.githubusercontent.com/77602549/171035356-1c8aae8e-3eb7-4b34-93d6-0136158565e0.png)
Vì hàm check là native method, nên các hàm check1, check2, check 3 sẽ là các điều kiện, 1 phần trong quá trình lấy flag, ta thấy còn load thư viện lhm, ta đưa vào IDA xem thử:
![image](https://user-images.githubusercontent.com/77602549/171035671-ad10a86f-7785-43ab-ad16-3fb7722f9e23.png)

Ta đã có đủ điều kiện để rev thành 1 file  code solve.py như sau:

![image](https://user-images.githubusercontent.com/77602549/171037207-54c6f063-dca9-4cab-973c-d49b429178f7.png)


![image](https://user-images.githubusercontent.com/77602549/171037174-69698851-b324-4ef0-adbd-50fc04e844ae.png)

![image](https://user-images.githubusercontent.com/77602549/171037153-3ffa3f20-9c72-4f12-9de3-71d42b7caeae.png)


## Timer

![image](https://user-images.githubusercontent.com/77602549/171037459-45274a24-f2f0-4549-9a98-4873814f9928.png)

![image](https://user-images.githubusercontent.com/77602549/171038497-9018b367-e5d2-47e1-a7fa-5876d0b90d73.png)

![image](https://user-images.githubusercontent.com/77602549/171040548-874a86ed-c5c4-4c61-b4f2-a734f835eb5b.png)

Ta có thể thấy rằng flag được xác định bởi giá trị của k. Có một câu nếu có điều kiện dưới đây. Hàm IS2
được gọi là Hàm này được sử dụng để tính giá trị chính xác của k. Ta có thể viết 1 đoạn code mô phỏng lại để tìm ra k như sau:

![image](https://user-images.githubusercontent.com/77602549/171043548-fde4befe-6378-43b1-8e4d-3eac16086e85.png)


![image](https://user-images.githubusercontent.com/77602549/171043510-6dbaedfe-a466-4c5b-b115-34c91e3bfc52.png)

Giá trị của k là 1616384. Tuy nhiên ta cần biết biến k nằm ở đâu trong lúc complie và run apk để thay đổi nó. 



Đảo ngược điều kiện của cờ đầu ra, nghĩa là, trong MainActivity $1.smali
if-gtz v0, :cond_0
Câu này (tiếp theo là bước nhảy để xuất ra The Flag Is) được thay đổi thành
if-ltz v0, :cond_0
Thay đổi giá trị của k thành hằng số, nghĩa là trong tệp smali được đề cập ở trên
iget v3, v3 .... (bỏ qua);->k:I
Thêm sau
const v3, 1616384





