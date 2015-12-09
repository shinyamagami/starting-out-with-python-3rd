# Chapter.6
# 04. Item Counter

def count():
    object_file = open('names.txt', 'r')
    line = object_file.readline()
    line = line.rstrip('\n')
    count = 0
    while line != '':
        count += 1
        line = object_file.readline()
        line = line.rstrip('\n')
    object_file.close()
count()
print(line)
