# Chapter.4
# 01. Bug Collector

days = 1
total = 0
while days < 6:
    bugs = int(input('Please enter the number of bugs you got today: '))
    total += bugs
    days += 1
print(total)
