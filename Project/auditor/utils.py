"""
Module providing utility functions for this project.

These functions are general purpose utilities used by other modules in this project.
Some of these functions were exercises in early course modules and should be copied
over into this file.

The preconditions for many of these functions are quite messy.  While this makes writing 
the functions simpler (because the preconditions ensure we have less to worry about), 
enforcing these preconditions can be quite hard. That is why it is not necessary to 
enforce any of the preconditions in this module.

Author: Andy Nash
Date: 2023-01-04
"""
import csv
import json
import datetime
import pytz
from dateutil.parser import parse

def read_csv(filename):
    """
    Returns the contents read from the CSV file filename.
    
    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the 
    programmer to interpret this data, since CSV files contain no type information.
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid CSV file
    """
    #combine with accum pattern to create a new table
    result = []

    #make each row a list
    #open file
    file = open(filename)
    #wrapper creates a new object
    wrapper = csv.reader(file)
    #use wrapper in a for loop
    for row in wrapper:
        #print(row)
        #put full row in a list
        result.append(row)

    file.close()
    #print(result)
    return result                  


def write_csv(data,filename):
    """
    Writes the given data out as a CSV file filename.
    
    To be a proper CSV file, data must be a 2-dimensional list with the first row 
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.
    
    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a  2-dimensional list of strings
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """
    #Pay attention to the precondition, particularly the restriction that only
    #nested lists may be written to the file.

    #open file from filepath
    file = open(filename,'w')
    #create a second object
    wrapper = csv.writer(file)
    #for loop to
    for row in data:
        #print(row)
        wrapper.writerow(row)
        #print(wrapper.writerow(row))

    file.close()


def read_json(filename):
    """
    Returns the contents read from the JSON file filename.
    
    This function reads the contents of the file filename, and will use the json module
    to covert these contents in to a Python data value.  This value will either be a
    a dictionary or a list. 
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid JSON file
    """
        #open file
    file = open(filename)
    #read all the text
    text = file.read()
    #now convert to dictionary using json.loads
    data = json.loads(text)
    #can do somethign like data['height']
    #print(data)
    file.close()

    return data


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
    # HINT: Use the code from the previous exercise and add time zone handling.
    # Use localize if tzsource is a string; otherwise replace the time zone if not None
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



def daytime(time,daycycle):
    """
    Returns true if the time takes place during the day.
    
    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dicitionary.
    
    A daycycle dictionary has keys for several years (as int).  The value for
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
    datetime objects from this set.  If the time parameter does not have a timezone,
    we assume that it is in the same timezone as the daycycle dictionary
    
    Parameter time: The time to check
    Precondition: time is a datetime object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
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


def get_for_id(id,table):
    """
    Returns (a copy of) a row of the table with the given id.
    
    Table is a two-dimensional list where the first element of each row is an identifier
    (string).  This function searches table for the row with the matching identifier and
    returns a COPY of that row. If there is no match, this function returns None.
    
    This function is useful for extract rows from a table of pilots, a table of instructors,
    or even a table of planes.
    
    Parameter id: The id of the student or instructor
    Precondition: id is a string
    
    Parameter table: The 2-dimensional table of data
    Precondition: table is a non-empty 2-dimension list of strings
    """
    if id != None:
        for row in range(len(table)):
            if table[row][0] == id: 
                return table[row]
    else: 
        return None

