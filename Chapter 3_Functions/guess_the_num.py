"""
This is a "Guess The Number" game.
"""

import random
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for taken_guesses in range(1, 7):
    guess = int(input('Take a guess.\n'))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        # This condition is the correct guess!
        break

if guess == secret_number:
    print(f'Good job! You guessed my number in {str(taken_guesses)} guesses!')
else:
    print(f'Nope. The number I was thinking of was {str(secret_number)}.')
