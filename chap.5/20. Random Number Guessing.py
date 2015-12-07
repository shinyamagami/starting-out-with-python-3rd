# Chapter.5
# 20. Random Number Guessing Game

import random

y = 'y'
while y == 'y' or y == 'Y':
    r = random.randrange(1, 101)
    def guess(r):
        number = int(input('Enter a integer betweeen 1 to 100 to guess a number: '))
        while r != number:
            if number > r:
                print('Too high')
                number = int(input('Enter a integer betweeen 1 to 100 to guess a number: '))
            elif number < r:
                print('Too low')
                number = int(input('Enter a integer betweeen 1 to 100 to guess a number: '))
        print('Congratulatioin!!')
    guess(r)
    y = input('Do this again? If yes, enter y or Y. If no, enter other letters')
