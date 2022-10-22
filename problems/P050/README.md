# Problem 050
Write a program to finds a combination of subset of a list which equals to a specific number.

First line of input is T, the number of cases.
For each case two lines are provided, first a list of numbers and then a number n.

Output contains an expression of a subset of list numbers with some operators which equals to n.

In case of multiple answers, the one with minimum number of elements (numbers) must be selected. If there are multiple answers with same number of numbers, then any of them is valid. 
Consider that you can use each number only once in the expression.

# Persian Description
 عدد دیگری (n) را از ورودی بگیرد. به ازای هر مورد، یک ترکیب از بخشی از اعضای لیست تشکیل دهد که معادل n شود. 
اولین ورودی یک عدد T هست و سپس 2T خط وارد می شود. اولین خط هر کیس، شامل مجموعه اعداد و دومین خط شامل عدد n می باشد. در صورت وجود جواب های متعدد، جوابی که کمترین تعداد اعداد را دارد را انتخاب کنید. در صورتی که چندین جواب با تعداد اعداد یکسان وجود داشت، هر کدام از جواب ها معتبر هستند.
همچنین هر عدد را فقط یکبار میتوانید در عبارت استفاده کنید.

# Sample Input/Output

## Input:
```
3
10 2 66 7 9 4 6
50
1 22 5 12
121
2 67 3 4
140
```

## Output: 
```
50 = (66 / 2) + 7 + 10
121 = 12 + (22 * 5) - 1
140 = ((67 + 3) / 2) * 4
```