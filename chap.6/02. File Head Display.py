# Chapter.6
# 02. File Head Display

def read():
    file = input('Enter a file name with its extension: ')
    object_file = open(file, 'r')
    line = object_file.readline()
    line = line.rstrip('\n')
    count = 0
    while count <= 4:
        if line == '' :
            count += 5
        else:
            print(line)
            line = object_file.readline()
            line = line.rstrip('\n')
            count += 1
def main():
    read()

main()
