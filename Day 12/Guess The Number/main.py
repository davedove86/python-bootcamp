# import random number
from random import randint

# Difficulity level variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check if user guess is correct


def check_answer(guess, answer, turns):
    """ Checks answer against guess, returns number of turns remaining"""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it, the answer was {answer}")

# Set difficulty based on user input


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Game function


def game():
    print("Welcome to the guessing game")

    print("I am thinking of a number between 1 and 100")

    turns = set_difficulty()

    answer = randint(1, 100)
    print(f"The answer is {answer}")

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaning to guess the number.")

        guess = int(input("Make a guess "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again")


game()
