# Chapter.4
# 04. Distance Traveled

speed = float(input('What is the speed of the vehicle in mph? '))
hour = int(input('How many hours has it traveled? '))
distance = 0
print('Hour\t', 'Distance Traveled')
print('-' * 30)

for i in range(1, hour + 1):
    
    print(format(i, '1.0f'), '\t\t', format(i * speed, '6.1f'))
    distance += i * speed
