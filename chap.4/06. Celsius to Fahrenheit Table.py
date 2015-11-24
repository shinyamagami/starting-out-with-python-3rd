# Chapter.4
# 06. Celsius to Fahrenheit Table

print('Celsius\t', 'Fahrenheit')
print('-' * 20)
for c in range(21):
    print(format(c, '2.0f'), '\t', format(9 / 5 * c + 32, '.2f'))
    
'''
fahrenheit = 9c/5 + 32
'''
