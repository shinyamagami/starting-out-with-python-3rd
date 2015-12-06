# Chapter.5
# 17. Prime Numbers

# get a number from a user and return it as a variable 'x'
def get_input():
    return int(input('Please enter a positive integer: '))

# check if the number is a prime number or not
def is_prime(x):
    # When x <= 1, it shows 'False.'
    if x <= 1:
        return False
    else:
        # When x = 2, it shows 'True.' 
        i = 2
        while x > i:
            # If x % == 0, it shows 'False', otherwise i = i + 1 while x > i.
            if x % i == 0:
                return False
            else:
                i = i + 1
        else:
            return True

def print_value(boolean):
    print(boolean)

def main():
               
    x = get_input()

    boolean = is_prime(x)

    print_value(boolean)

main()
