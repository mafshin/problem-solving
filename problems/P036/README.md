# Problem 036
Write a compiler (interpreter) which gets some commands from input
and evaluates them the same way the language compiler (interprter) does.
Do not use `eval` for parsing the input.
The end of input is marked with `END`

# Persian Description
یک کامپایلر (مفسر) بنویسید که دستورات زیر را از ورودی دریافت کند و خروجی مشابه آنچه کامپایلر زبانی که در آن کد نوشته اید، تولید می کند، داشته باشد. 
ورودی در چندین خط وارد می شود و با END خاتمه می یابد. از امکانات موجود در زبان مثل eval برای parse کردن ورودی استفاده نکنید.

Python valid keywords:
```
print
str
+ - * / ( ) = , '
a b c d e
1234567890
```

C# valid keywords:
```
Console.WriteLine
+ - * / ( )  = ; , "
var a b c d e
1234567890
```


# Sample Input/Output

## Input (Python):
```
a = 20
ab2 = a + 5
ac3 = a - (ab2 *  6)
print('ac3 is ' + str(ac3) + ' and ab2 is ' + str(ab2))
print('Congrats')
END
```

## Input (C#):
```
var a = 20;
var ab2 = a + 5;
var ac3 = a - (ab2 *  6);
Console.WriteLine("ac3 is " + ac3 + " and ab2 is " + ab2);
Console.WriteLine('Congrats');
END
```

## Output: 
```
ac3 is -130 and ab2 is 25
Congrats
```