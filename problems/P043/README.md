# Problem 043
Write a program which receives a Sparce matrix and compress that in a way when the compressed matrix is provided as input, the original Sparce matrix is generated.

First line of input is `n` and `m` for rows and columns of the matrix. 
Then `n` rows containing `m` numbers are provided.

First output of the program must be the compressed form of matrix, such that when the compressed output is provided as next input, original matrix should be re-generated and printed.
Finally the compression ratio must be calculated and printed:
Compression ratio = output size / input size

The compression method you choose is up to you, so first output and second input of the program for your implementation may differ from others. When second input is provided, you should ignore first input and re-generate the matrix only using the second input (compressed matrix).

It's recommended to test your program using large matrixes with 10,000 rows and 20,000 columns .

In the following sample, the original matrix had 20 members while the compressed one had only 12 members which means 40 percent reduction

# Persian Description
برنامه ای بنویسید یک ماتریس خلوت (Sparce) از ورودی دریافت کرده سپس آن را فشرده کند به صورتی که وقتی خروجی را مجدد به برنامه ارسال کنید ماتریس اولیه را برگرداند.

خط اول ورودی دو عدد n و m برای تعداد ردیف و تعداد ستون ماتریس است. سپس n ردیف حاوی m عدد وارد می شود.

خروجی اولیه برنامه باید فرمت فشرده شده ماتریس باشد به نحوی که وقتی عیناً خروجی به برنامه ارسال شد ماتریس اولیه به عنوان خروجی دوم چاپ شود.
در انتها میزان فشرده سازی به صورت زیر محاسبه و نمایش داده شود:
Compression Ratio = output size / input size

این بدان معنی است که فرمت ماتریس فشرده آزاد و به انتخاب شماست، پس خروجی اول و ورودی دوم برای برنامه شما ممکن است متفاوت باشد. دقت کنید ماتریس اولیه فقط باید بر اساس ورودی دوم (فرمت فشرده) بازسازی شود.

برنامه خود را با ماتریس های تصادفی و ابعاد بزرگ مثلا ۱۰۰۰۰ ردیف و ۲۰۰۰۰ ستون تست کنید.
در این مثال ۲۰ عضو ماتریس به ۱۲ عضو کاهش پیدا کرده است یعنی ۴۰ درصد فشرده سازی.

# Sample Input/Output

## Input:
```
4 5
0 0 0 7 0
4 2 0 0 1
0 0 0 2 0
0  9 0 0 0
4 5
3 7 
0 4 1 2 4 1
3 2
1 9
```

## Output: (Yours may be different) 
```
4 5
3 7 
0 4 1 2 4 1
3 2
1 9
0 0 0 7 0
4 2 0 0 1
0 0 0 2 0
0  9 0 0 0
0.6
```