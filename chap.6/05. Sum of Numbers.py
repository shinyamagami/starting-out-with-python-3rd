# Chapter.6
# 05. Sum of Numbers

def count():
    object_file = open('numbers.txt', 'r')
    total = 0
    for i in object_file:
        i = int(i.rstrip('\n'))
        total += i
        print(i)
    print('The total is', total)
    object_file.close()
count()

