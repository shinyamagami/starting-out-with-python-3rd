# Chapter.7
# 01. Total Sales

def calculate():
    sales = []
    total = 0
    for i in range(7):
        sale = input('Enter a store\'s sales for today: ')
        sales.append(sale)
        total += float(sale)
    print(sales)
    print(total)
calculate()
