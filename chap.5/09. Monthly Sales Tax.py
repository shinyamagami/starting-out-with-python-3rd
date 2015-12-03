# Chapter.5
# 09. Monthly Sales Tax

sales = float(input('Enter the total sales for this month: $'))

def calculate_taxes(sales):
    county_tax = sales * 0.05
    state_tax = sales * 0.025
    total_tax = county_tax + state_tax
    print('The amount of county sales tax is $', county_tax, sep='')
    print('The amount of state sales tax is $', state_tax, sep='')
    print('The amount of total sales tax is $', total_tax, sep='')
calculate_taxes(sales)
