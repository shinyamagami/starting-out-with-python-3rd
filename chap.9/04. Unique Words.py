# Chapter.9
# 04. Unique Words

def read():
    file = input('Enter a file name with its extension: ')
    object_file = open(file, 'r')
    unique_words = set()
    for i in object_file:
        i = i.rstrip('\n')
        if i not in unique_words:
            unique_words.add(i)
    print(unique_words)

read()
