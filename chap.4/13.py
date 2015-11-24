# Chapter.4
# 13. Write a program that uses nested loops to draw this pattern

base_size = 8
for r in range(base_size, 1, -1):
    for c in range(r - 1):
        print('*', end='')
    print()
'''
for i in range(7, 0, -1):
    print('*' * i)
'''
