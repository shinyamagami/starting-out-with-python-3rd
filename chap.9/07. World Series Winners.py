# Chapter.9
# 07. World Series Winners

file = "WorldSeries.txt"

def description():
    # display description
    print('This program makes two dictionaries from a text file, prompt a user'
          'to enter a year and display a team won World Series in the year and'
          'the time to win World Series.\n')
'''
def get_file():
    return input('Enter the file name with its extension: ')
'''
def open_file():
    # open a file in a read mode
    return open(file, 'r')
def make_dict(file_object):
    # make two dictionaries which has years as keys and teams as values and
    # teams as keys and times as values
    champ_dict = {}
    line = file_object.readline().rstrip('\n')
#    while line != '':
#        line = file_object.readline().rstrip('\n')
#        print(line)
    for i in range(1903, 2010):
        champ_dict[i] = line
        line = file_object.readline().rstrip('\n')
    print(champ_dict, '\n')
    numb_dict = {}
    for i in range(1903, 2010):
        team = champ_dict[i]
        if not team in numb_dict:
            numb_dict[team] = 1
        else:
            numb_dict[team] += 1
    print(numb_dict, '\n')
    return champ_dict, numb_dict

def get_prompt(champ_dict, numb_dict):
    # get a year from a user
    valid = True
    while valid:
        try:
            year = int(input('Enter a year in the range from 1903 to 2009 to '
                             'know which team won World Series in the year: '))
            if year > 1902 and year < 2010 and year != 1904 and year != 1994:
                print(champ_dict[year], 'won in the year!',numb_dict[champ_dict[year]], 'times')
                valid = False
            elif year == 1904:
                print('World Series Not Played in 1904')
                valid = False
            elif year == 1994:
                print('World Series Not Played in 1994')
                valid = False
        except:
            print('Enter a year in integer.')
    
def main():
    description() # display description
#    file = get_file()
    file_object = open_file() # open a file in a read mode
    champ_dict, numb_dict = make_dict(file_object)
    # make two dictionaries which has years as keys and teams as values and
    # teams as keys and times as values
    get_prompt(champ_dict, numb_dict) # get a year from a user

main()
