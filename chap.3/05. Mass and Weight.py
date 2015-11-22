# Chapter.3
# 5. Mass and Weight

mass = float(input('Please enter an object\'s mass: '))

weight = mass * 9.8

if weight > 500:
    print('It is too heavy.')
elif weight < 100:
    print('It is too light.')
else:
    print(weight, 'N', sep='')
