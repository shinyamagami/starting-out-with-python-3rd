# Chapter.4
# 03. Budget Analysis

budget = float(input('Please input the amount of your budget: $'))
total = 0
another = 'y'
while another == 'y' or another == 'Y':
    expense = float(input('Please input the amount of your expense: $'))
    total += float(expense)
    another = input('Do you want to enter another amount? Enter y or Y for yes:')
print(budget - total)
