# Problem 039
Write a program which finds the common members among multiple list of members.

First line of input is a number N followed by N lines, one line per list.

Maximum number of members in each list: 1,000,000 members

# Persian Description
برنامه ای بنویسید که یک عدد N دریافت کرده سپس N لیست از ورودی دریافت کند و اعضای مشترک بین آنها را استخراج کند.

ماکزیمم تعداد اعضای هر لیست: ۱ میلیون عضو

# Sample Input/Output

## Input:
```
5
3 90 4 1 67 59 2
4 67 32 2 90 4
4 90 3 1 56 387 34 2
2 67 532 876 90
4 29 61 39 2 90
```

## Output: 
```
2 90
```

To generate random input in Python you can use the following code:
```
import random 
b = list(map(lambda x: random.randint(1, 1000),list(range(1, 1000))))
```