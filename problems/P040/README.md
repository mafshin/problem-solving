# Problem 040
Write a program which controls a soccer robot.

Input is in the following format:
S
G1 G2
B
R
N

Field of game is a foursquare of of size S, the gate is determined by G1 and G2 points. The ball and robot are located in point B and R respectively.
Robot can only move in vertical and horizontal directions by one unit.
When the robot hits the ball, the ball will be moved by one unit in the direction of robot movement. 
Note that robot can't go beyond the borders of the field but it can move
along the borders.
The last input is N which determines the number of solutions that must 
be generated for making a goal by shooting the ball into gate.

Output contains N lines, one line per all robot movements to shoot the ball
into gate. The robot movement are represented by the following codes:
U: Up
D: Down
R: Right
L: Left

In this sample, ball will enter the gate at position (10,7).

# Persian Description
برنامه ای بنویسید که یک ربات فوتبالیست را کنترل کند.

زمین بازی یک مربع با اضلاع S است، دروازه با نقاط G1 و G2 مشخص می شود. 
در شروع توپ بازی در نقطه B قرار دارد. و ربات در نقطه R. 
ربات تنها می تواند بر روی خطوط عمودی و افقی به اندازه یک واحد حرکت کند.
هنگامی که ربات با توپ برخورد می کند، به اندازه یک واحد توپ را در جهتی که ربات حرکت می کرده، جابجا می کند.
دقت کنید ربات نمی تواند از مرز زمین خارج شود ولی میتواند روی مرز زمین جابجا شود.
آخرین ورودی N است که تعیین می کند چند راه حل برای رساندن توپ به دروازه نیاز است تولید شود.
ورودی به ترتیب شامل خطوط زیر است
S
G1 G2
B
R
N

خروجی شامل N خط می باشد که هر خط شامل حرکات ربات ربات تا رساندن توپ به دروازه (عبور از مرز زمین) را تعیین می کند.
حرکات ربات به صورت زیر نمایش داده می شود
U به سمت بالا
D به سمت پایین
R به سمت راست
L به سمت چپ 

در این نمونه توپ از نقطه 10,7 وارد دروازه می شود.

# Sample Input/Output

## Input:
```
10
10,5 10,8
2,1
7,4
1
```

## Output: 
```
D D D D L L L L L U U U U U U L U R R R R R R R R R
```