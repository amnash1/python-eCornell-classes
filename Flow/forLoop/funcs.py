"""
Module with for-loops that loop over positions.

Author: Andy Nash
Date: 2022-11-26
"""


def skip(s,n):
    """
    Returns a copy of s, only including positions that are multiples of n

    A position is a multiple of n if pos % n == 0.

    Examples:
        skip('hello world',1) returns 'hello world'
        skip('hello world',2) returns 'hlowrd'
        skip('hello world',3) returns 'hlwl'
        skip('hello world',4) returns 'hor'

    Parameter s: the string to copy
    Precondition: s is a nonempty string

    Parameter n: the letter positions to accept
    Precondition: n is an int > 0
    """
    word = ''

    for pos in range(len(s)):
        #print (pos)

        if pos%n == 0:

            word = word + s[pos]

    return word


def fixed_points(tup):
    """
    Returns a copy of tup, including only the "fixed points".

    A fixed point of a tuple is an element that is equal to its position in the tuple.
    For example 0 and 2 are fixed points of (0,3,2).  The fixed points are returned in
    the order that they appear in the tuple.

    Examples:
        fixed_points((0,3,2)) returns (0,2)
        fixed_points((0,1,2)) returns (0,1,2)
        fixed_points((2,1,0)) returns (1,)

    Parameter tup: the tuple to copy
    Precondition: tup is a tuple of ints
    """

    result = ()
    #position counter
    pos = -1
    #break the tuple in to rows

    for row in tup:
        #print ('the tuple row value is '+str(row))
        pos = pos +1
        #print ('the postion is '+str(pos))
        if pos == row:
            #print ('match value '+str(row))
            result = result +(row,)
    return result
    #print ('the result is '+str(result))

fixed_points((2,1,2,1))
#introcs.assert_equals((1,2),result)
