# Chapter.3
# 9. Roulette Wheel Colors

number = int(input('Please enter a pocket number in the range of 0 through 36: '))

if number == 0:
    print('Green')
elif number >= 1 and number <= 10:
    if number % 2 != 0:
        print('Red')
    else:
        print('Black')
elif number >= 11 and number <= 18:
    if number % 2 != 0:
        print('Black')
    else:
        print('Red')
elif number >= 19 and number <= 28:
    if number % 2 != 0:
        print('Red')
    else:
        print('Black')
elif number >= 29 and number <= 36:
    if number % 2 != 0:
        print('Black')
    else:
        print('Red')
else:
    print('Error')
