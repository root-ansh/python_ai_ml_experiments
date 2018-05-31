import  turtle
import random
turtle.speed(10)
choice=["red","green","yellow","blue"]
for i in range(10):
    x,y,=6,8
    turtle.color("green","yellow")
    turtle.begin_fill()
    
    for i in range(x+1):
        turtle.forward(55)
        turtle.left(60)
        
    turtle.end_fill()

    
    turtle.color("yellow","green")
    turtle.begin_fill()
    
    for j in range(y+1):
        turtle.forward(55)
        turtle.right(60)
    
    turtle.end_fill()
        
   
a=raw_input()
