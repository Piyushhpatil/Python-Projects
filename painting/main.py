import turtle as t
from turtle import Screen
import random


# def move():
#
#     timmy.forward(100)
#     timmy.left(90)
#
# for i in range(4):
#     move()

# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
# side = 3
# while side < 10:
#     for i in range(side):
#         timmy.forward(100)
#         timmy.left(360/side)
#     side+=1
timmy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rcolors = (r, g ,b)
    return rcolors
# x = 0
# y = [0, 90, 180, 270]
# timmy.pensize(10)
# while x < 1:
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(y))
#     timmy.speed("fastest")
# for i in range(100):
#     timmy.speed("fastest")
#     timmy.color(random_color())
#     timmy.circle(100)
#
#     current_head = timmy.heading()
#     timmy.setheading(current_head + 10)
timmy.penup()
timmy.setposition(-450, -350)
timmy.pendown()
for i in range(100):
    timmy.speed("fastest")
    timmy.dot(10, random_color())
    timmy.penup()
    timmy.forward(25)
    timmy.pendown()
    timmy.dot(10, random_color())



















screen = Screen()
screen.exitonclick()