# Chapter.6
# 09. Exception Handling

def read():
    count = 0
    total = 0    
    try:
        object_file = open('numbers.txt', 'r')
    except IOError:
        print('IOError')
    except ValueError:
        print('ValueError')
    else:
        for i in object_file:
            total += int(i)
            count += 1
    print(total / count)
    object_file.close()
read()
