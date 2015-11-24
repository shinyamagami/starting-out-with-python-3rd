# Chapter.4
# 12. Population

starting_number = int(input('Enter the starting number of organisms: '))
daily_increase = int(input('Enter the average daily population increase (as a percentage): '))
days = int(input('Enter the number of days to multiply: '))

print('Day Approximate\t', 'Population')
for i in range(1, days + 1):
    print(i, '\t', starting_number)
    starting_number += starting_number * daily_increase / 100
    
    
