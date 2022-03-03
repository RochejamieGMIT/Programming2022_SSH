# Author: Jamie Roche
#Week 5 task
# Using this link to find how to import day of the week
#https://www.delftstack.com/howto/python/python-datetime-day-of-week/
#

from datetime import datetime

Day = datetime.today().weekday()
#Day = 0-6 to test

days = ("Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday"
)

today = days[Day]

if Day >= 5:
    print ("Today is ", today, "it is the weekend, yay!")
else :
    print ("Today is ", today, "Yes, It is a weekday")

