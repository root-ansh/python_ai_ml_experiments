import  turtle
import random
turtle.speed(0)
choice=["red","green","yellow","blue"]
for i in range(32):
    x,y,=6,7
    for i in range(x+1):
        turtle.forward(200)
        turtle.pencolor("green")
        turtle.left(90)
    turtle.backward((200.0/4))
    turtle.pencolor("green")
    turtle.right(45.0/4)
    
   
a=raw_input()
