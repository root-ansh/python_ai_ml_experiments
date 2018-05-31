import  turtle
import random
turtle.speed(0)
choice=["red","green","yellow","blue"]
for i in range(100):
    x,y,=6,6
    for i in range(x+1):
        turtle.forward(100)
        turtle.pencolor("green")
        turtle.left(60)
    turtle.left(45)
    turtle.forward(100)
    for i in range(x+1):
        turtle.forward(100)
        turtle.pencolor("green")
        turtle.left(60)

        
a=raw_input()
