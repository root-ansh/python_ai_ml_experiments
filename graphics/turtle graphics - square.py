import  turtle
import random
turtle.speed(0)
choice=["red","green","yellow","blue"]
for i in range(10):
    x,y,=6,7
    for i in range(x+1):
        turtle.forward(100)
        turtle.pencolor("green")
        turtle.left(90)
    turtle.backward((100.0/2))
    turtle.pencolor("green")
    turtle.right(45)
    
   
a=raw_input()
