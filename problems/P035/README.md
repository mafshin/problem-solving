# Problem 035
Write a program which aligns multiple lines of text based on the
longest common substring.

First line of input N is the number of lines, then N lines follows.
For each free space use `#` as placeholder.

First line of output must contain the longest substring, and 
then the aligned lines of texts should be printed.

# Persian Description
برنامه ای بنویسید که تعدادی متن در خطوط مختلف دریافت کرده و سپس بر اساس طولانی ترین زیر متن مشترک با بیشترین تکرار، آن ها را تراز کند. فضای خالی ابتدا را با # پر کنید. اولین خط خروجی شامل عبارت مشترک باشد سپس خطوط تراز شده چاپ شود

# Sample Input/Output

## Input:
```
4
some yes ok
yes will some do it
it is somehow good yes
yes someone found it
```

## Output: 
```
some
########some yes ok
yes will some do it
##it is somehow good
####yes someone found it
```
