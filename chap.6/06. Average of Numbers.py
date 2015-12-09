# Chapter.6
# 06. Average of Numbers

def read():
    object_file = open('numbers.txt', 'r')
    count = 0
    total = 0
    for i in object_file:
        total += int(i)
        count += 1
    print(total / count)
    object_file.close()
read()
