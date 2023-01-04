"""
Module with simple for-loop functions.

Author: Andy Nash
Date: 2022-11-22
"""


def lesser(tup,value):
    """
    Returns the number of elements in tup strictly less than value

    Examples:
        lesser((5, 9, 1, 7), 6) returns 2
        lesser((1, 2, 3), -1) returns 0

    Parameter tup: the tuple to check
    Precondition: tup is a non-empty tuple of ints

    Parameter value:  the value to compare to the tuple
    Precondition:  value is an int
    """
    result = 0

    for x in tup:
        #print (list)
        if x < value:
            result = result+1
            # will loop until the end of the tuple
    return result


def avg(tup):
    """
    Returns average of all of the elements in the tuple.

    Remember that the average of a tuple is the sum of all of the elements in the
    tuple divided by the number of elements in the tuple.

    Examples:
        avg((1.0, 2.0, 3.0)) returns 2.0
        avg((1.0, 1.0, 3.0, 5.0)) returns 2.5

    Parameter tup: the tuple to check
    Precondition: tup is a tuple of numbers (int or float)
    """
    # accumulator starts at 0
    thesum = 0
    thecount = 0
    result = 0
    # sum the tuple
    for x in tup:
        thesum = thesum + x
        thecount = thecount+1

        if thecount !=0:
            result = thesum / thecount
    return float(result)

    # accumulator starts at 0


    # count the values in the tuple
    #for x in tup:
    #    thecount = thecount +1
    #eturn thecount
