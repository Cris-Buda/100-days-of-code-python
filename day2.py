#Data types

#String

"Hello"



#Integer

1234567890

#sau

123_456_789



#Float

12345.06789



#Boolean

True

#sau

False



#Subscript - Caracterul de la pozitia indicata

print("Hello"[0])



#type() function

num_char = len(input("What is your name?"))
print(type(num_char))



#Type conversion

#str()

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

#Exemple

print(70 + float("100.5"))

print(str(70) + str(100))

#Exercitiu

two_digit_number = input()
num1 = two_digit_number[0]
num2 = two_digit_number[1]
print(int(num1) + int(num2))

#int() function

print(int(2.35))

#float() function

print(float(3))



#Operations

#Addition

1 + 2

#Subtraction

2 - 3

#Multiplication

3 * 4

#Division

4 / 5

#Exponent

5 ** 6

#Ordinea efectuarii operatiilor
#PEMDAS
#Parantheses
#Exponent
#Multiplication
#Division
#Addition
#Subtraction

#Exemplu

print(3 * 3 + 3 / 3 - 3)

print(3 * (3 + 3) / 3 - 3)

#Exercitiu

height = input()
weight = input()
BMI = float(weight) / float(height) ** 2
print(int(BMI))



#Number manipulation

#round() function

print(round(8 / 3))

#round() cu zecimale

print(round(8 / 3, 2))

#sau

print(round(2.66666666, 2))



#// pentru integer direct din operatie

print(8 // 3)



#Continuarea operatiei

result = 4 / 2
result /= 2
print(result)



#f-Strings

score = 0
height = 1.8
isWining = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWining}")



#Exercitiu

age = input()
total_years = 90
weeks_in_year = 52
weeks_left = (total_years - int(age)) * weeks_in_year

print(f"You have {weeks_left} weeks left.")



#Proiect

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
persons = int(input("How many people to split the bill?"))

pay = round(bill * ((tip / 100) + 1) / persons, 2)

print(f"Each person should pay: ${pay}")