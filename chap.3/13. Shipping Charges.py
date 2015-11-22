# Chapter.3
# 13. Shipping Charges

weight = int(input('Please enter the weight of a package you leave in pound: '))

if weight > 10:
    print('The shipping charge is $4.75')
elif weight <= 10 and weight > 6:
    print('The shipping charge is $4.00')
elif weight <= 6 and weight > 2:
    print('The shipping charge is $3.00')
else:
    print('The shipping charge is $1.50')
