# Chapter.8
# 05. Alphabetic Telephone Number Translator

def description():
    print('This program asks users to enter a file name to open and translate'
          'alphabetic numbers in it into numeric numbers.')
def get_file():
    return input('Enter a file name with its extension: ')
def make_list(object_file):
    phone_numbers = object_file.readlines()
    index = 0
    print('The list has', len(phone_numbers), 'lines')
    while index < len(phone_numbers):
        phone_numbers[index] = phone_numbers[index].rstrip('\n')
        index +=1
    print(phone_numbers)
    return phone_numbers
def convert(phone_numbers):
    index = 0
    a = 0
    new_object = open('numericnumbers.txt', 'w')
    while index < len(phone_numbers):
#        print(phone_numbers[index])
        number = ''
        for i in phone_numbers[index]:
#            print(i)
            if i == '0':
                a = '0'
                number += a
            elif i == '1':
                a = '1'
                number += a
            elif i == '2' or i == 'A' or i == 'B' or i == 'C':
                a = '2'
                number += a
            elif i == '3' or i == 'D' or i == 'E' or i == 'F':
                a = '3'
                number += a
            elif i == '4' or i == 'G' or i == 'H' or i == 'I':
                a = '4'
                number += a
            elif i == '5' or i == 'J' or i == 'K' or i == 'L':
                a = '5'
                number += a
            elif i == '6' or i == 'M' or i == 'N' or i == 'O':
                a = '6'
                number += a
            elif i == '7' or i == 'P' or i == 'Q' or i == 'R' or i == 'S':
                a = '7'
                number += a
            elif i == '8' or i == 'T' or i == 'U' or i == 'V':
                a = '8'
                number += a
            elif i == '9' or i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
                a = '9'
                number += a
            else:
                a = '-'
                number += a
        print(number)
        new_object.write(number)
        new_object.write('\n')
        index += 1
    new_object.close()
def main():
    description()
    file = get_file()
    object_file = open(file, 'r')
    phone_numbers = make_list(object_file)
    object_file.close()
    convert(phone_numbers)
main()
