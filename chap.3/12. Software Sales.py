# Chapter.3
# 12. Software Sales

number = int(input('Please enter the number of packages you purchased: '))

if number >= 100:
    print('The amount of discount is 40% and the total amount of the purchase'
          'after the discount is $', 99 * number * 0.6, sep='')
elif number >= 50 and number <= 99:
    print('The amount of discount is 30% and the total amount of the purchase'
          'after the discount is $', 99 * number * 0.7, sep='')
elif number >= 20 and number <= 49:
    print('The amount of discount is 20% and the total amount of the purchase'
          'after the discount is $', 99 * number * 0.8, sep='')
elif number >= 10 and number <= 19:
    print('The amount of discount is 10% and the total amount of the purchase'
          'after the discount is $', 99 * number * 0.9, sep='')
else:
    print('The amount of discount is 0% and the total amount of the purchase'
          'after the discount is $', 99 * number, sep='')
