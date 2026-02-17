################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")



# Local Scope

def drink_potion():
  potion_strength = 2
  print(potion_strength)
drink_potion()



# Global Scope

player_health = 10
def drink_potion():
  potion_strength = 2
  print(player_health)
drink_potion()



# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)



# Modifying Global Scope

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#sau

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")



#Global Constants

PI = 3.14159
URL = "https://www.google.com"



#Proiect

from guess_the_number import logo

import random

list_of_numbers = list(range(1, 101))

print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

correct_number = random.choice(list_of_numbers)

print(f"Pssst, the correct answer is {correct_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard'")
allowed_attempts = 0
if difficulty == "easy":
  allowed_attempts = 10
elif difficulty == "hard":
  allowed_attempts = 5

should_end = False
used_attempts = 0

while used_attempts < allowed_attempts and not should_end:
  guess = int(input(f"You have {allowed_attempts - used_attempts} attempts remaining to guess the number.\nMake a guess: "))
  used_attempts += 1
  if guess == correct_number:
    should_end = True
    print("You guessed!")
  elif guess > correct_number:
    print("Too high.\nGuess again")
  elif guess < correct_number:
    print("Too low.\nGuess again.")

if used_attempts == allowed_attempts:
  print("You've run out of guesses, you lose.")



#sau



from random import randint

from guess_the_number import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()