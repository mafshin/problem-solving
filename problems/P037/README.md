# Problem 037
Write a program to receive a large input text along with a 
list of stop words to be removed from text.

# Persian Description
برنامه ای بنویسید که یک متن طولانی از ورودی دریافت کرده و سپس یک لیست از کلمات Stop Words دریافت کند سپس کلمات را از متن حذف کرده و متن را چاپ کند.
دقت کنید متن ورودی می تواند خیلی طولانی باشد.

# Sample Input/Output

## Input:
```
Today is president resignation date, a vantage point in history of our country. You, the next generation of this soil, will decide who should take control of your country.
END
soil
president
vantage
country
END
```

## Output: 
```
Today is resignation date, a point in history of our. You, the next generation of this, will decide who should take control of your.
```