# Chapter.8
# 02. Sum of Digits In a String

def read():
    numbers = input('Enter a series of single-digit numbers with nothing'
                    'separating them: ')
    total = 0
    for i in numbers:
        total += int(i)
    print(total)
read()
