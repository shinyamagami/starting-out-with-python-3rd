# Chapter.5
# 07. Stadium Seating

class_a = int(input('Enter the numuber of tickets for Class A were sold: '))
class_b = int(input('Enter the numuber of tickets for Class B were sold: '))
class_c = int(input('Enter the numuber of tickets for Class C were sold: '))

def total(class_a, class_b, class_c):
    a = class_a * 20
    b = class_b * 15
    c = class_c * 10
    print('The total amount of income generated from ticket sales is $', a + b + c, sep='')

total(class_a, class_b, class_c)


