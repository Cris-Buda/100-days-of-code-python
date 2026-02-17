from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# def move_forward():
#     tim.forward(10)
#
# screen.listen()
# screen.onkey(key="space", fun=move_forward)





#Functions as Inputs

# def function_a(something):
#     Do this with something
#     Then do this
#    Finally do this
#
# def function_b():
#     Do this
#
# function_a(function_b)

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(10)

#sau

# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

def move_clockwise():
    tim.right(10)

#sau

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)



#Turtle race

import random

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)











screen.exitonclick()