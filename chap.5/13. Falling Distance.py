# Chapter.5
# 13. Falling Distance

def falling_distance(i):
    d = (1 / 2) * 9.8 * (i ** 2)
    print(format(d, '6.2f'), 'meters')
    return d

for i in range(1, 11):
    falling_distance(i)
