# Chapter.9
# 05. Word Frequency

def read():
    file = input('Enter a file name with its extension: ')    
    object_file = open(file, 'r')
    return object_file

def count(object_file):
    word_frequency = {}
    count = 1
    for line in object_file:
        words = line.split()
        for word in words:
            word = word.lower()
            if word not in word_frequency:
                word_frequency[word] = count
            else:
                word_frequency[word] = count + 1

    print(word_frequency)
object_file = read()
count(object_file)
