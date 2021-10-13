import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 7

def check_answer(guess,random_number):  
  if guess < random_number:
    print("Too low")
  elif guess > random_number:
    print("Too high")
  elif guess == random_number:
    print("You've won!")

def set_difficulty(difficulty):
  if difficulty == 'easy':
    return EASY_LEVEL_ATTEMPTS
  else:
    return HARD_LEVEL_ATTEMPTS

def game():
  print("Welcome to the Number Guessing Game \n I'm thinking of a number between 1 and 100")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  random_number = random.randint(1,100)

  attempts = set_difficulty(difficulty)

  # While loop to allow for continous guessing until attempt ends
  guess = 0
  while guess != random_number and attempts > 0:
    print(f"You have {attempts} attempts remaining")
    guess = int(input("Make a guess: "))
    attempts -= 1
    check_answer(guess,random_number)

game()




    
