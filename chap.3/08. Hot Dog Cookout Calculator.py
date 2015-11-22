# Chapter.3
# 8. Hot Dog Cookout Calculator

people = int(input('Please enter the number of people attending the cookout: '))
hotdogs = int(input('Please enter the number of hot dogs each person will be given: '))

if people * hotdogs % 8 == 0 and people * hotdogs % 10 == 0:
    print(people * hotdogs // 8, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is 0')
    print('The number of hot dogs that will be left over is 0')
elif people * hotdogs % 8 == 0 and people * hotdogs % 10 != 0:
    print(people * hotdogs // 8, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10 + 1, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is', people * hotdogs % 8)
    print('The number of hot dogs that will be left over is', 
         (people * hotdogs // 10 + 1) * 10 - people * hotdogs)  
elif people * hotdogs % 8 != 0 and people * hotdogs % 10 == 0:
    print(people * hotdogs // 8 + 1, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is',
         (people * hotdogs // 8 + 1) * 8 - people * hotdogs)
    print('The number of hot dogs that will be left over is', people * hotdogs % 10)
else:
    print(people * hotdogs // 8 + 1, 'of packages of hot dog buns required.')
    print(people * hotdogs // 10 + 1, 'of packages of hot dogs required.')
    print('The number of hot dog buns that will be left over is',
         (people * hotdogs // 8 + 1) * 8 - people * hotdogs)
    print('The number of hot dogs that will be left over is',
         (people * hotdogs // 10 + 1) * 10 - people * hotdogs) 
