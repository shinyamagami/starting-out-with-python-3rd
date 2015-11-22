# Chapter.3
# 14. Body Mass Index

weight = float(input('Please enter your weight in pounds: '))
height = float(input('Please enter your height in inches: '))

BMI = weight * 703 / (height ** 2)

if BMI < 18.5:
    print('Your body mass index (BMI) is', format(BMI, '.2f'), 'Your weight is underweight')
elif BMI > 25:
    print('Your body mass index (BMI) is', format(BMI, '.2f'), 'Your weight is overweight')
else:
    print('Your body mass index (BMI) is', format(BMI, '.2f'), 'Your weight is optimal.')
