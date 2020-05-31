import  turtle
import random
turtle.speed(0)
#for i in range(6):#will give 6 sided rangoli
a='green','red'
turtle.color('blue','blue')
for i in range(64):
    if i%32<>0:
        b=random.choice(a)
        turtle.color(b,b)
    turtle.circle(150)
    turtle.left(45.0/4)

#turtle.forward(150)#these 2 line s in main loop only
#turtle.left(60)

a=raw_input()
