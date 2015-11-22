# Chapter.3
# 6. Magic Dates

month = int(input('Please enter a month in numeric form: '))
day = int(input('Please enter a day in numeric form: '))
year = int(input('Please enter a two-digit year in numeric form: '))

if month * day == year:
    print('The date is magic!')
else:
    print('The date is not magic.')
