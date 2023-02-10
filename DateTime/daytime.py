"""
Functions for parsing time values and determining daylight hours.

Both of these functions will be used in the main project.  You should hold on to them.

Author: Andy Nash
Date:   2023-01-02
"""

import datetime
import pytz
from dateutil.parser import parse
#contains a single function called parse




def str_to_time(timestamp,tzsource=None):
    """
    Returns the datetime object for the given timestamp (or None if timestamp is
    invalid).

    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.

    If the timestamp has a time zone, then it should keep that time zone even if
    the value for tzsource is not None.  Otherwise, if timestamp has no time zone
    and tzsource is not None, then this function will use tzsource to assign
    a time zone to the new datetime object.

    The value for tzsource can be None, a string, or a datetime object.  If it
    is a string, it will be the name of a time zone, and it should localize the
    timestamp.  If it is another datetime, then the datetime object created from
    timestamp should get the same time zone as tzsource.

    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string

    Parameter tzsource: The time zone to use (OPTIONAL)
    Precondition: tzsource is either None, a string naming a valid time zone,
    or a datetime object.
    """
    """
    # HINT: Use the code from the previous exercise and add time zone handling.
    # Use localize if tzsource is a string; otherwise replace the time zone if not None
    # g = cert.replace(tzinfo=event.tzinfo)
    
    try:
        parse(timestamp)
    except:
        return None



    time = parse(timestamp)
    #print(time)
    #If the timestamp has a time zone, then it should keep that time zone even if
    #the value for tzsource is not None.
    if time.tzinfo is not None:
        #print('1')
        new_tz = time.replace(tzinfo=time.tzinfo)
        return datetime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.second, tzinfo=new_tz.tzinfo)

    #The value for tzsource can be None
    if tzsource is None:
        #print ('2')
        return datetime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.second, tzinfo=tzsource)

    #Otherwise, if timestamp has no time zone and tzsource is not None
    if time.tzinfo is None and tzsource is not None:
        #print('3')
        #then this function will use tzsource to assign
        #a time zone to the new datetime object.
        #if it is a string,
        if type(tzsource) == str:
            #print ('4')
            #it will be the name of a time zone, and it should localize thetimestamp.
            #Use localize if tzsource is a string
            timezone_name = pytz.timezone(tzsource).localize(time)
            return datetime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.second, tzinfo=timezone_name.tzinfo)

        #If it is another datetime,
        else:
            #print ('5')
            #then the datetime object created from
            #timestamp should get the same time zone as tzsource.
            g = tzsource.tzinfo
            #print(g)
            return datetime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.second,  tzinfo= g)
            #expected datetime.datetime(2016, 5, 12, 16, 23, tzinfo=tzoffset(None, -14400)
            #TypeError: tzinfo argument must be None or of a tzinfo subclass, not type 'datetime.datetime'
    """
    
    
    #Bruce's method (try fails in codio)
    
    result = None
    try:
        d = parse(timestamp)
        if tz == None:
            result = parse(timestamp)
        if tz != None and d.tzinfo != None and type(tz) != str:
            result = parse(timestamp)
        elif tz != None and d.tzinfo == None and type(tz) != str:
            result = d.replace(tzinfo=tz)
        elif type(tz) == str:
            result = timezone(tz).localize(d)
        return result
    except:
        return None
    


def daytime(time,daycycle):
    """
    Returns True if the time takes place during the day, False otherwise (and
    returns None if a key does not exist in the dictionary).

    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dictionary.

    A daycycle dictionary has keys for several years (as strings).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.

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
    
    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects using data from the daycycle dictionary.  Also, if the time
    parameter does not have a timezone, we assume that it is in the same timezone
    as the daycycle dictionary.

    Parameter time: The time to check
    Precondition: time is a datetime object

    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    """
    # HINT: Use the code from the previous exercise to get sunset AND sunrise
    # Add a timezone to time if one is missing (the one from the daycycle)

    
    
    from datetime import datetime
    from datetime import date

    converted_date = str_to_time(datetime.combine(time,datetime.min.time()).isoformat() )

    #eliminate the location data, find the year to start, need to jump down 5 rows
    #make new json without location data
    for year, mo_day_sun in daycycle.items():
        lst = list(daycycle.items())
        record_days = dict(lst[5:])

        #make a queriable date from daycycle json
        for year, mo_day_sun in record_days.items():
            #print (year, mo_day_sun)
            #now down to just year, day, sunrise, sunset in new dictionary
            #need to convert to iso formate to match input (date)
            #if statement to match input to json
            if int(year) == converted_date.year:

                for month_day in mo_day_sun:

                    if month_day == converted_date.strftime("%m-%d"):

                        tz = pytz.timezone(daycycle['timezone'])
                        #<DstTzInfo 'America/New_York' LMT-1 day, 19:04:00 STD
                        sunrise = datetime(int(year), int(converted_date.month),int(converted_date.day), int(mo_day_sun[month_day]["sunrise"][:2]), int(mo_day_sun[month_day]["sunrise"][3:]))
                        sunrise_with_tz = sunrise.replace(tzinfo=tz)
                        sunrise_with_tz = str(tz.localize(sunrise))


                        sunset = datetime(int(year), int(converted_date.month),int(converted_date.day), int(mo_day_sun[month_day]["sunset"][:2]), int(mo_day_sun[month_day]["sunset"][3:]))
                        sunset_with_tz = sunset.replace(tzinfo=tz)
                        sunset_with_tz = str(tz.localize(sunset))


    print ('sunrise is ' +str(sunrise_with_tz))
    print ('sunset is ' +str(sunset_with_tz))
    print ('time given is ' +str(time))
    return sunrise_with_tz < str(time) < sunset_with_tz
    

    
    #this works too

    year = str(time.year)

    day  = None
    json = daycycle[year]
    mo_day  = '%02d-%02d' % (time.month,time.day)

    day = json[mo_day]
    sun_tz  = daycycle['timezone']
    sunrise = str_to_time(year+'-'+mo_day+'T'+day['sunrise'],sun_tz)
    sunsets = str_to_time(year+'-'+mo_day+'T'+day['sunset'],sun_tz)

    if time.tzinfo is None:
        time = pytz.timezone(sun_tz).localize(time)

    return sunrise < time < sunsets
    
   




    """
    #Bruce's Method



    try:    
        m_d_str = str(time)[5:7] + "-" + str(time)[8:10]
        y_str = str(time.year)
        y_m_d_str = y_str + "-" + m_d_str + "T"
        tz_str = daycycle['timezone']
        sunset = str_to_time(y_m_d_str + daycycle[y_str][m_d_str]['sunset'], tz_str)
        sunrise = str_to_time(y_m_d_str + daycycle[y_str][m_d_str]['sunrise'], tz_str)

        if time.tzinfo == None:
            time_tz = timezone(tz_str).localize(time)
        else:
            time_tz = time

        return time_tz > sunrise and time_tz < sunset
    except:
        return None