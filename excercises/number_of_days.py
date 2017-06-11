terminate = False

print ('This program will display calendar month between 1800 and 2099')

while not terminate:
    month = int(input('Enter month 1-12 (-1 to quit): '))

    if month == -1:
        terminate = True

    else:
        while month <1 or month >12:
            month = int(input('Invalid input - enter month 1-12'))

        year = int(input('Enter year (yyyy)'))

        while year <1800 or year >2099:
            year = int(input('Invalid - Enter year (1800 - 2099)'))

        if (year % 4 ==0) and (not (year%100 == 0) or (year %400 ==0)):
             leap_year = True
        else:
             leap_year = False

        if month in (1,3,5,7,8,10, 12):
              num_days_in_month = 31
        elif month in (4,6,9,11):
             num_days_in_month = 30
        elif leap_year:
            num_days_in_month = 29
        else:
            num_days_in_month = 28

        print '\n', month, ',', year, 'has', num_days_in_month, 'days'

        if leap_year:
            print year, 'is a leap year\n'
        else:
            print (year, 'is a not leap year\n')
    
                
