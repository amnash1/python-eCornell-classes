"""
Functions for working with datetime objects.

Author: Andy Nash
Date:   2022-12-30
"""
import datetime


def christmas_day(year):
    """
    Returns ISO day of the week for Christmas in the given year.

    The ISO day is an integer between 1 and 7.  It is 1 for Monday, 7 for Sunday
    and the appropriate number for any day in-between.

    Parameter year: The year to check for Christmas
    Precondition: years is an int > 0 (and a year using the Gregorian calendar)
    """
    # HINT: Make a date object and use the isoweekday method
    #datetime.date(2022,12,25)
    #covert to string str(d)
    t = datetime.date(year,12,25)
    dow = t.isoweekday()
    return dow


def iso_str(d,t):
    """
    Returns the ISO formatted string of date and time together.

    When combining, the time must be accurate to the microsecond.

    Parameter d: The month-day-year
    Precondition: d is a date object

    Parameter t: The time of day
    Precondition: t is a time object
    """
    # HINT: Combine date and time into a datetime and use isoformat
    #You will need to combine d and t into a single datetime object.
    #datetime.datetime(2019,9,25,13,45)
    #t.hour, t.minute, t.second
    daytime = datetime.datetime(d.year, d.month, d.day, t.hour, t.minute,t.second, t.microsecond )

    # You will also need to use the method isoformat.
    form = daytime.isoformat()
    #convert to string
    return form

#christmas_day(2022)
#d = datetime.date(2019,10,12)
#funcs.iso_str(d,datetime.time(12,35,15,205))
