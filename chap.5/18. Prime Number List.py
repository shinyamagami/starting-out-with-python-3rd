# Chapter.5
# 18. Prime Number List
# I could not understand what #17 and #18 asked me.
# So I made a program that display prime numbers between 1 to 100.

for n in range(2, 101):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    if prime == True:
        print(n)
        



                

