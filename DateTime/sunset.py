"""
Functions for parsing time values from text.

While these functions are similar to functions found in the assignment, they
are missing timezone information.  The next exercise will modify these
functions to make them compatible with the assignment.

Author: Andy Nash
Date:   2022-12-31
"""

from dateutil.parser import parse
#contains a single function called parse
from datetime import datetime
from datetime import date
import introcs
#import datetime



def str_to_time(timestamp):
    """
    Returns the datetime object for the given timestamp (or None if the stamp is invalid)

    This function should just use the parse function in dateutil.parser to convert the
    timestamp to a datetime object.  If it is not a valid date (so the parser crashes),
    this function should return None.

    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    """
    # Hint: Use a try-except to return None if parsing fails

    """
    d.strftime('%Y-%m-%d')
    d.strftime('%m/%d/%y')
    d.strftime('%H:%M:%S')

    iso8601
    d.isoformat() takes no arugments
    """

    try:
        #call parser
        return parse(timestamp)

    #return None if parsing fails
    except:
        return None


def sunset(date,daycycle):
    """
    Returns the sunset datetime (day and time) for the given date

    This function looks up the sunset from the given daycycle dictionary. If the
    daycycle dictionary is missing the necessary information, this function
    returns the value None.

    A daycycle dictionary has keys for several years (as int).  The value for each year
    is also a dictionary, taking strings of the form 'mm-dd'.  The value for that key
    is a THIRD dictionary, with two keys "sunrise" and "sunset".  The value for each of
    those two keys is a string in 24-hour time format.

    For example, here is what part of a daycycle dictionary might look like:

        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }

    Parameter date: The date to check
    Precondition: date is a date object

    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: ISO FORMAT IS 'yyyy-mm-ddThh:mm'.  Find the sunset value by constructing a
    # string in ISO format and calling str_to_time.
    #convert to an iso format
    converted_date = str_to_time(datetime.combine(date,datetime.min.time()).isoformat() )
    #print (converted_date)  #2017-08-02 00:00:00

    #eliminate the location data, find the year to start, need to jump down 5 rows
    #make new json without location data
    for year, mo_day_sun in daycycle.items():
        #print(year)
        lst = list(daycycle.items())
        record_days = dict(lst[5:])
        #timezone = daycycle['timezone']
        #print(timezone)
        #make a queriable date from daycycle json

        for year, mo_day_sun in record_days.items():
            #print (year, mo_day_sun)
            #now down to just year, day, sunrise, sunset in new dictionary
            #need to convert to iso formate to match input (date)
            #if statement to match input to json
            if int(year) == converted_date.year:
                #print(int(year))
                for month_day in mo_day_sun:
                    #print(month_day)
                    if month_day == converted_date.strftime("%m-%d"):
                        #sunrise = datetime(int(year), int(converted_date.month),int(converted_date.day), int(mo_day_sun[month_day]["sunrise"][:2]), int(mo_day_sun[month_day]["sunrise"][3:]))
                        sunset = datetime(int(year), int(converted_date.month),int(converted_date.day), int(mo_day_sun[month_day]["sunset"][:2]), int(mo_day_sun[month_day]["sunset"][3:]))
                        #print(sunrise, sunset)
                        return sunset
