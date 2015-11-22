# Chapter.3
# 10. Money Counting Game

penny = int(input('Please enter the number of pennies you have: ')) * 1
nickel = int(input('Please enter the number of nickels you have: ')) * 5
dime = int(input('Please enter the number of dimes you have: ')) * 10
quarter = int(input('Please enter the number of quarters you have: ')) * 25



if penny + nickel + dime + quarter > 100:
    print('The sum of coins you entered is', penny + nickel + dime + quarter - 100
          , 'cent over than $1.')
elif penny + nickel + dime + quarter < 100:
    print('The sum of coins you entered is', 100 - penny + nickel + dime + quarter
          , 'cent less than $1.')    
else:
    print('Congratulations! You won!')
    
