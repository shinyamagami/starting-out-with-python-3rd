# Chapter.5
# 01. Kilometer Converter

km = float(input('Enter a distance in kilometers: '))
def convert(km):
    miles = km * 0.6214
    print(format(miles, '.2f'), 'miles')
    
convert(km)
