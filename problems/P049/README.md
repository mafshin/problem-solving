# Problem 049
Write a program which calculates the routes of photons emitted from a laser in an imaginary world.

Imagin that you are living in a world of universe which have the following characteristics:
- Width: w
- Height: h
- Two Dimensional

In this world, photos have a special behavior such that when they hit a star, they do not follow normal phyics rules, but the deviates toward the
closes start.

Each star in this world is positioned in position of the world plane.
You are also located in x,y position when you turn on your laser and point 
it to a star with a,b position.

Write the program which calculate the route of laser photons in this world. Route contains the list of stars that laser hit them. Also calculate
the exact time when the photons hit the star. Time zero is when you turn on
the laser.

First line of input is w, h the width and height of the world.
Next line is n, the number of stars, followed by n lines. For each line the name of the star and x, y coordinate of the star is provided.
Next line of the input is x, y of your position and the last line is the name of the star you points your laser toward.

Each unit of distance in this world is one Astronomical Unit or AU. Print the time based on seconds with floating points.

# Persian Description
فرض کنید شما در یکی از جهان های هستی زندگی می کنید که مشخصات زیر را دارد.
- ابعادی به عرض w و ارتفاع h
- دو بعدی
- فوتون های خارجی در این جهان رفتار خاصی دارند، آنگونه که وقتی به ستاره ای برخورد می کنند به سمت نزدیک ترین ستاره بعدی منحرف می شوند.
هر کدام از ستاره های این جهان، دقیقا بر روی یکی از نقاط این صفحه که با عدد صحیح مشخص می شوند قرار دارند. شما نیز در موقعیت x و y حضور دارید که لیزر خود را روش می کنید و به سمت ستاره ای با مختصات a و b نشانه میگیرید.
برنامه ای بنویسید که مسیر حرکت فوتون های خارج شده از لیزر شما را محاسبه کند. مسیر شامل مختصات ستاره هایی هست که لیزر به آن‌ها برخورد می کند. همچنین زمان دقیق برخورد  را نیز محاسبه کنید. زمان صفر، لحظه روشن شدن لیزر است.
ورودی شامل w و h در خط اول، سپس عدد n شامل تعداد ستاره هاست
سپس n خط شامل نام ستاره و مختصات x و y هر کدام است.
ورودی بعدی x و y موقعیت شماست و در خط آخر نام ستاره اولین هدف شما.
هر واحد فاصله در مختصات این جهان, یک AU یا واحد نجومی است. زمان را بر اساس ثانیه (به صورت اعشاری) نشان دهید

# Sample Input/Output

## Input:
```
1000 1000
5
Luna 500 230
Virgo 260 450
Altair 120 890
Miram 530 20
Cyg 1000 650
200 300
Altair
```

## Output: 
```
+680 Altair
+1569.34 Miram
+2178.45 Cyg 
+3409.87 Virgo
+4575.21 Luna
```