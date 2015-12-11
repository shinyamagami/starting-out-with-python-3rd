# Chapter.8
# 03. Date Printer

def read():
    date = input('Enter a date in the form mm/dd/yyyy: ')
    mm = date[0:2]
    if mm == '01':
        month = 'January'
    elif mm == '02':
        month = 'February'
    elif mm == '03':
        month = 'March'
    elif mm == '04':
        month = 'April'
    elif mm == '05':
        month = 'May'
    elif mm == '06':
        month = 'June'
    elif mm == '07':
        month = 'July'
    elif mm == '08':
        month = 'August'
    elif mm == '09':
        month = 'September'
    elif mm == '10':
        month = 'October'
    elif mm == '11':
        month = 'November'
    elif mm == '12':
        month = 'December'
    print(month, date[3:5]+',', date[6:10])
read()
