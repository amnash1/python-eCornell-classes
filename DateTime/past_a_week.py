"""
A simple function computing time elapsed

Author: Andy Nash
Date:   2022-12-30
"""
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta

def past_a_week(d1,d2):
    """
    Returns True if event d2 happens at least a week (7 days) after d1.

    If d1 is after d2, or d2 is less than a week after d1, this function returns False.
    Values d1 and d2 can EITHER be date objects or datetime objects.  If a date object,
    assume that it happens at midnight of that day.

    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object

    Parameter d2: The second event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison

    #t = datetime.timedelta(days = 7)

    if type(d1) == type(d2):
        #print('same type')
        return (d2 - d1) >= timedelta(days = 7)

    #if not the same type
    elif type(d1) != type(d2):
        #check if d1 is a date, change to datetime
        #print('not same type')
        #print(type(d2))

        if type(d1) == date:
            #print('see this')
            convert_d1 = datetime.combine(d1,datetime.min.time())
            #print('d1 was converted')
            #print(convert_d1)
                #then compare to d2
            return (d2 - convert_d1) >= timedelta(days = 7)

        if type(d2) == date:
            convert_d2 = datetime.combine(d2,datetime.min.time())
            #print('d2 was converted')
            #print(convert_d2)
            return (d1 - convert_d2) >= timedelta(days = 7)




"""


d1 = date(2019,10,12)
d2 = date(2019,10,25)
d3 = date(2019,10,19)
d4 = datetime(2019,10,12,9,45,15)
d5 = datetime(2019,10,19,10,15)
d6 = datetime(2019,10,19,8,30)

past_a_week(d1,d3)
"""
