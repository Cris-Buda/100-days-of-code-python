# print() function

print("Hello World!")

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

#sau

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.")



# print modifiers "", '', /

print('She said: "Hello" and then left.')

print("She said: \"Hello\" and then left.")

print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")



# string concatenation

print("Hello" + "Angela")

print("Hello" + " " + "Angela")

#sau

print("Hello " + "Angela")

#sau

print("Hello" + " Angela")



#input

input("What is your name?\n")

print("Hello " + input("What is your name?\n"))



# len() function

print(len(input()))

#sau

name = input("What is your name?\n")
print(len(name))

# variable *store a value and *retain a value

a = input()
b = input()
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)



#Day 1 project Band Name Generator

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
city_name = input("What's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city_name + " " + pet_name)
#5. Make sure the input cursor shows on a new line