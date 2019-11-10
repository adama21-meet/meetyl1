import turtle
turtle.goto(0,0)
turtle.pensize(8)
turtle.bgcolor('purple')

def up():
    turtle.direction='Up'
    turtle.forward(20)

turtle.onkey(up,'Up')
turtle.goto(0,0)
turtle.listen()

turtle.mainloop()
