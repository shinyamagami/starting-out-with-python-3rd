# Chapter.6
# 08. Random Number File Reader

def read():
    object_file = open('random_numbers.txt', 'r')
    total = 0
    count = 0
    for i in object_file: 
        i = i.rstrip('\n')
        i = int(i)
        print(i)
        total += i
        count += 1
    print(total)
    print(count)
    object_file.close()
read()
