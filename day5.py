#For Loop

#for item in list_of_items:
    #do something to each item

fruits = ["apple", "peach", "pear"]
for fruit in fruits:
  print(fruit)

#Multiple action in one loop

fruits = ["apple", "peach", "pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " pie")

#Exercitiu

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

student_number = 0
for student in student_heights:
    student_number += 1
print(f"number of students = {student_number}")

average_height = round(total_height / student_number)
print(f"average height = {average_height}")

#sau

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

student_number = len(student_heights)
print(f"number of students = {student_number}")

average_height = round(total_height / student_number)
print(f"average height = {average_height}")



#Exercitiu

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# Write your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")



#For loop with range

#for number in range(a, b):
#  print(number)

for number in range(1, 10):
  print(number)

for number in range(1, 11):
  print(number)

#For loop with range and step

for number in range(1, 11, 3):
  print(number)



even_sum = 0
for number in range(1, 101):
  even_sum += number
print(even_sum)



#Exercitiu
target = int(input()) # Enter a number between 0 and 1000
even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)



#Exercitiu
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)



#Proiect: Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

random_letters = []
for letter in range(0, nr_letters):
  random_letters += [random.choice(letters)]
random_symbols = []
for symbol in range(0, nr_symbols):
  random_symbols += [random.choice(symbols)]
random_numbers = []
for number in range(0, nr_numbers):
  random_numbers += [random.choice(numbers)]

easy_password = random_letters + random_symbols + random_numbers
final_easy_password = ''.join(easy_password)
print(final_easy_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(easy_password)
final_hard_password = ''.join(easy_password)
print(final_hard_password)



#sau

password = []
for char in range(1, nr_letters + 1):
  password += random.choice(letters)
for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)
print(password)

random.shuffle(password)
print(password)

password_string = ""
for char in password:
  password_string += char

print(f"Your password is {password_string}")
