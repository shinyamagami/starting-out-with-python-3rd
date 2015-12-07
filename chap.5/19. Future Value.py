# Chapter.5
# 19. Future Value

present_value = float(input('Enter the amount of money in your account: $'))
monthly_interest_rate = float(input('Enter the monthly interest rate : '))
month = int(input('Enter the number of months thatt the money will be left in'
                  'the account: '))

def calculate(present_value, monthly_interest_rate, month):
    f = present_value * ((1 + monthly_interest_rate / 100) ** month)
    print('The account\'s future value is $', format(f, '.2f'), sep='')

calculate(present_value, monthly_interest_rate, month)
