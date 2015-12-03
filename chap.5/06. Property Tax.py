# Chapter.5
# 06. Calories from Fat and Carbohydrates

fat_grams = float(input('Enter the number of fat grams: '))
carb_grams = float(input('Enter the number of carbohydrate grams: '))

def calculate(fat_grams, carb_grams):
    print('The calories from fat is', format(fat_grams * 9, '.2f'), 'calories')
    print('The calories from carbohydrate is', format(carb_grams * 4, '.2f'), 'calories')

calculate(fat_grams, carb_grams)
