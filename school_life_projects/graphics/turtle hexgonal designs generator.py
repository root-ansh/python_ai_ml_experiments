import  turtle
import random
turtle.speed(0)
choice=["red","green","yellow","blue"]
x,y,=random.randint(6,10),random.randint(6,10)
for i in range(30):
    turtle.color("green","yellow")
    turtle.begin_fill()
    
    for i in range(x+1):
        turtle.forward(25)
        turtle.left(60)
        
    turtle.end_fill()

    
    turtle.color("yellow","green")
    turtle.begin_fill()
    
    for j in range(y+1):
        turtle.forward(25)
        turtle.right(60)
    
    turtle.end_fill()
        
print"x,y=",x,y   
a=raw_input()
