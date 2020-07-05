#   https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
mdy = input()
mdy = mdy.split()
mm = int(mdy[0])
dd = int(mdy[1])
yyyy = int(mdy[2])

cal = calendar.weekday(yyyy,mm,dd)
if cal == 0:
    print("MONDAY")
elif cal == 1:
    print("TUESDAY")
elif cal == 2:
    print("WEDNESDAY")
elif cal == 3:
    print("THURSDAY")
elif cal == 4:
    print("FRIDAY")
elif cal == 5:
    print("SATURDAY")
elif cal == 6:
    print("SUNDAY")
