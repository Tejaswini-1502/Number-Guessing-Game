#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

noOfLoops=0
flag = 0
print(art.logo)
number = random.randint(1,100)
choice = int(input("Select\n1->Easy\n2->Hard\n"))
if choice == 1:
  noOfLoops = 10
elif choice == 2:
  noOfLoops = 5
else:
  print("Invalid Choice")

if choice==1 or choice==2:
  attempts = noOfLoops
  for i in range(noOfLoops):
    guess = int(input("Enter your guess: "))
    if(guess < number):
      print("Too Low")
      attempts-=1
      print(f"You have {attempts} attempts remaining to guess the number")
    elif guess > number:
      print("Too High")
      attempts-=1
      print(f"You have {attempts} attempts remaining to guess the number")
    else:
      flag = 1
      print("Yay!! Yoy guessed it right.\nYOU WIN.")
      break


if flag == 0:
  print(f"You have no more attempts left.\nYOU LOSE.\nThe number is: {number}")

