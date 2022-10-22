# Problem 046
Write a program which encrypts and decrypts a text using a password. 

Encryption algorithm is up to your choice as long as you can recover 
and decrypt the encrypted input using the same password (Symmetric Encryption).

The input format is as follows:
P:Password:Plain Text
E:Password:Encrypted Text

The input starting with `P:` means the plain text to be encrypted.
The input starting with `E:` means the encrypted text to be decrypted.

Note that password may not contain `:` character but input text may contain `:` character.

# Persian Description
برنامه ای بنویسید که یک متن دریافت کرده، سپس با استفاده از یک رمز عبور که از ورودی میگیرد، متن را با یک روش ابداعی (منحصر به برنامه شما) رمزنگاری کرده و در خروجی چاپ کند.
همچنین در حالت معکوس، اگر متن رمزنگاری شده به همراه رمز عبور به برنامه ارسال شود، متن اولیه در خروجی چاپ شود. 

متن اولیه را با حرف P به معنای Plain Text و متن رمزنگاری شده را با حرف E به معنای Encrypted Text شناسایی کنید. فرمت ورودی به صورت زیر است
P:Password:Plain Text
E:Password:Encrypted Text

رمز عبور شامل کاراکتر : نیست ولی ورودی میتواند شامل : باشد

# Sample Input/Output

## Input:
```
P:UnfoldTheUniverse340:James Webb will change our understanding of universe
E:UnfoldTheUniverse340:xghuudsrnSakigbnmhfxd346Saqjibcdsby32vgz6iommkud
```

## Output: 
```
Encrypted Text is "xghuudsrnSakigbnmhfxd346Saqjibcdsby32vgz6iommkud"

Plain text is "James Webb will change our understanding of universe"
```