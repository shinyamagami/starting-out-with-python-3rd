# Chapter.9
# 06. File Analysis

def read():
    text_1 = input('Enter a file name with its extension: ')
    text_2 = input('Enterh another file name with its extension: ')
    object_file_1 = open(text_1, 'r')
    object_file_2 = open(text_2, 'r')
    for line in object_file_1:
        words_1 = line.split()
    for line in object_file_2:
        words_2 = line.split()
    words_list = words_1 + words_2
    print(words_list)
    words_set = set()
    for word in words_list:
        if word not in words_set:
            words_set.add(word)
    print(words_set)

    words_1_set = set()
    for word in words_1:
        if word not in words_1_set:
            words_1_set.add(word)
    words_2_set = set()
    for word in words_2:
        if word not in words_2_set:
            words_2_set.add(word)
    intersection_sets = words_1_set & words_2_set
    print('A list of the words that appear in both files:', intersection_sets)
    print('A list of the words that appear in the first file but not the'
          'second:', words_1_set - words_2_set)
    print('A list of the words that appear in the second file but not the'
          'first file:', words_2_set - words_1_set)
    print('A list of the words that appear in either the first or second file'
          'but not both:', words_1_set ^ words_2_set)
read()
