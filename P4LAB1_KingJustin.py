#Justin King
#11/3/2024
#P4LAB1
#square and triangle drawing program
import turtle

#set up
t = turtle.Turtle()
t.pensize(2)
t.speed(3)

#draw square
for i in range(4):
    t.forward(100)
    t.right(90)

#move to draw triangle
t.penup()
t.goto(150, 0)
t.pendown()

#draw triangle 
for i in range(3):
    t.forward(100)
    t.left(120)

#keep program open
turtle.done()
