# Chapter.5
# 17. Prime Numbers

def is_prime():
    number = int(input('Enter a positive integer: '))
    if number > 2:
        if number % 2 == 0:
            return False
        else:
            return True
    elif number == 2:
        return True
    else:
        return False
print(is_prime())
