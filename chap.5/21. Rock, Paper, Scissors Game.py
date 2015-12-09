# Chapter.5
# 21. Rock, Paper, Scissors Game

import random

def set_up():
    n = random.randrange(1, 4)
    com = ''
    if n == 1:
        com = 'rock'
    elif n == 2:
        com = 'scissors'
    else:
        com = 'paper'
    choice = input('Choose and enter one among \'rock\', \'scissors\' or'
                       '\'paper\': ')
    print(com)
    return com, choice
def rule(com, choice):
    while com == choice:
        com, choice = set_up()
    else:
        if com == 'rock' and choice == 'scissors':
            print('Computer wins!')
        elif com == 'scissors' and choice == 'rock':
            print('You wins!')
        elif com == 'paper' and choice == 'scissors':
            print('You wins!')
        elif com == 'scissors' and choice == 'paper':
            print('Computer wins!')
        elif com == 'rock' and choice == 'paper':
            print('You wins!')
        elif com == 'paper' and choice == 'rock':
            print('Computer wins!')
def main():
    com, choice = set_up()
    rule(com, choice)
main()
