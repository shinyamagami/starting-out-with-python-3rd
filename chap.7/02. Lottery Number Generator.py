# Chapter.7
# 02. Lottery Number Generator

import random

def generate():
    lottery_list = []
    for i in range(7):
        lottery_list.append(random.randrange(0 ,10))
    print(lottery_list)
    return lottery_list
def display(lottery_list):
    for i in lottery_list:
        print(i)
lottery_list = generate()
display(lottery_list)
