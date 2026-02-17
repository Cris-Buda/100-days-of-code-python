#conditionals

#if/else

# if condition:
#     do this
# else:
#     do this

water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")



#comparison operators

#>

#<

#>=

#<=

#==

#!=


#Modulo

#%

#x % y == 0 restul e 0

#Exercitiu

number = int(input())

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")



#nested if/else

#if condition:
#   if another condition:
#       do this
#   else:
#       do this
#else:
#   do this



#Exercitiu

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age <= 18:
    print("Please pay 7$")
  else:
    print("Please pay 12$")
else:
  print("Sorry, you have to grow taller before you can ride.")



#if/elif/else

#if condition1:
#   do A
#elif condition2:
#   do B
#  else:
#   do this



#Exercitiu

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    print("Please pay 5$")
  elif age <= 18:
    print("Please pay 7$")
  else:
    print("Please pay 12$")
else:
  print("Sorry, you have to grow taller before you can ride.")



#Exercitiu

height = float(input())
weight = int(input())
BMI = float(weight) / float(height) ** 2
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")
  
#Exercitiu

year = int(input())
if (year % 4) == 0:
  if (year % 100) == 0:
    if(year % 400) == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")



#Multuple if

#if condition1:
#   do A
#if condition2:
#   do B
#if condition3:
#   do C

#Exercitiu

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")



#Exercitiu
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill = 0
if size == "S":
  bill = 15
elif size == "M":
  bill = 20    
elif size == "L":
  bill = 25
if add_pepperoni == "Y":
    bill += 2
else:
    bill += 3
if extra_cheese == "Y":
  bill += 1 
print(f"Your final bill is: ${bill}.")

#Logical operators

#and

#A and B

#or

#C or D

#not

#not E

#Exercitiu

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")



#.lower() function decapitalizeaza toate literele

#.count() function numara de cate ori un caracter se afla intr-un grup de caractere

#Exercitiu

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combined_name = (name1 + name2).lower()

digit1 = combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e')
digit2 = combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e')

score = (digit1 * 10) + digit2

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")



#Proiect

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input("You\'re at a crossed road. Where do you want to go? Type 'left' or 'right' \n").lower()
if direction == "left":
          action = input("You\'ve come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
          if action == "wait":
                    color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
                    if color == "red":
                              print("It's a room full of fire. Game Over.")
                    if color == "yellow":
                              print("You found the treasure! You Win!")
                    if color == "blue":
                              print("You enter a room of beasts. Game Over.")
          else:
                    print("You get attacked by an angry trout. Game Over.")
else:
          print("You fell into a hole. Game Over.")