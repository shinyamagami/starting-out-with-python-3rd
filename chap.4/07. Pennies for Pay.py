# Chapter.4
# 07. Pennies for Pay

days = int(input('Enter the number of days: '))
print('Day\t\t', 'Salary')
print('-' * 25)
total = 0
for i in range(1, days + 1):
    salary = 0.01 * 2 ** (i -1)
    print(format(i, '3.0f'), '\t\t$', format(salary, '8.2f'))
    total += salary
print('The total pay at the end of the period is $', total)
