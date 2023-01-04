"""
Module to demonstrate tuple expansion.

Author: Andy Nash
Date: 2022-12-15
"""


def avg(*args):   # The parameter is MISSING.  Add it back.
    """
    Returns average of all of arguments (passed via tuple expansion)

    Remember that the average of a list of arguments is the sum of all of the elements
    divided by the number of elements.

    Examples:
        avg(1.0, 2.0, 3.0) returns 2.0
        avg(1.0, 1.0, 3.0, 5.0) returns 2.5

    Parameter args: the function arguments
    Precondition: args are all numbers (int or float)
    """

    # accumulator starts at 0
    thesum = 0
    thecount = 0
    result = 0
    # sum the tuple
    for x in args:
        thesum = thesum + x
        thecount = thecount+1

        if thecount !=0:
            result = thesum / thecount
    return (float(result))

#avg(1.0, 1.0, 3.0, 5.0)
