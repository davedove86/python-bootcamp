# get random number
import random

number_answer = random.randint(1, 10)
print(f'Your random number is {number_answer}')

lives = []
easy = 10
hard = 5

# add two levels - Easy & Hard
# Ask the player to pick a level
difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ")

# if they pick Easy they get 10 lives
# If they pick Hard they get 5 lives
if difficulty == 'easy':
    lives = 10
else:
    lives = 5

print(f"Your lives are {lives}")

# Ask the player to guess the number
