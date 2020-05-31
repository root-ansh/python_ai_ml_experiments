import turtle
turtle.speed(0)
l=50
ang=15
turtle.color("black","yellow")
for i in range(100):
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(l)
        turtle.left(120)
    turtle.end_fill()
    l+=2
    turtle.left(ang)
