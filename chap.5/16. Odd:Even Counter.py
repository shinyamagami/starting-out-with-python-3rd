# Chapter.5
# 16. Odd/Even Counter

import random

def odd_even():
    count = 0
    odd = 0
    even = 0
    while count < 100:
        number = random.randrange(1, 101)
        count +=1
        print(number)
        if number % 2 != 0:
            even += 1
        else:
            odd += 1
    print('The time of odd is', odd, 'and the time of even is', even)
odd_even()
