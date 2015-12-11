# Chapter.8
# 04. Morse Code Converter

def read():
    string = input('Enter a string: ')
    return string
def convert(string):
    string = string.upper()
    morse = ''
    for i in string:
#        print(i)
        if i == ' ':
            morse += ' '
        elif i == ',':
            morse += '--..--'
        elif i == '.':
            morse += '.-.-.-'
        elif i == '?':
            morse += '..--..'
        elif i == '0':
            morse += '-----'
        elif i == '1':
            morse += '.----'
        elif i == '2':
            morse += '..---'
        elif i == '3':
            morse += '...--'
        elif i == '4':
            morse += '....-'
        elif i == '5':
            morse += '.....'
        elif i == '6':
            morse += '-....'
        elif i == '7':
            morse += '--...'
        elif i == '8':
            morse += '---..'
        elif i == '9':
            morse += '----.'
        elif i == 'A':
            morse += '.-'
        elif i == 'B':
            morse += '-...'
        elif i == 'C':
            morse += '-.-.'
        elif i == 'D':
            morse += '-..'
        elif i == 'E':
            morse += '.'
        elif i == 'F':
            morse += '..-.'
        elif i == 'G':
            morse += '--.'
        elif i == 'H':
            morse += '....'
        elif i == 'I':
            morse += '..'
        elif i == 'J':
            morse += '.---'
        elif i == 'K':
            morse += '-.-'
        elif i == 'L':
            morse += '.-..'
        elif i == 'M':
            morse += '--'
        elif i == 'N':
            morse += '-.'
        elif i == 'O':
            morse += '---'
        elif i == 'P':
            morse += '.--.'
        elif i == 'Q':
            morse += '--.-'
        elif i == 'R':
            morse += '.-.'
        elif i == 'S':
            morse += '...'
        elif i == 'T':
            morse += '-'
        elif i == 'U':
            morse += '..-'
        elif i == 'V':
            morse += '...-'
        elif i == 'W':
            morse += '.--'
        elif i == 'X':
            morse += '-..-'
        elif i == 'Y':
            morse += '-.-'
        elif i == 'Z':
            morse += '--..'
    print(morse)
string = read()
convert(string)
