"""
Module to check violations for a flight lesson.

This module processes the primary violations, which are violations of weather restrictions. 
Weather restrictions express the minimum conditions that a pilot is allowed to fly in.  
So if a pilot has a ceiling minimum of 2000 feet, and there is cloud cover at 1500 feet, 
the pilot should not fly.To understand weather minimums, you have to integrate three 
different files: daycycle.json (for sunrise and sunset), weather.json (for hourly weather 
observations at the airport), and minimums.csv (for the schools minimums set by agreement 
with the insurance agency). You should look at those files BRIEFLY to familiarize yourself 
with them.

This module can get overwhelming if you panic and think too much about the big picture.  
Like a good software developer, you should focus on the specifications and do a little
at a time.  While these functions may seem like they require a lot of FAA knowledge, all
of the information you need is in the specifications. They are complex specifications,
but all of the information you need is there.  Combined with the provided unit tests
in tests.py, this assignment is very doable.

It may seem weird that these functions only check weather conditions at the time of 
takeoff and not the entire time the flight is in the air.  This is standard procedure 
for this insurance company.  The school is only liable if they let a pilot take off in 
the wrong conditions.  If the pilot stays up in adverse conditions, responsibility shifts 
to the pilot.

The preconditions for many of these functions are quite messy.  While this makes writing 
the functions simpler (because the preconditions ensure we have less to worry about), 
enforcing these preconditions can be quite hard. That is why it is not necessary to 
enforce any of the preconditions in this module.

Author: Andy Nash
Date: 2023-01-10
"""
import utils
import pilots
import os.path
#import parser
from dateutil.parser import parse
from datetime import datetime
from datetime import date



#contains a single function called parse
# WEATHER FUNCTIONS
def bad_visibility(visibility,minimum):
    """
    Returns True if the visibility measurement violates the minimum, False otherwise
    
    A valid visibility measurement is EITHER the string 'unavailable', or a dictionary 
    with (up to) four values: 'minimum', 'maximum',  'prevailing', and 'units'. Only 
    'prevailing' and 'units' are required; the other two are optional. The units may be 
    'FT' (feet) or 'SM' for (statute) miles, and explain how to interpret other three 
    fields, which are all floats.
    
    This function should compare ths visibility 'minimum' (if it exists) against the 
    minimum parameter. Else it compares the 'prevailing' visibility. This function returns
    True if minimum is more than the measurement. If the visibility is 'unavailable', 
    then this function returns True (indicating bad record keeping).
    
    Example: Suppose we have the following visibility measurement.
        
        {
            "prevailing": 21120.0,
            "minimum": 1400.0,
            "maximum": 21120.0,
            "units": "FT"
        }
    
    Given the above measurement, this function returns True if visibility is 0.25 (miles)
    and False if it is 1.
    
    Parameter visibility: The visibility information
    Precondition: visibility is a valid visibility measurement, as described above.
    (e.g. either a dictionary or the string 'unavailable')
    
    Parameter minimum: The minimum allowed visibility (in statute miles)
    Precondition: minimum is a float or int
    """
    #data profile
    #print(visibility) #{'prevailing': 8.0, 'units': 'SM'}
    #print(visibility['units']) #SM
    #print(visibility['minimum']) #"minimum": 6000.0,
    

    #A valid visibility measurement is EITHER the string 'unavailable',
    #unavailabe returns true

    if visibility == 'unavailable':
        #print('1')
        return True

    
    #dictionary with (up to) four values: 'minimum', 'maximum',  'prevailing', and 'units'

    #This function should compare ths visibility 'minimum' (if it exists) against the minimum parameter. 
    #The units may be 'FT' (feet) or 'SM' for (statute) miles, and explain how to interpret other three 
    #fields, which are all floats.
    elif 'minimum' in visibility and visibility['units'] == 'SM':
       #print('3')
        return visibility['minimum'] < minimum
    
    elif 'minimum' in visibility and visibility['units'] == 'FT':
        #print('4')
        return visibility['minimum'] / 5280 < minimum

    # Else it compares the 'prevailing' visibility.
    elif visibility['units'] == 'SM':
        #print('5')
        return visibility['prevailing'] < minimum

    elif visibility['units'] == 'FT':
        #print('6')
        return visibility['prevailing'] / 5280 < minimum
    
    else:
        #print ('7')
        return True
    


def bad_winds(winds,maxwind,maxcross):
    """
    Returns True if the wind measurement violates the maximums, False otherwise
    
    A valid wind measurement is EITHER the string 'calm', the string 'unavailable' or 
    a dictionary with (up to) four values: 'speed', 'crosswind', 'gusts', and 'units'. 
    Only 'speed' and 'units' are required if it is a dictionary; the other two are 
    optional. The units are either be 'KT' (knots) or 'MPS' (meters per second), and 
    explain how to interpret other three fields, which are all floats.
    
    This function should compare 'speed' or 'gusts' against the maxwind parameter
    (whichever is worse) and 'crosswind' against the maxcross. If either measurement is greater
    than the allowed maximum, this function returns True.
    
    If the winds are 'calm', then this function always returns False. If the winds are
    'unavailable', then this function returns True (indicating bad record keeping).
    
    For conversion information, 1 MPS is roughly 1.94384 knots.
    
    Example: Suppose we have the following wind measurement.
        
        {
            "speed": 12.0,
            "crosswind": 10.0,
            "gusts": 18.0,
            "units": "KT"
        }
    
    Given the above measurement, this function returns True if maxwind is 15 or maxcross is 5.
    If both maxwind is 20 and maxcross is 10, it returns False.  (If 'units' were 'MPS'
    it would be false in both cases).
    
    Parameter winds: The wind speed information
    Precondition: winds is a valid wind measurement, as described above.
    (e.g. either a dictionary, the string 'calm', or the string 'unavailable')
    
    Parameter maxwind: The maximum allowable wind speed (in knots)
    Precondition: maxwind is a float or int
    
    Parameter maxcross: The maximum allowable crosswind speed (in knots)
    Precondition: maxcross is a float or int
    """
    #A valid wind measurement is EITHER the string 'calm', the string 'unavailable' or 
    #a dictionary with (up to) four values: 'speed', 'crosswind', 'gusts', and 'units'. 

    #Returns True if the wind measurement violates the maximums, False otherwise

    #If the winds are 'unavailable', then this function returns True
    



    if winds == 'calm':
        return False

    elif winds == 'unavailable':
        return True

      #gusts trumps speed
    elif winds['units'] == 'MPS':
       #print(winds['units'])
  
        if 'gusts' in winds:
            windspeed = (winds['gusts']*1.94384)
        elif 'speed' in winds:
            windspeed = (winds['speed']*1.94384)
    ## crosswind is on it's own
        crossspeed = (winds['crosswind']*1.94384)

      #gusts trumps speed  
    elif winds['units'] == 'KT':  


        if 'gusts' in winds :
            windspeed = (winds['gusts'])
        elif 'speed' in winds:
            windspeed = (winds['speed']) 
    #crosswind is on its own
        crossspeed = (winds['crosswind'])
 

    return windspeed > maxwind or crossspeed > maxcross
        
    
 
def bad_ceiling(ceiling,minimum):
    """
    Returns True if the ceiling measurement violates the minimum, False otherwise
    
    A valid ceiling measurement is EITHER the string 'clear', the string 'unavailable', 
    or a list of cloud layer measurements. A cloud layer measurement is a dictionary with 
    three required keys: 'type', 'height', and 'units'.  Type is one of 'a few', 
    'scattered', 'broken', 'overcast', or 'indefinite ceiling'. The value 'units' must 
    be 'FT', and specifies the units for the float associated with 'height'.
    
    If the ceiling is 'clear', then this function always returns False. If the ceiling 
    is 'unavailable', then this function returns True (indicating bad record keeping).
    Otherwise, it compares the minimum allowed ceiling against the lowest cloud layer 
    that is either 'broken', 'overcast', or 'indefinite ceiling'.
    
    Example: Suppose we have the following ceiling measurement.
        
        [
            {
                "cover": "clouds",
                "type": "scattered",
                "height": 700.0,
                "units": "FT"
            },
            {
                "type": "overcast",
                "height": 1200.0,
                "units": "FT"
            }
        ]
    
    Given the above measurement, this function returns True if minimum is 2000,
    but False if it is 1000.
    
    Parameter ceiling: The ceiling information
    Precondition: ceiling is a valid ceiling measurement, as described above.
    (e.g. either a dictionary, the string 'clear', or the string 'unavailable')
        
    Parameter minimum: The minimum allowed ceiling (in feet)
    Precondition: minimum is a float or int
    """
    #If the ceiling is 'clear', then this function always returns False.
    if ceiling == 'clear':
        return False

    #If the ceiling is 'unavailable', then this function returns True 

    elif ceiling == 'unavailable':
        return True
    
    #A cloud layer measurement is a dictionary with three required keys: 'type', 'height', and 'units'.
    else:
        for row in ceiling:
            #print(row)
            #it compares the minimum allowed ceiling against the lowest cloud layer that is either 'broken', 'overcast', or 'indefinite ceiling'.
    
            if row['type'] in ['broken', 'overcast', 'indefinite ceiling'] and row ['height'] < minimum:
                return True
    return False


def get_weather_report(takeoff,weather):
    """
    Returns the most recent weather report at or before take-off.
    
    The weather is a dictionary whose keys are ISO formatted timestamps and whose values 
    are weather reports.  For example, here is an example of a (small portion of) a
    weather dictionary:
        
        {
            "2017-04-21T08:00:00-04:00": {
                "visibility": {
                "prevailing": 10.0,
                "units": "SM"
            },
            "wind": {
                "speed": 13.0,
                "crosswind": 2.0,
                "units": "KT"
            },
            "temperature": {
                "value": 13.9,
                "units": "C"
            },
            "sky": [
                {
                    "cover": "clouds",
                    "type": "broken",
                    "height": 700.0,
                    "units": "FT"
                }
            ],
            "code": "201704211056Z"
        },
        "2017-04-21T07:00:00-04:00": {
            "visibility": {
                "prevailing": 10.0,
                "units": "SM"
            },
            "wind": {
                "speed": 13.0,
                "crosswind": 2.0,
                "units": "KT"
            },
            "temperature": {
                "value": 13.9,
                "units": "C"
            },
            "sky": [
                {
                    "type": "overcast",
                    "height": 700.0,
                    "units": "FT"
                }
            ],
            "code": "201704210956Z"
        }
        ...
    },
    
    If there is a report whose timestamp matches the ISO representation of takeoff, 
    this function uses that report.  Otherwise it searches the dictionary for the most
    recent report before (but not equal to) takeoff.  If there is no such report, it
    returns None.
    
    Example: If takeoff was as 8 am on April 21, 2017 (Eastern), this function returns 
    the value for key '2017-04-21T08:00:00-04:00'.  If there is no additional report at
    9 am, a 9 am takeoff would use this value as well.
    
    Parameter takeoff: The takeoff time
    Precondition: takeoff is a datetime object
    
    Paramater weather: The weather report dictionary 
    Precondition: weather is a dictionary formatted as described above
    """
    # HINT: Looping through the dictionary is VERY slow because it is so large
    
    # Only loop through the dictionary as a back-up if that fails.
    
    # Search for time in dictionary
    # As fall back, find the closest time before takeoff
   
    
    # You should convert the takeoff time to an ISO string and search for that first.
    #ISO formatted timestamp
    converted_time  = takeoff.isoformat()

    #empty string if flight is ok
 

    #If there is a report whose timestamp matches the ISO representation of takeoff, this function uses that report. 
    if converted_time in weather:
        return weather[converted_time]
        #print (weather[converted_time])
    #{'visibility': {'prevailing': 10.0, 'units': 'SM'}, 'wind': 'unavailable', 'temperature': {'value': 12.8, 'units': 'C'}, 'sky': [{'cover': 'clouds', 'type': 'a few', 'height': 1700.0, 'units': 'FT'}, {'cover': 'clouds', 'type': 'broken', 'height': 5500.0, 'units': 'FT'}, {'cover': 'clouds', 'type': 'broken', 'height': 7000.0, 'units': 'FT'}], 'code': '201710121356Z'}

    #Otherwise it searches the dictionary for the mostrecent report before (but not equal to) takeoff
    #loop through json

    #result could be None 
    recent_time = None
    most_recent = float('inf') #infinity
    #https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python

    for takeoff_timestamp, data in weather.items():
        #print (timestamp,data)
        #timetamp is iso, takeoff is datetime
        #parse timestampt to match takeoff datetime
        dt_time = parse(takeoff_timestamp)
        time_delta = takeoff - dt_time
        #print (min(time_delta)) #252 days, 3:30:00

        #mostrecent report before (but not equal to) takeoff
        #https://docs.python.org/3.7/library/datetime.html#datetime.datetime



        if time_delta.total_seconds() < most_recent and time_delta.total_seconds()> 0:
            most_recent = time_delta.total_seconds()
            #loop/accume
            recent_time = takeoff_timestamp

        #Returns the most recent weather report at or before take-off.    
    return weather[recent_time]
    


def get_weather_violation(weather,minimums):
    """
    Returns a string representing the type of weather violation (empty string if flight is ok)
    
    The weather reading is a dictionary with the keys: 'visibility', 'wind', and 'sky'.
    These correspond to a visibility, wind, and ceiling measurement, respectively. It
    may have other keys as well, but these can be ignored. For example, this is a possible 
    weather value:
        
        {
            "visibility": {
                "prevailing": 21120.0,
                "minimum": 1400.0,
                "maximum": 21120.0,
                "units": "FT"
            },
            "wind": {
                "speed": 12.0,
                "crosswind": 3.0,
                "gusts": 18.0,
                "units": "KT"
            },
            "temperature": {
                "value": -15.6,
                "units": "C"
            },
            "sky": [
                {
                    "cover": "clouds",
                    "type": "broken",
                    "height": 2100.0,
                    "units": "FT"
                }
            ],
            "weather": [
                "light snow"
            ]
        }
    
    The minimums is a list of the four minimums ceiling, visibility, and max windspeed,
    and max crosswind speed in that order.  Ceiling is in feet, visibility is in statute
    miles, max wind and cross wind speed are both in knots. For example, 
    [3000.0,10.0,20.0,8.0] is a potential minimums list.
    
    This function uses bad_visibility, bad_winds, and bad_ceiling as helpers. It returns
    'Visibility' if the only problem is bad visibility, 'Winds' if the only problem is 
    wind, and 'Ceiling' if the only problem is the ceiling.  If there are multiple
    problems, it returns 'Weather', It returns 'Unknown' if no weather reading is 
    available (e.g. weather is None).  Finally, it returns '' (the empty string) if 
    the weather is fine and there are no violations.
    
    Parameter weather: The weather measure
    Precondition: weather is dictionary containing a visibility, wind, and ceiling measurement,
    or None if no weather reading is available.
    
    Parameter minimums: The safety minimums for ceiling, visibility, wind, and crosswind
    Precondition: minimums is a list of four floats
    """
    #The weather reading is a dictionary with the keys: 'visibility', 'wind', and 'sky'.

    #need to set variables before if statements
    visbility_violation = None
    wind_violation = None
    sky_violation = None

    if weather == None:
        return 'Unknown'

    #This function uses bad_visibility, bad_winds, and bad_ceiling as helpers
    #It returns 'Visibility' if the only problem is bad visibility,    
    if bad_visibility(weather['visibility'], minimums[1]) == True:
        visbility_violation = 'Visibility'

    #'Winds' if the only problem is wind
    if bad_winds(weather['wind'], minimums[2], minimums[3]) == True:
        wind_violation = 'Winds'

    # 'Ceiling' if the only problem is the ceiling.
    if bad_ceiling(weather['sky'], minimums[0]) == True:
        sky_violation = 'Ceiling'

   
    #accumulator
    violations = []

    if visbility_violation != None:
        violations.append(visbility_violation)
    if wind_violation != None:
        violations.append(wind_violation)
    if sky_violation != None:
        violations.append(sky_violation)


  # returns '' (the empty string) if the weather is fine and there are no violations. 
    if len(violations) == 0:
        return ''

        # It returns 'Visibility' if the only problem is bad visibility, 
        # 'Winds' if the only problem is wind
        # 'Ceiling' if the only problem is the ceiling.
    elif len(violations) == 1:
        return violations[0]

        #Weather if multiple
    elif len(violations) > 1:
        return 'Weather'

 


# FILES TO AUDIT
# Sunrise and sunset
DAYCYCLE = 'daycycle.json'
# Hourly weather observations
WEATHER  = 'weather.json'
# The list of insurance-mandated minimums
MINIMUMS = 'minimums.csv'
# The list of all registered students in the flight school
STUDENTS = 'students.csv'
# The list of all take-offs (and landings)
LESSONS  = 'lessons.csv'



def list_weather_violations(directory):
    """
    Returns the (annotated) list of flight reservations that violate weather minimums.
    
    This function reads the data files in the given directory (the data files are all
    identified by the constants defined above in this module).  It loops through the
    list of flight lessons (in lessons.csv), identifying those takeoffs for which
    get_weather_violation() is not the empty string.
    
    This function returns a list that contains a copy of each violating lesson, together 
    with the violation appended to the lesson.
    
    Example: Suppose that the lessons
        
        S00687  548QR  I061  2017-01-08T14:00:00-05:00  2017-01-08T16:00:00-05:00  VFR  Pattern
        S00758  548QR  I072  2017-01-08T09:00:00-05:00  2017-01-08T11:00:00-05:00  VFR  Pattern
        S00971  426JQ  I072  2017-01-12T13:00:00-05:00  2017-01-12T15:00:00-05:00  VFR  Pattern
    
    violate for reasons of 'Winds', 'Visibility', and 'Ceiling', respectively (and are the
    only violations).  Then this function will return the 2d list
        
        [[S00687, 548QR, I061, 2017-01-08T14:00:00-05:00, 2017-01-08T16:00:00-05:00, VFR, Pattern, Winds],
         [S00758, 548QR, I072, 2017-01-08T09:00:00-05:00, 2017-01-08T11:00:00-05:00, VFR, Pattern, Visibility],
         [S00971, 426JQ, I072, 2017-01-12T13:00:00-05:00, 2017-01-12T15:00:00-05:00, VFR, Pattern, Ceiling]]
    
    REMEMBER: VFR flights are subject to minimums with VMC in the row while IFR flights 
    are subject to minimums with IMC in the row.  The examples above are all VFR flights.
    If we changed the second lesson to
    
        S00758, 548QR, I072, 2017-01-08T09:00:00-05:00, 2017-01-08T11:00:00-05:00, IFR, Pattern
    
    then it is possible it is no longer a visibility violation because it is subject to
    a different set of minimums.
    
    Parameter directory: The directory of files to audit
    Precondition: directory is the name of a directory containing the files 'daycycle.json',
    'weather.json', 'minimums.csv', 'students.csv', and 'lessons.csv'
    """
    # Load in all of the files
    import csv
    students_csv = utils.read_csv(os.path.join(directory, STUDENTS))  #contains header row
    
    minimums_csv = utils.read_csv(os.path.join(directory,MINIMUMS))  #contains header row
    weather_json = utils.read_json(os.path.join(directory, WEATHER))
    daycycle_json = utils.read_json(os.path.join(directory, DAYCYCLE))


       
    file = open(os.path.join(directory, LESSONS))
    #test = []
    results = []
    wrapper = csv.reader(file)
    next(wrapper)
    #https://stackoverflow.com/questions/14674275/skip-first-linefield-in-loop-using-csv-file
    
    # For each of the lessons
    #each row is a lesson
    for lesson in wrapper:
        #['S01075', '548QR', 'I096', '2017-10-14T15:00:00-04:00', '2017-10-14T17:00:00-04:00', 'VFR', 'Pattern']
        
        # Get the takeoff time
        get_takeoff = utils.str_to_time(lesson[3])

        # Get the pilot credentials
        get_cert = pilots.get_certification(get_takeoff, utils.get_for_id(lesson[0],students_csv))


        #violations.list_weather_violations(tests) is missing the flight 2017-03-07T08:00:00-05:00 for pilot S00591      
        #check for instructor
        instructor_check = True
        if lesson[2] == '':
            instructor_check = False

        vfr_check = True
        
        if lesson[5] == 'IFR':
            vfr_check = False

           # Get the pilot minimums
       
        get_mins = pilots.get_minimums(get_cert, lesson[6], instructor_check, vfr_check, utils.daytime(get_takeoff, daycycle_json), minimums_csv)

        # Get the weather conditions
        weather = get_weather_report(get_takeoff, weather_json)

        # Check for a violation and add to result if so
        vioaltions = get_weather_violation(weather,get_mins)
        if vioaltions != '':
            lesson.append(vioaltions)
            results.append(lesson)

    # Returns the (annotated) list of flight reservations that violate weather minimums.
    return results

