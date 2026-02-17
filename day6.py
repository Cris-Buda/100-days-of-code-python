#Functions

def my_function():
    print("Hello")
    print("Bye")

my_function()

#Defining Functions

#def my_function():
#   do this
#   then do this
# finally do this

#Calling Functions

#my_function()



#Reeborg's world

#Exercitiu

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

#Exercitiu

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

#for step in range(6):
#    jump()



#Function with if inside
# def my_function():
#     if sky == "clear":
#         print("blue")
#     else:
#         print("grey")



#While loop

# while something_is_true:
#     do something repeatedly

#Exercitiu

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#      move()
#      turn_left()
#      move()
#      turn_right()
#      move()
#      turn_right()
#      move()
#      turn_left()

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)



#Exercitiu

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#      move()
#      turn_left()
#      move()
#      turn_right()
#      move()
#      turn_right()
#      move()
#      turn_left()

# while at_goal() == False:
#     jump()

#sau

# while not at_goal():
#     jump()



#Infinite loop

# while 5 > 3:
#     do this
#     then do this
#     then do this



#Exercitiu

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#      turn_left()
#      move()
#      turn_right()
#      move()
#      turn_right()
#      move()
#      turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()



#Exercitiu

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     while wall_in_front() == True:
#         turn_left()
#         move()
#         turn_right()  
#     move()
#     turn_right()
#     while front_is_clear() == True:
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

#sau

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear() == True:
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()



#Proiect

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def turn_around():
#     turn_left()
#     turn_left()

# while not at_goal():
#     if front_is_clear() and right_is_clear():
#         turn_right()
#         move()
#     elif right_is_clear() and wall_in_front():
#         turn_right()
#         move()
#     elif front_is_clear() and wall_on_right():
#         move()
#     elif wall_on_right() and wall_in_front():
#         turn_around()
#     elif wall_in_front():
#         turn_right()

#sau

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

#sau pentru intermediari

# while front_is_clear():
#     move()
#     turn_left()
#     while not at_goal():
#         if right_is_clear():
#             turn_right()
#             move()
#         elif front_is_clear():
#             move()
#         else:
#             turn_left()