# Chapter.6
# 03. Line Numbers

def read():
    file = input('Enter a file name with its extension: ')
    object_file = open(file, 'r')
    line = object_file.readline()
    line = line.rstrip('\n')
    line_number = 1
    while line != '':
        print(line_number, ':', line, sep='')
        line = object_file.readline()
        line = line.rstrip('\n')
        line_number += 1
    object_file.close()
read()
