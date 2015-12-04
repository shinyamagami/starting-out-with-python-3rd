# Chapter.5
# 12. Maximum of Two Values

a = int(input('Enter a integer: '))
b = int(input('Enter another integer: '))
def max(a, b):
    if a > b:
        print(a, 'is bigger than', b)
    else:
        print(b, 'is bigger than', a)
max(a, b)
