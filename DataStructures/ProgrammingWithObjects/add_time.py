"""
Module demonstrating how to write functions with objects.

This module contains two versions of the same function.  One version returns a new
value, while other modifies one of the arguments to contain the new value.

Author: Andy Nash
Date: 2022-12-09
"""
import clock


def add_time1(time1, time2):
    """
    Returns the sum of time1 and time2 as a new Time object

    DO NOT ALTER time1 or time2, even though they are mutable

    Examples:
        The sum of 12hr 13min and 13hr 12min is 25hr 25min
        The sum of 1hr 59min and 3hr 2min is 5hr 1min

    Parameter time1: the starting time
    Precondition: time1 is a Time object

    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    assert type(time1) == clock.Time
    assert type(time2) == clock.Time
    hours = 0
    minutes = 0

    if time1.minutes +time2.minutes > 59:
        #print (time1.minutes +time2.minutes)
        hours = time1.hours + time2.hours +1
        minutes = (time1.minutes +time2.minutes) -60
        result = clock.Time(hours, minutes)
        #print (hours)
        #print (minutes)

    else:
        hours = time1.hours + time2.hours
        minutes = time1.minutes +time2.minutes
        result = clock.Time(hours, minutes)

    return result


def add_time2(time1, time2):
    """
    Modifies time1 to be the sum of time1 and time2

    DO NOT RETURN a new time object.  Modify the object time1 instead.

    Examples:
        The sum of 12hr 13min and 13hr 12min is 25hr 25min
        The sum of 1hr 59min and 3hr 2min is 5hr 1min

    Parameter time1: the starting time
    Precondition: time1 is a Time object

    Parameter time2: the time to add
    Precondition: time2 is a Time object

    Note that this function is a procedure that modifies one (and only one) of
    the arguments. It should not contain a constructor call and should not
    return anything.
    """
    #assert type(time1) == clock.Time
    #assert type(time2) == clock.Time

    #hours = 0
    #minutes = 0

    if time1.minutes + time2.minutes > 59:
        time1.hours = time1.hours + time2.hours + 1
        time1.minutes = (time1.minutes +time2.minutes) -60


    else:
        time1.hours = time1.hours + time2.hours
        time1.minutes = time1.minutes + time2.minutes



#time1 = clock.Time(12,13)
#time2 = clock.Time(12,12)

#add_time1 (time1, time2)
#add_time2 (time1,time2)
