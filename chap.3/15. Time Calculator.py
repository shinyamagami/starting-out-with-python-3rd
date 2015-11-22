# Chapter.3
# 15. Time Calculator

seconds = int(input('Please enter the number of seconds: '))

if 86400 <= seconds:
    print(86400 // 86400, 'day')
elif seconds >= 3600 and seconds < 86400:
    print(seconds // 3600, 'hour')
else:
    print(seconds // 60, 'minute')
