# Chapter.3
# 2. Areas of Rectangles

length_a = float(input('Please input the length of rectangle a: '))
width_a = float(input('Please input the width of rectangle a: '))
length_b = float(input('Please input the length of rectangle b: '))
width_b = float(input('Please input the width of rectangle b: '))
area_of_a = length_a * width_a
area_of_b = length_b * width_b

if area_of_a > area_of_b:
    print('Rectangle a has the greater area.')
elif area_of_b > area_of_a:
    print('Rectangle b has the greater area.')
else:
    print('Rectangle a and b has the same area.')
