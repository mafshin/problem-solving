# Problem 033
Write a program which accepts two multi-line text inputs and prints
their differences. The first text is the reference text. 

The end of each text is indicated by END. 
For each removed chracter sequences use `-` and for each added character `+`. You should surround sequence ofcharacters which are either deleted or added.
You can imagine that input texts will not include either `-` or `+`.

Note: This problem is similar to what DiffTools do, Git also uses 
these tools to show changes between commits.

# Persian Description
برنامه ای بنویسید که دو متن (چند خطی) از ورودی دریافت کرده و تفاوت آن دو را نمایش دهد. متن اول مبنا است. پایان ورودی ها با END مشخص می شود. حذف شدن از متن اول را با '-' و اضافه شدن را با '+' در ابتدا و انتهای بخش اضافه یا کم شده نشان دهید. فرض کنید متن های ورودی حاوی - و + نمی باشد.

نکته: ابزارهای DiffTool چنین کاری انجام می دهند. گیت نیز ازین ابزارها استفاده می کند.


# Sample Input/Output

## Input:
```
This is a sample text
which spans across several
lines.
END
is a new text
where spans ross new ver
lines.
END
```

## Output: 
```
-Th-is -is- a +new+ -sample- text
wh-ich-+ere+ spans -ac-ross +new+ -se-ver-al-
lines.
```
