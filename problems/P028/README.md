# Problem 028
Write a program which calculates the required fuel for traveling
the specified routes between cities. The routes are only on the
lines of x and y in the coordinates system.

First line of input, N, is the number of cities. 
Then N lines follows with each line in the format of CITY X Y.

Then multiples routes are provided, one per each line. 
Each route contains the names of the cities in the route.

For each route calculate the total fuel required for traveling.

The required fuel for traveling between two cities is equal to their distance.

# Persian Description
برنامه ای بنویسید که اطلاعات مکانی تعدادی شهر را دریافت کرده سپس سوخت مصرفی برای مسیرهای تعیین شده را محاسبه و چاپ کند. مسافر همواره از کوتاهترین مسیر بین دو شهر عبور خواهد کرد. جاده فقط روی خطوط x و y قابل استفاده است.

سطر اول ورودی یک عدد n معادل تعداد شهرها، سپس n سطر شامل سه بخش، بخش اول نام شهر، بخش دوم مقدار X و بخش سوم مقدار Y در دستگاه مختصات
سپس نامحدود ورودی دریافت می شود شامل نام شهرهایی که در هر مسیر هستمد و خاتمه ورودی END است

خروجی شامل مجموع سوخت مصرفی برای هر مسیر باشد

X, Y >= 0, integer


# Sample Input/Output

## Input:
```
5
A 2 0
B 2 4
C 5 2
D 7 0
E 0 7

ACE
DBA
ABE
AC
```

## Output: 
```
ACE: 15
DBA: 13
ABE: 9
AC: 5
```
