# Chapter.5
# 11. Math Quiz

import random

number1 = random.randint(1, 1000)
number2 = random.randint(1, 1000)
total = number1 + number2
print('\t', format(number1, '4.0f'))
print('+\t', format(number2, '4.0f'))

answer = int(input('Enter the answer: '))

def check(answer, total):
    if answer == total:
        print('Congratulation!')
    else:
        print('The answer is', total)

check(answer, total)
