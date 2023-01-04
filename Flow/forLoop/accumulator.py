"""
Module with more complex for-loop functions.

All of these functions make use of accumulators that make new tuples.

Author: YOUR NAME HERE
Date: THE DATE HERE
"""
import introcs

def clamp(tup,min,max):
    """
    Returns a copy of tup where every element is between min and max.

    Any number in the tuple less than min is replaced with min.  Any number
    in the tuple greater than max is replaced with max. Any number between
    min and max is left unchanged.

    Examples:
        clamp((-1, 1, 3, 5),0,4) returns (0,1,3,4)
        clamp((-1, 1, 3, 5),-2,8) returns (-1,1,3,5)
        clamp((-1, 1, 3, 5),-2,-1) returns (-1,-1,-1,-1)
        clamp((),0,4) returns ()

    Parameter tup: the tuple to copy
    Precondition: tup is a tuple of numbers (float or int)

    Parameter min: the minimum value for the tuple
    Precondition: min <= max is a number

    Parameter max: the maximum value for the tuple
    Precondition: max >= min is a number
    """
    #first initialize and empty tuples
    clamped = ()
    #then intilaize and empty county vaariable

    for x in tup:
        # if the tuple is within min/max range
        if x > min and x < max:
            clamped = clamped + (x,)
            #the comma is important!
            #print('between, clamped='+str(clamped))
        elif x<= min:
            clamped = clamped + (min,)
            #print('less than min, clamped='+str(clamped))
        else:
            clamped = clamped + (max,)
            #print('great than max, clamped='+str(clamped))
    return clamped


def uniques(tup):
    """
    Returns the number of unique elements in the tuple.

    Examplse:
        uniques((5, 9, 5, 7)) returns 3
        uniques((5, 5, 1, 'a', 5, 'a')) returns 3
        f returns 0

    Parameter tup: the tuple to copy
    Precondition: tup is a tuple
    """
    #make a new tuple that contains each element of the original tuple,
    #but only contains it once. Then return the length of this new tuple.

    #new tuple
    element = ()

    for x in tup:
        if x not in element:
            #print (x)
            element = element + (x,)
            #print ('the new tuple '+str(element))

    #return length of new tuple
    return len(element)
