# Chapter.3
# 11. Book Club Points

book = int(input('Please enter the number of books you purchased this month: '))

if book >= 8:
    print('You earned 60 points.')
elif book < 8 and book >= 6:
    print('You earned 30 points.')
elif book < 6 and book >= 4:
    print('You earned 15 points.')
elif book < 4 and book >= 2:
    print('You earned 5 points.')
elif book < 2 and book >= 0:
    print('You earned 0 points.')
