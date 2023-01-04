"""
Module with range-based for-loop functions.

Author: Andy Nash
Date: 2022-11-25
"""

def factorial(n):
    """
    Returns n! = n * (n-1) * (n-2) ... * 1

    0! is 1.  Factorial is undefined for integers < 0.

    Examples:
        factorial(0) returns 1
        factorial(2) returns 2
        factorial(3) returns 6
        factorial(5) returns 120

    Parameter n: The integer for the factorial
    Precondition: n is an int >= 0
    """
    f = 1

    for row in range(n):
        #print ('rows '+str(row))
        bump = row+1
        #print('bumped '+str(bump))
        f =  f * bump
        #print (f)
    return f


def revrange(a,b):
    """
    Returns the tuple (b-1, b-2, ..., a)

    Note that this tuple is the reverse of tuple(range(a,b))

    Parameter a: the "start" of the range
    Precondition: a is an int <= b

    Parameter b: the "end" of the range
    Precondition: b is an int >= a
    """
    #As a hint, think about how you add to the accumulator.
    #Does it matter if you add to the left or the right?
    tup = ()
    # result = ()
    for row in range(a,b):
        tup = (row,) + tup
    return tup
