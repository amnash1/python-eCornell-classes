"""
Module determining pilot certifications, ratings, and endorsements.

The restrictions that we place on a pilot depend on their qualifications.  There are three
ways to think about a pilot.  

(1) Certifications.  These are what licenses a pilot has.  We also use these to classify
where the student is in the licensing process.  Is the student post solo (can fly without
instructor), but before license?  Is the student 50 hours past their license (a threshold 
that helps with insurance)?

(2) Ratings.  These are extra add-ons that a pilot can add to a license. For this project,
the only rating is Instrument Rating, which allows a pilot to fly through adverse weather
using only instruments.

(3) Endorsements. These are permission to fly certain types of planes solo.  Advanced 
allows a pilot to fly a plane with retractable landing gear. Multiengine allows a pilot
to fly a plane with more than one engine.

The file pilots.csv is a list of all pilots in the school, together with the dates that
they earned these certifications, ratings, and endorsements.  Specifically, this CSV file
has the following header:
    
    ID  LASTNAME  FIRSTNAME  JOINED  SOLO  LICENSE  50 HOURS  INSTRUMENT  ADVANCED  MULTIENGINE

The first three columns are strings, while all other columns are dates.

The functions in this class take a row from the pilot table and determine if a pilot has
a certain qualification at the time of takeoff. As this program is auditing the school 
over a course of a year, a student may not be instrument rated for one flight but might
be for another.

The preconditions for many of these functions are quite messy.  While this makes writing 
the functions simpler (because the preconditions ensure we have less to worry about), 
enforcing these preconditions can be quite hard. That is why it is not necessary to 
enforce any of the preconditions in this module.

Author: Andy Nash
Date: 2022-01-06
"""
from datetime import datetime
import math
from pickle import FALSE
import utils


# CERTIFICATION CLASSIFICATIONS
# The certification of this pilot is unknown
PILOT_INVALID = -1
# A pilot that has joined the school, but has not soloed
PILOT_NOVICE  = 0
# A pilot that has soloed but does not have a license
PILOT_STUDENT = 1
# A pilot that has a license, but has under 50 hours post license
PILOT_CERTIFIED = 2
# A pilot that 50 hours post license
PILOT_50_HOURS  = 3


def get_certification(takeoff,student):
    """
    Returns the certification classification for this student at the time of takeoff.
    
    The certification is represented by an int, and must be the value PILOT_NOVICE, 
    PILOT_STUDENT, PILOT_CERTIFIED, PILOT_50_HOURS, or PILOT_INVALID. It is PILOT_50_HOURS 
    if the student has certified '50 Hours' before this flight takeoff.  It is 
    PILOT_CERTIFIED if the student has a private license before this takeoff and 
    PILOT_STUDENT if the student has soloed before this takeoff.  A pilot that has only
    just joined the school is PILOT_NOVICE.  If the flight takes place before the student
    has even joined the school, the result is PILOT_INVALID.
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object with a time zone
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """

    #takeoff time formatted like 2015-01-14T08:00:00'
    #pilot does not exist before takeoff
    if takeoff < datetime.strptime(student[3] + '+0000', '%Y-%m-%d%z'):
        
        return PILOT_INVALID


    if student[4] and datetime.strptime(student[4] + '+0000', '%Y-%m-%d%z') < takeoff:
        #print (student, student[4])
        if student[5] and datetime.strptime(student[5] + '+0000', '%Y-%m-%d%z') < takeoff:
            if student[6] and datetime.strptime(student[6] + '+0000', '%Y-%m-%d%z') < takeoff:
                #print(PILOT_50_HOURS)
                return PILOT_50_HOURS
                
            else:
                #print(PILOT_CERTIFIED)
                return PILOT_CERTIFIED
                
        else:
            #print(PILOT_STUDENT)
            return PILOT_STUDENT
           
    else:
        #print (PILOT_NOVICE)
        return PILOT_NOVICE
        



def has_instrument_rating(takeoff,student):
    """
    (OPTIONAL)
    Returns True if the student has an instrument rating at the time of takeoff, False otherwise
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    NOTE: Just because a pilot has an instrument rating does not mean that every flight
    with that pilot is an IFR flight.  It just means the pilot could choose to use VFR
    or IFR rules.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
    pass                    # Implement this function


def has_advanced_endorsement(takeoff,student):
    """
    (OPTIONAL)
    Returns True if the student has an endorsement to fly an advanced plane at the time of takeoff.
    
    The function returns False otherwise.
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
    pass                    # Implement this function


def has_multiengine_endorsement(takeoff,student):
    """
    (OPTIONAL)
    Returns True if the student has an endorsement to fly an multiengine plane at the time of takeoff.
    
    The function returns False otherwise.
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
    pass                    # Implement this function

def get_best_value(data, index, maximum=True):
    """
    Returns the 'best' value from a given column in a 2-dimensional nested list.
    
    This function is a helper function for get_minimums (whose docstring you should
    read and understand first). 
    
    The data parameter is a 2-dimensional nested list of data.  The index parameter
    indicates which "colummn" of data should be evaluated. Each item in that column
    is expected to be a number in string format.  Each item should be evaluated as a 
    float and the best value selected as the return value for the function. The
    best value is determined by the maximum parameter and is either the highest or
    lowest float value.

    The 2D list does not include a header row. It should not be modified in any way.
    
    Parameter data: a 2-dimensional nested list of data
    Precondition: the column referenced by index should by numbers in string format
    
    Parameter index: position to examine in each row of data
    Precondition: index is a an integer
    
    Parameter maximum: indicates whether to return the highest value (True) or
    lowest value (False)
    Precondition: maximum is a boolean and defaults to True
    
    """
    # Find the best values for each column of the row
    # index is given 
    # data is given 

    #Each item should be evaluated as a float and the best value selected as the return value for the function. 
    # get data at the index field and cast as float


    #more generic helper function called get_best_value that can loop through any nested list and examine one
    #specified column, identifying either the highest or lowest value.


    #this actually identfies the lowest and highest values in the column  
    
    result = float(data[0][index])    
    #print('result ' + str(result))
    
    for row in data[:]: # skip header row with [:]
       value = float(row[index])
       #print(value)
       if (maximum and value > result) or (not maximum and value < result):
           result = value
    #print(result)
    return result


def get_minimums(cert, area, instructed, vfr, daytime, minimums):
    """
    Returns the most advantageous minimums for the given flight category.
    
    The minimums is the 2-dimensional list (table) of minimums, including the header.
    The header for this table is as follows:
        
        CATEGORY  CONDITIONS  AREA  TIME  CEILING  VISIBILITY  WIND  CROSSWIND
    
    The values in the first four columns are strings, while the values in the last
    four columns are numbers.  CEILING is a measurement in ft, while VISIBILITY is in
    miles.  Both WIND and CROSSWIND are speeds in knots.
    
    This function first searches the table for rows that match the function parameters. 
    It is possible for more than one row to be a match.  A row is a match if ALL four 
    of the first four columns match.
    
    The first column (CATEGORY) has values 'Student', 'Certified', '50 Hours', or 'Dual'.
    If the value 'Student', it is a match if cert is PILOT_STUDENT or higher.  If the
    value is 'Certified', it is a match if cert is PILOT_CERTIFIED or higher. If it is 
    '50 Hours', it is only a match if cert is PILOT_50_HOURS. The value 'Dual' only
    matches if instructed is True and even if cert is PILOT_INVALID or PILOT_NOVICE.
    
    The second column (CONDITIONS) has values 'VMC' and 'IMC'. A flight filed as VFR 
    (visual flight rules) is subject to VMC (visual meteorological conditions) minimums.  
    Similarly, a fight filed as IFR is subject to IMC minimums.
    
    The third column (AREA) has values 'Pattern', 'Practice Area', 'Local', 
    'Cross Country', or 'Any'. Flights that are in the pattern or practice area match
    'Local' as well.  All flights match 'Any'.
    
    The fourth column (TIME) has values 'Day' or 'Night'. The value 'Day' is only 
    a match if daytime is True. If it is False, 'Night' is the only match.
    
    Once the function finds the all matching rows, it searches for the most advantageous
    values for CEILING, VISIBILITY, WIND, and CROSSWIND. Lower values of CEILING and
    VISIBILITY are better.  Higher values for WIND and CROSSWIND are better.  It then
    returns this four values as a list of four floats (in the same order they appear)
    in the table.
    
    Example: Suppose minimums is the table
        
        CATEGORY   CONDITIONS  AREA           TIME  CEILING  VISIBILITY  WIND  CROSSWIND
        Student    VMC         Pattern        Day   2000     5           20    8
        Student    VMC         Practice Area  Day   3000     10          20    8
        Certified  VMC         Local          Day   3000     5           20    20
        Certified  VMC         Practice Area  Night 3000     10          20    10
        50 Hours   VMC         Local          Day   3000     10          20    10
        Dual       VMC         Any            Day   2000     10          30    10
        Dual       IMC         Any            Day   500      0.75        30    20
    
    The call get_minimums(PILOT_CERTIFIED,'Practice Area',True,True,True,minimums) matches
    all of the following rows:
        
        Student    VMC         Practice Area  Day   3000     10          20    8
        Certified  VMC         Local          Day   3000     5           20    20
        Dual       VMC         Any            Day   2000     10          30    10
    
    The answer in this case is [2000,5,30,20]. 2000 and 5 are the least CEILING and 
    VISIBILITY values while 30 and 20 are the largest wind values.
    
    If there are no rows that match the parameters (e.g. a novice pilot with no 
    instructor), this function returns None.
    
    Parameter cert: The pilot certification
    Precondition: cert is an int and one of PILOT_NOVICE, PILOT_STUDENT, PILOT_CERTIFIED, 
    PILOT_50_HOURS, or PILOT_INVALID.
    
    Parameter area: The flight area for this flight plan
    Precondition: area is a string and one of 'Pattern', 'Practice Area' or 'Cross Country'
    
    Parameter instructed: Whether an instructor is present
    Precondition: instructed is a boolean
    
    Parameter vfr: Whether the pilot has filed this as an VFR flight
    Precondition: vfr is a boolean
    
    Parameter daytime: Whether this flight is during the day
    Precondition: daytime is boolean
    
    Parameter minimums: The table of allowed minimums
    Precondition: minimums is a 2d-list (table) as described above, including header
    """
    # Find all rows that can apply to this student
  
    # HINT: remember to use get_best_value to find best value in list of matches
    
    
    matches = []
    for row in minimums[:]: #skip the header
    
        if (row[0] == 'Student' and cert >= PILOT_STUDENT) or (row[0] == 'Certified' and cert >= PILOT_CERTIFIED) or (row[0] == '50 Hours' and cert == PILOT_50_HOURS) or (row[0] == 'Dual' and instructed):
            
            if (row[1] == 'VMC' and vfr) or (row[1] == 'IMC' and not vfr):
                if (row[2] == 'Any') or (row[2] == 'Local' and (area == 'Pattern' or area == 'Practice Area')) or (row[2] == area):
                    if (row[3] == 'Day' and daytime) or (row[3] == 'Night' and not daytime):
                        matches.append(row)
                        #matches.append(list(row[-4:]))
   
    #['Dual', 'IMC', 'Any', 'Day', '500', '0.75', '30', '20']]
    
    # (pilots.PILOT_STUDENT,  'Practice Area',True,True, False,table,19),
    if len(matches) == 0:
       return None

    # Find the best values for each column of the row
    else:
    #Lower values of CEILING and VISIBILITY are better.  Higher values for WIND and CROSSWIND are better.    
    #Remember, after you have built a list of minimums that are valid matches for the various function parameters, 
    # you simply need to call get_best_value four times, once for each of the CEILING, VISIBILITY, WIND, 
    # and CROSSWIND columns in that list of matches,
        best_ceiling = get_best_value(matches,4,maximum=False)
        best_visibility = get_best_value(matches,5,maximum=False)
        best_wind = get_best_value(matches,6)
        best_crosswind = get_best_value(matches,7)
        return [best_ceiling, best_visibility, best_wind, best_crosswind]
    

    
    """
    matches = []
    for row in minimums[1:]:
        col0 = False
        if row[0] == 'Student':
            col0 = cert >= PILOT_STUDENT
        elif row[0] == 'Certified':
            col0 = cert >= PILOT_CERTIFIED
        elif row[0] == '50 Hours':
            col0 = cert >= PILOT_50_HOURS
        elif row[0] == 'Dual':
            col0 = instructed
        col1 = row[1] == ('VMC' if vfr else 'IMC')
        col2 = (row[2] == area) or (row[2] == 'Local' and area != 'Cross Country') or (row[2] == 'Any')
        col3 = row[3] == ('Day' if daytime else 'Night')

        #matches.append(row)

        if col0 and col1 and col2 and col3:
            matches.append(list(row[-4:]))
           

    
    
    if matches == []:
        return None


    else:
    
   # best_ceiling_data = (matches[0][0])
        #result = matches[0][:]
        #print(matches)
        #print (len(matches))
        best_ceiling = get_best_value(matches,0)
        best_visibility = get_best_value(matches,1)
        best_wind = get_best_value(matches,2)
        best_crosswind = get_best_value(matches,3)
        return [best_ceiling, best_visibility, best_wind, best_crosswind]
  
   

 """   




        