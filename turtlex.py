import turtle
t = turtle.Turtle()
t.shape("turtle")

t.fillcolor("blue")

t.begin_fill()
t.penup()
t.goto(-200,-100)
t.pendown()
t.goto(300, -100)
t.goto(300, 200)
t.goto(-200, 200)
t.goto(-200,-100)
t.end_fill()

t.fillcolor("brown")
t.penup()
t.begin_fill()
t.goto(0,0)
t.pendown()
t.goto(0,100)
t.goto(100,100)
t.goto(100,0)
t.goto(0,0)
t.end_fill()
t.penup()

turtle.done()