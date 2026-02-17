#import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r,g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

colormode(255)

screen = Screen()

screen.setup(350,350)

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
 (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# rows = 10
# colons = 10
# tim.setposition(-230,-230)
# tim.setheading(0)
#
# for c in range(rows):
#     for _ in range(colons):
#         tim.dot(20, random.choice(color_list))
#         tim.forward(50)
#     tim.setheading(90)
#     tim.forward(50)
#     tim.setheading(180)
#     tim.forward(colons * 50)
#     tim.setheading(0)

#sau

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dots in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = Screen()
screen.exitonclick()