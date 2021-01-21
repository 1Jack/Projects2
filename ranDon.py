# rewritten by W.Anderson 14/12/2020
# freeCodeCamp.org https://www.youtube.com/watch?v=8ext9G7xspg
# this is code that generates a number and we have to guess the correct number 

import random

def guess(x):
    randon_Number = random.randint(1, x)
    guess = 0
    while guess != randon_Number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        print(guess)

    
