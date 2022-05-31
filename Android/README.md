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

Thay đổi giá trị của k thành hằng số, nghĩa là trong tệp smali được đề cập ở trên
iget v3, v3 .... (bỏ qua);->k:I
Thêm sau
const v3, 1616384

![image](https://user-images.githubusercontent.com/77602549/171141365-6de617e1-56e1-426d-b88f-886d66f6da32.png)


Đảo ngược điều kiện của cờ đầu ra, nghĩa là, trong MainActivity $1.smali
if-gtz v0, :cond_0
Câu này (tiếp theo là bước nhảy để xuất ra The Flag Is) được thay đổi thành
if-ltz v0, :cond_0


![image](https://user-images.githubusercontent.com/77602549/171141540-67c4e2e8-29aa-4ae1-9030-66ab40f99aab.png)



![image](https://user-images.githubusercontent.com/77602549/171141687-13db268d-d15f-44e2-9c80-74391c8d79e1.png)


![image](https://user-images.githubusercontent.com/77602549/171142215-da2ff46b-d6bf-4eec-aa4a-630c001d020e.png)

![image](https://user-images.githubusercontent.com/77602549/171143258-a8bf817c-cfbb-4fd6-9374-ed12d3b0882d.png)
![image](https://user-images.githubusercontent.com/77602549/171143299-b2dc41f8-ffaa-4f1a-aa39-bfc4961183b0.png)



![image](https://user-images.githubusercontent.com/77602549/171144196-3faddb32-352b-422c-b4cf-a221b8321a9b.png)

## WantAShell

![image](https://user-images.githubusercontent.com/77602549/171144441-7563d46a-5f6b-43ed-a07d-30c987880fe7.png)


![image](https://user-images.githubusercontent.com/77602549/171144805-4b302b9e-f89a-40bf-89bd-60c7be9e8d17.png)


![image](https://user-images.githubusercontent.com/77602549/171217668-a07a718e-cdf0-4df5-932c-139b40c53ff1.png)


![image](https://user-images.githubusercontent.com/77602549/171217690-69fe2d6e-adfc-4a87-9b24-831e564d147f.png)


![image](https://user-images.githubusercontent.com/77602549/171217874-0bf69db2-ede2-4e4a-9407-f68f96906ac1.png)



## 

![image](https://user-images.githubusercontent.com/77602549/171229805-2ff6e6eb-e6bf-407d-8cc3-ae52115192b3.png)


![image](https://user-images.githubusercontent.com/77602549/171229901-7327a0e0-2e4f-4195-9fad-ba4ce8c11522.png)


![image](https://user-images.githubusercontent.com/77602549/171229946-94d2b443-c28d-4983-8439-7191dcdcba2e.png)

![image](https://user-images.githubusercontent.com/77602549/171230008-0c004f03-22ac-47aa-9486-98954be910ec.png)

![image](https://user-images.githubusercontent.com/77602549/171230304-8b073693-0cc4-4415-a66e-f7e670b3255b.png)


key là QflMn`fH,ZHVW^7c 



