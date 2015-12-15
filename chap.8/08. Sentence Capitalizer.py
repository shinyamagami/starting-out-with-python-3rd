# Chapter.8
# 08. Sentence Capitalizer
# This was so difficult for me

sentence = input('Enter sentences with lower letters: ')

def convert(sentence):
    sentence_list = sentence.split(' ')
    new_sentence = ''
    for i in sentence_list:
        print(i)
        n = i[0].upper()
        new = i.replace(i[0], n)
        space = ' '
        new_sentence += new + space
    print(new_sentence)
    print(sentence_list)
    




convert(sentence)
