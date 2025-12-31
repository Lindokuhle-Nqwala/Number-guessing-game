# Import
import random

# Random selection of a guess number
number_to_guess = random.randint(1, 100)

# A while for the game to not stop
while True:
  try:
    # Request a user to guess a number
    user_guess = int(input("Enter a number between 0 and 100: "))

    # Conditions and code to run based on user guess
    if user_guess > number_to_guess:
      print("Number is high!")
    elif user_guess < number_to_guess:
      print("Number is low!")
    else:
      print("Congratulations for guessing the number!")
      break
  except ValueError:
    print("Invalid entry!")
