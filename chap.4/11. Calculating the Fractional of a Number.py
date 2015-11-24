# Chapter.4
# 11. Calculating the Factorial of a Number

n = int(input('Enter a nonnegative integer: '))
f = 1
for i in range(2, n + 1):
    f *= int(i)

print('The factorial of the number you gave is', f)
