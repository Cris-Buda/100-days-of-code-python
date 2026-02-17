#Random Module

import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")



#Import a Module

import my_module
print(my_module.pi)



#Exercitiu

import random
random_side = random.randint(0, 1)
if random_side == 0:
  print("Tails")
else:
  print("Heads")



#Lists

#fruits = [item1, item2]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america)

#Alege din lista itemul de la pozitia dorita
print(states_of_america[0])
print(states_of_america[-1])

#Inlocuieste itemul de la pozitia dorita cu alt item
states_of_america[1] = "Pencilvania"
print(states_of_america)

#Adauga un singur item nou in lista
#.append() function
states_of_america.append("Angelaland")
print(states_of_america)

#Adauga mai multi itemi la lista
#.extend() function
states_of_america.extend(["Dreamland","Jack Bauer Land"])
print(states_of_america)

#Creeaza o lista pe baza de input cu un anumit format

#names = names_string.split(", ")

#Exercitiu

names = ["James", "John", "Ben", "Harry", "Jack", "Angela", "Jenny", "Michael", "Chloe"]
import random
number_of_person = len(names)
person = random.randint(0, number_of_person - 1)
pay = names[person]
print(f"{pay} is going to buy the meal today!")



#Nested lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

#Alegerea listei din lista

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0])
print(dirty_dozen[1])

#Alegerea itemului dintr-o lista din lista

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

#Exercitiu

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
row_literal = position[0]
line_to_update = int(position[1]) - 1

if row_literal == "A":
    row_to_update = 0
elif row_literal == "B":
    row_to_update = 1
elif row_literal == "C":
    row_to_update = 2

map[line_to_update][row_to_update] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

#sau

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
row_literal = position[0].lower()
abc = ['a', 'b', 'c']

row_to_update = abc.index(row_literal)
line_to_update = int(position[1]) - 1

map[line_to_update][row_to_update] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")



#Proiect

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Invalid input")
    
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
print(f"Computer chose {computer_choice}.")

if user_choice == 0 and computer_choice == 2:
    print("You win.")
elif user_choice == 2 and computer_choice == 1:
    print("You win.")
elif user_choice == 1 and computer_choice == 0:
    print("You win.")
elif user_choice == computer_choice:
    print("It's a draw.")
else:
    print("You lose.")

#sau

import random

games_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("Invalid input.")
else:
    print(games_images[user_choice])
    
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(games_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win.")
elif user_choice == 2 and computer_choice == 1:
    print("You win.")
elif user_choice == 1 and computer_choice == 0:
    print("You win.")
elif user_choice == computer_choice:
    print("It's a draw.")
else:
    print("You lose.")