# importing random module
import random

# Welcome message
print("Welcome to the guess game")
print("Range for the gusses is 1 to 50")

# Taking input from the user
guess = int(input("What is your guess? : "))

# Generate the number to be guessed with random module
correct_number = random.randint(0, 50)

# Define the number of guesses
guesses = 1

# Logic for comparing the gussed and correct number
while guess != correct_number:
    guesses += 1
    if(guess < correct_number):
        print("You have to guess a little higher number")
    if(guess > correct_number):
        print("You have to guess a little lower number")
    guess = int(input("Write a number between 0 to 50 : "))

print(f"Wow!! You guessed it right!")
print(f"It took {guesses} guesses for you to guess {correct_number} is the correct number.")