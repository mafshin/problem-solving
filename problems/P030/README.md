# Problem 030
Write a program which finds the sequence of characters for a word from a table of characters.

First line of input is N, then N lines of N characters are entered.
Then multiple lines are entered which will be terminated by END.

The characters can form a word if they are beside each other (not more than 1 character distance).

For each word, find the position of its characters in the table.

# Persian Description
برنامه ای بنویسید که یک لیست دو بعدی از حروف دریافت کرده، سپس به ازای هر کلمه ورودی در جدول حروف، به دنبال این کلمه بگردد، در صورت یافت شدن کلمه، مختصات حروف آن را چاپ کند.
ورودی اول n اندازه جدول، سپس n خط شامل n کاراکتر وارد می شود. سپس در هر خط یک کلمه برای جستجو وارد می شود. خاتمه ورودی END است. جستجو میتواند عمودی افقی یا عرضی یا ترکیبی از همه باشد. تنها شرط پشت سر هم بودن کاراکتر هاست

# Sample Input/Output

## Input:
```
5
K D E W B
O W A F L
O I T R O
B U R F S
V D T J E
sofa
fruit
impossible 
dart
END
```

## Output: 
```
sofa is (4,5) (3,5) (2,4) (2,3)
fruit is (4,4) (4,3) (4,2) (3,2) (3,3)
impossible is not found
dart is (1,2) (2,3) (3,4) (3,3)
```
