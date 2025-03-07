import turtle

from Tools.demo.ss1 import center

screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('tan')
t=turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor("blue")
t.pensize(3)
t.circle(35)
t.penup()
t.goto(-40,-20)
t.pendown()
t.pencolor('yellow')
t.circle(35)
t.penup()
t.goto(0,15)
t.pendown()
t.pencolor('black')
t.circle(35)
t.penup()
t.goto(40,-20)
t.pendown()
t.pencolor('green')
t.circle(35)
t.penup()
t.goto(80,15)
t.pendown()
t.pencolor('red')
t.circle(35)
t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('purple')
t.write("Winter Olympics",font=("Arial",20,"normal"),align="center")
t.penup()
t.goto(0,-55)
t.pendown()
t.write("2026",font=("Arial",20,"normal"),align="center")


















turtle.done()