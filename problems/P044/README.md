# Problem 044
Write a program which receives a list of numbers, then followed by multiple numbers in multiple lines. The `END` marks the end of input.

For each number N after first line of input, find a subset of numbers in 
the list which have the following conditions:

- The sum of the subset numbers is equal to N

If there exist multiple subset with first condition, then pick the subset:
- Having the sum of all of its numbers digits being minimum. (Higher priority)
- Number of elements in the subset beging minimum

If both of above conditions are equal, then print all answers.

# Persian Description
برنامه ای بنویسید که یک لیست از اعداد دریافت کرده سپس به ازای هر عدد ورودی یک زیر مجموعه از اعداد لیست دریافتی را پیدا کند که شرایط زیر را داشته باشید:

حاصلجمع اعداد آن با عدد ورودی برابر باشد
در صورت وجود چندین جواب، جمع ارقام تمام اعداد آن حداقل باشد. (اولویت بالا) 
تعداد اعضا نیز حداقل باشد. (اولویت پایین)
در صورت برابری هر دو شرط، تمام جواب ها نمایش داده شود.
 
پایان ورودی END است.

# Sample Input/Output

## Input:
```
9 20 8 4 23 1 34 28 2 110 63 24 11
12
28
123 
30
END
```

## Output: (Yours may be different) 
```
12 = 1 + 11
28 = 24 + 4 
123 = 11 + 110 + 2
30 = 9 + 20 + 1 = 20 + 8 + 2
```