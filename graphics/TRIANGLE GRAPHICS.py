# file contains the following unicode character -*- \xf3 -*-
import turtle,random
a=256
choice='yellow','blue','red'
turtle.speed(0)
for i in range(5):
    c1,c2=random.choice(choice),random.choice(choice)
    turtle.color(c1,c2)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(a)
        turtle.left(120)
    turtle.end_fill()
    turtle.forward(a/2)
    turtle.left(60)
    a=a/2
raw_input()
