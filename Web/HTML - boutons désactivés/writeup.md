## HTML - boutons désactivés

![img](https://github.com/datnlq/R0OtM3/blob/main/Web/HTML%20-%20boutons%20d%C3%A9sactiv%C3%A9s/HTML-disabledbuttons.png?raw=true)

Truy cập vào challenge thì ta sẽ thấy được 1 trang web như sau: 

![img](https://github.com/datnlq/R0OtM3/blob/main/Web/HTML%20-%20boutons%20d%C3%A9sactiv%C3%A9s/HTML-disabledbuttons_chall.png?raw=true)

Chúng ta nhận ra rằng nút đã bị disabled nên chúng ta có thể dựa vào script sau để enabled lại tất cả các button của các form.
```
 let formElements = document.getElementsByName("authform")[0].elements
 
for (let i = 0; i < formElements.length; i++)
    formElements[i].disabled = false;
```
Ta áp dụng script này chạy trên console của trang web:

![img](https://github.com/datnlq/R0OtM3/blob/main/Web/HTML%20-%20boutons%20d%C3%A9sactiv%C3%A9s/HTML-disabledbuttons_chall2.png?raw=true)


Sau khi chạy được đoạn script thì chúng ta đã có thể thấy được mật khẩu.

![img](https://github.com/datnlq/R0OtM3/blob/main/Web/HTML%20-%20boutons%20d%C3%A9sactiv%C3%A9s/HTML-disabledbuttons_solve.png?raw=true)


Pass: HTMLCanStopYou
