# Chapter.4
# 14. Write a program that uses nested loops to draw this pattern

steps = 6
for r in range(steps):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')
