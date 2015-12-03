# Chapter.5
# 04. Automobile Costs

loan_payment = float(input('Enter a monthly loan payment: $'))
insurance = float(input('Enter a monthly insurance cost: $'))
gas = float(input('Enter a monthly gas cost: $'))
tires = float(input('Enter a monthly tires cost: $'))
maintenance = float(input('Enter a monthly maintenance cost: $'))

def sum_costs(loan_payment, insurance, gas, tires, maintenance):
    total = loan_payment + insurance + gas + tires + maintenance
    print(total)

sum_costs(loan_payment, insurance, gas, tires, maintenance)
