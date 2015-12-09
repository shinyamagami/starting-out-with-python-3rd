# Chapter.6
# 07. Random Number File Writer

import random

def write():
    object_file = open('random_numbers.txt', 'w')
    how_many = int(input('Enter a number as a integer how many random number'
                          'the file will hold: '))
    for i in range(how_many):
        number = random.randrange(1, 501)
        number = str(number)
        object_file.write(number)
        object_file.write('\n')
    object_file.close()
write()
