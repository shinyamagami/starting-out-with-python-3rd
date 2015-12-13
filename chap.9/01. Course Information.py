# Chapter.9
# 01. Course Information

def make_dictionaries():
    course_room = {}
    course_room['CS101'] = '3004'
    course_room['CS102'] = '4501'
    course_room['CS103'] = '6755'
    course_room['NT110'] = '1244'
    course_room['CM241'] = '1411'

    course_instructor = {}
    course_instructor['CS101'] = 'Haynes'
    course_instructor['CS102'] = 'Alvarado'
    course_instructor['CS103'] = 'Rich'
    course_instructor['NT110'] = 'Burke'
    course_instructor['CM241'] = 'Lee'

    course_time = {}
    course_time['CS101'] = '8:00 a.m.'
    course_time['CS102'] = '9:00 a.m.'
    course_time['CS103'] = '10:00 a.m.'
    course_time['NT110'] = '11:00 a.m.'
    course_time['CM241'] = '1:00 p.m.'

#    print(course_room)
#    print(course_instructor)
#    print(course_time)

    return course_room, course_instructor, course_time
def prompt(course_room, course_instructor, course_time):
    course_number = input('Enter a course_number: ')
    room = course_room[course_number]
    instructor = course_instructor[course_number]
    time = course_time[course_number]
    print(room, instructor, time, sep=' ')

def main ():
    course_room, course_instructor, course_time = make_dictionaries()
    prompt(course_room, course_instructor, course_time)
main()
