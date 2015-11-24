# Chapter.4
# 08. Sum of Numbers

number = float(input('Enter a positive number or enter a negative number '
                     'if you want to end: '))
total = 0
while number > 0:
    total += number
    number = float(input('Enter a positive number: '))
print('The sum is', total)
