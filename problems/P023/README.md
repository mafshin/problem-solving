# Problem 023
Write a program which calculates the product of two matrixes
and prints the result.

First line of input contains 3 numbers N , M and P.
Then N lines of input with M numbers and
then M lines of input with P numbers are entered.

First matrix is N x M and second matrix is M x P.

Your solution should contain a function named `matrix_product`
which accepts two matrixes (list of lists) and returns a result matrix.


# Persian Description
برنامه ای بنویسید که دو ماتریس را از ورودی دریافت کرده و آن ها را در هم ضرب کرده و جواب را چاپ کند
ابتدا سه عدد n و m و p به عنوان ردیف و ستون ماتریس اول و تعداد ستون ماتریس دوم دریافت می شود
سپس n خط ورودی که هر خط شامل m عدد است وارد می شود. (ماتریس اول)
در ادامه m خط ورودی که هر خط شامل p عدد است وارد می شود. (ماتریس دوم)

این دو ماتریس سپس به صورت دو پارامتر از نوع آرایه دو بعدی به یک تابع ارسال می شوند. عملیات ضرب انجام می شود و خروجی که یک ماتریس n ردیف و p ستونی است برگردانده می شود.

نهایتا یک تابع هم یک آرگومان آرایه دو بعدی دریافت و آن را چاپ می کند.

در ضرب ماتریس ها، باید تعداد ستون ماتریس اول با تعداد ردیف ماتریس دوم برابر باشند (متغیر m در اینجا)

[n x m] X [m x p] = [n x p]

# Sample Input/Output

## Input:
```
3 4 2
1 24 3 4
5 61 7 8
19 10 11 12
8 20
1 3
4 65
90 32
```

## Output: 
```

```
