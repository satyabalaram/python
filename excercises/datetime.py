import time
import datetime

print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))
print("Current time:", datetime.datetime.now().time())


def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False
print(leap_year(1900))
print(leap_year(2004))

#substract 5 days from current date

from datetime import date, timedelta

dt = date.today() - timedelta(5)
today = date.today()
yesterday = date.today() - timedelta(days = 1)
tomorrow = date.today() + timedelta(days = 1)

print 'current date:', date.today()
print '5 days before current date', dt
print 'today:', today
print 'yesterday:', yesterday
print 'tomorrow:', tomorrow

#unix timestamp to readbale date
print (datetime.datetime.fromtimestamp(int("1284105682")).strftime('%Y-%m-%d %H:%M:%S'))
