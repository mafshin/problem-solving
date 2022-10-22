# Problem 048
Write a program which accepts a folder path in local file system, then
outputs the tree structure of all files and folders beneath that and
calculates the following statistics:

- 5 most used file extensions across all folders (mention the usage numbers)
- 5 largest folders by size (the size of each folder is equal to sum of size of all folders and files under that folder)
- 5 most duplicated files (you should identify duplicate files by 
evaluating the hash of its contents not by the name of the file). For each item
output the full path of all duplicated files.
- 5 paths (folders and files) with highest depth in tree structure 
 (if there are more than one route with same depth, first order by name, then pick the first one)

# Persian Description
برنامه ای بنویسید که آدرس یک پوشه بر روی هارد دیسک دریافت کرده سپس ساختار درختی تمام فایل ها و پوشه های زیر آن آدرس را تشکیل داده و آمارهای زیر را محاسبه کند:

- ۵ پسوند فایل با بیشترین تکرار در سرتاسر پوشه ها (با ذکر تعداد تکرار)
-  ۵ پوشه با بیشترین سایز (سایز هر پوشه معادل مجموع سایز تمام پوشه ها و فایل های زیر آن است)
- ۵ فایل با بیشترین تکرار (فایل تکراری را با بررسی Hash محتوای آن شناسایی کنید, نه با نام فایل). برای هر مورد، آدرس کامل تمام فایل های تکراری در خروجی چاپ شود.
- ۵ مسیر (شامل فایل و پوشه) با بیشترین عمق در ساختار درختی (در صورتی که بیشتر از یک مورد وجود دارد، بر اساس نام صعودی مرتب کنید و اولین مسیر را برگردانید)

# Sample Input/Output

## Input:
```
d:\myfolder
```

## Output: 
```
Top 5 file extensions:
JPG 243
Exe 120
MP3 18
PNG 5
PDF 2

Top 5 largest folders
d:\myfolder\work 2.6GB
d:\myfolder\1\best 1.1GB
d:\myfolder\2\books\new 620MB
d:\myfolder\music 130MB
d:\myfolder\booknew 44MB

Top 5 most duplicated files
d:\myfolder\1\photo.png
Duplicates: (... duplicated files paths)
d:\myfolder\books\120.pdf
Duplicates: (... duplicated files paths)
d:\myfolder\1\78\photo.png
Duplicates: (... duplicated files paths)
d:\myfolder\photo\new.jpg
Duplicates: (... duplicated files paths)
d:\myfolder\120\photo.png
Duplicates: (... duplicated files paths)

Top 5 deepest paths
d:\myfoler\120\43\work\news\reading
d\myfolder\root\word\books\life.pdf
d:\myfolder\names\books\nike.jpg
d:\myfolder\root\word
d:\myfolder\names
```