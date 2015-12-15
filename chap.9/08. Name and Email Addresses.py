# Chapter.9
# 08. Name and Email Addresses

import pickle

def open_file():
    output_file = open('mailing_list.dat', 'wb')
    return output_file

def make_mailing_list():
    mailing_list = {}
    validation = 'y'
    while validation == 'y':
        name = input('Enter a name in small letter to add his or her email'
                     'address: ')
        email = input('Enter his or her email address: ')
        name = name.lower()
        email = email.lower()
        mailing_list[name] = email
        validation = input('Enter Y or y to continue: ')
        validation = validation.lower()
#    print(mailing_list)
    return mailing_list

def menu(mailing_list):
    validation = 'y'
    while validation == 'y':
        select_menu = input('What do you want to do? Enter "Look up", "Add",'
                            '"Change" or "Delete": '
                            'If nothing to do, enter "N" or "n": ')
        select_menu = select_menu.lower()
        if select_menu == 'look up':
            mailing_list = look_up(mailing_list)

        elif select_menu == 'add':
            mailing_list = add(mailing_list)

        elif select_menu == 'change':
            mailing_list = change(mailing_list)

        elif select_menu == 'delete':
            mailing_list = delete(mailing_list)

        elif select_menu == 'n':
            print('See you!')
            validation = 'n'
            
def look_up(mailing_list):
    name = input('Enter a name to look up his or her email address: ')
    name = name.lower()
    print(mailing_list[name])
    return mailing_list
def add(mailing_list):
    name = input('Enter a name to add his or her email address: ')
    email = input('Enter his or her email address: ')
    name = name.lower()
    email = email.lower()
    mailing_list[name] = email    
    return mailing_list

def change(mailing_list):
    name = input('Enter a name to change his or her email address: ')
    name = name.lower()
    print(mailing_list[name])
    validation = input('Enter "y" to change this address: ')
    validation = validation.lower()
    if validation == 'y':
        email = input('Enter his or her email address: ')
        email = email.lower()
        mailing_list[name] = email    
    return mailing_list

def delete(mailing_list):
    name = input('Enter a name to delete his or her email address: ')
    name = name.lower()
    print(mailing_list[name])
    validation = input('Enter "y" to delete this address: ')
    validation = validation.lower()
    if validation == 'y':
        del mailing_list[name]
    return mailing_list

output_file = open_file()
mailing_list = make_mailing_list()
menu(mailing_list)
pickle.dump(mailing_list, output_file)
output_file.close()

