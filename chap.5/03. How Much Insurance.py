# Chapter.5
# 03. How Much Insureance?

cost = float(input('Enter the replacement cost of a building: $'))
def calculate(cost):
    insurance = cost * 0.8
    print('The minimum amount of insurance you should buy for the property is $', format(insurance, '.2f'))

calculate(cost)
