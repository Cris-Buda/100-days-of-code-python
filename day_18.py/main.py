import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue2")
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


#Import pentru o singura folosire
# import turtle
# tim = turtle.Turtle()

#Import pentru multipla folosire
# from turtle import Turtle
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()

#Importing everything
# from random import *
# choice([1, 2, 3])


#Aliasing Modules
import turtle as t
tim = t.Turtle()


timmy_the_turtle.penup()
timmy_the_turtle.forward(100)
timmy_the_turtle.pendown()
for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


timmy_the_turtle.forward(100)
i = 3
while i < 11:
    timmy_the_turtle.color(random.choice(colours))
    for _ in range(i):
        timmy_the_turtle.right(360 / i)
        timmy_the_turtle.forward(100)
    i += 1

#sau

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
# for shape_side_n in range(3, 11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)



import turtle as t
import random

tim = t.Turtle()

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))



#Tuples
#they are Immutable
#my_tuple = (1, 3, 8)
#my_tuple[2] '''8'''

#Random RGB color

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r, g, b

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



#Spirograph

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

for _ in range(36):
    tim.color(random_color())
    tim.circle(100)
    tim.left(10)

#sau

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)



screen = Screen()
screen.exitonclick()
