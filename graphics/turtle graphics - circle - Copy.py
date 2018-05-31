import  turtle
import random
turtle.speed(0)
turtle.color("yellow","blue")
for i in range(8):#will give 6 sided rangoli
    for i in range(32):
        turtle.begin_fill()
        turtle.circle(65)
        turtle.end_fill()
        turtle.left(45.0/4)
    turtle.forward(130)#these 2 line s in main loop only
    turtle.left(45)

