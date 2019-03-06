import datetime
#import dateutil

current_date = datetime.date.today()
print (datetime.date.today())
print (current_date.__str__())

# returns naive datetime object
today = datetime.datetime.today()

# equivalent to datetime.today(), when no tzinfo object is passed
now = datetime.datetime.now()

# returns the UTC time
utcnow = datetime.datetime.utcnow()

print(today)
print(now)
print(utcnow)

# get current date
date_now = datetime.date.today()
# date_now = datetime.datetime.today().date()
print("Current date: ",date_now)

# get current time
time_now = datetime.datetime.today().time()
print("Current time: ",time_now)

# get the date object
today = datetime.datetime.today()

# now, format it as string, using the format codes:
print("Year:", today.strftime("%Y"))
print("Month:", today.strftime("%m"))
print("Day:", today.strftime("%d"))
print("Hour:", today.strftime("%H"))
print("Minutes:", today.strftime("%M"))
print("Seconds:", today.strftime("%s"))

print("*"*60)

a=today.strftime("%d")
a=int(a)
b=today.strftime("%m")
b=int(b)
print("{}.{}.{}".format(a, b, current_date.strftime("%Y")))

print("*"*60)

# datetime object for the '2018.03.24'
date1 = datetime.date(2018, 3, 24)
print(date1.strftime("%m.%d.%Y"))
date1 = datetime.datetime.strptime('2018.03.24','%Y.%m.%d')
print(date1.strftime("%m.%d.%Y"))

print("*"*60)

import time
from functools import reduce

start = time.time()

# do some time intensive stuff:
sum = reduce(lambda x,y:x+y, range(1,1_000_001))
print("The sum of numbers from 1 to 1_000_000 is: ", sum)

end = time.time()

print("the code ran for {:.6f}s".format(end - start))

print("*"*60)

now = datetime.datetime.now()
lunch = datetime.datetime.strptime('2019.03.06 12:00', "%Y.%m.%d %H:%M" )
print(lunch - now)         

print("*"*60)

# print weekday name of "2020/12/31"
userdate=datetime.datetime.strptime('2020/12/31', "%Y/%m/%d")
print(userdate.strftime("%A"))

print("*"*60)

def get_weekday_name(date, lang):
  named_wd = {
    'bg':["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"],
    'en':["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  }

  wd_name = named_wd[lang][date.weekday()]
  return wd_name

now = datetime.datetime.now()

print('Today is', get_weekday_name(now, "bg"))

print("*"*60)

import datetime

def get_next_sunday_date(bdate, period):
  """get_next_sunday_date

  Args:
      bdate (datetime): Object representing the date
      period (tuple): (start_year,end_year) interval to look into

  Returns:
      list: years, on which a date will be on Sunday
  """
  years = []

  for y in range(*period):
    bdate_weekday = datetime.date(y, bdate.month, bdate.day).weekday()

    if bdate_weekday == 6:
      years.append(y)

  return years


birth_date = datetime.datetime.strptime("25/07/00", "%d/%m/%y")

sundays_years = get_next_sunday_date(birth_date, (2018,2100))
print(sundays_years)

print("*"*60)

def butcher_easter(year):
    "Returns (Western) Easter as a date object."
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    return datetime.date(year, month, day)

def easter_dates_between(start, end):
    for year in range(start, end+1):
        print( butcher_easter(year).strftime("%d.%m.%Y") )


easter_dates_between(2018, 2050)

print("*"*60)


#Homework:
#
#Write a function, that calculates the remaining days from current date to your next birthday day.
#The output should be only the number of days.
# To calculate difference between two date objects, t1 and t2, you can use: t1-t2 which will return a timedelta Object
#
# Write a function, which returns True if a year is a leap year in the Gregorian calendar, and False if it's not.
# Algorithm: Leap_year#Algorithm @wikipedia
#





