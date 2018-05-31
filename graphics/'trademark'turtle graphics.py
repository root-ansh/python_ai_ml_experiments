
import  turtle
import random
turtle.speed(0)
choice=["red","yellow","green","blue"]
c1,c2,c3,c4=random.choice(choice),random.choice(choice),random.choice(choice),random.choice(choice)
while c1==c2 or c1==c3 or c1==c4 or c2==c3 or c2==c4 or c3==c4:
    
    if c1==c2 or c1==c3 or c1==c4 or c2==c3 or c2==c4 or c3==c4:
        c1,c3,c2,c4=random.choice(choice),random.choice(choice),random.choice(choice),random.choice(choice)

        
for i in range(10):
    x,y,=6,7
    turtle.color(c1,c2)
    turtle.begin_fill()
    
    for i in range(x+1):
        turtle.forward(55)
        turtle.left(60)
        
    turtle.end_fill()

    
    turtle.color(c2,c3)
    turtle.begin_fill()
    
    for j in range(y+1):
        turtle.forward(55)
        turtle.right(60)

    turtle.end_fill()
for i in range(2):
    
    turtle.forward(55)
    turtle.right(60)

turtle.color(c3,c4)
turtle.begin_fill()
for i in range(6):
    turtle.forward(55)
    turtle.left(60)
turtle.end_fill()

print"c1,c2,c3,c4=",c1,c2,c3,c4
a=raw_input()
