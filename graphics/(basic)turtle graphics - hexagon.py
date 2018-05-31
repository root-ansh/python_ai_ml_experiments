import  turtle
import random
turtle.speed(0)
l=150.00
ang=60
choice=["green","yellow",]
for j in range(7):
    turtle.forward(l)
    turtle.left(ang)
    turtle.pencolor(random.choice(choice))
        
a=raw_input()

