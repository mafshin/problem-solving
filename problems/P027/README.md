# Problem 027
Write a encoder-decoder which encodes and decodes the input text using
Huffman method. Consider a word as a unit for compression. 

If input starts with `P:` then it's a plain text which must be compressed. Selection of replacement characters for encoding is up to you. Output should contain encoded text with the generated dictionary used for encoding.

If input starts with `E:` then it's a compressed encoded text which must be decoded. Then multiple lines of input will be provided as the encoding dictionary. Output should contain the decoded (uncompressed) text.

The delimiters between words are space character.

# Persian Description
برنامه ای بنویسید که یک رشته طولانی دریافت کرده و آن را به روشی مشابه Huffman با ساخت دیکشنری بر اساس تعداد تکرار فشرده کند. یک «کلمه» را واحد فشرده سازی در  نظر بگیرید. ورودی به این صورت است که اگر با P: شروع شود به معنای متن اصلی است که باید فشرده شود و اگر با E: شروع شود متن فشرده است که باید به حالت اولیه برگردد. انتخاب کاراکترهای جایگزین برای Encoding آزاد است. در حالت Encoding خروجی باید شامل متن Encode شده و دیکشنری تولید شده باشد.
در حالت Decoding متن ورودی باید شامل متن Encode شده و دیکشنری همراه آن باشد (پایان دیکشنری با END مشخص می شود). جدا کننده کلمات را space در نظر بگیرید.

# Sample Input/Output

## Input:
```
P: This text is a very long text which has many repeated text inside this long text

E: a b c d e f b g h i j b k l f m
a This
b text
c is
d a
e very
f long
g which
h has
i many
j repeated
k inside
l this
m text.
```

## Output: 
```
a b c d e f b g h i j b k l f m
a This
b text
c is
d a
e very
f long
g which
h has
i many
j repeated
k inside
l this
m text.

This text is a very long text which has many repeated text inside this long text.
```
