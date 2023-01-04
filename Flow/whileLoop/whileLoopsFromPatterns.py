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
    pos = 0

    while pos < len(s):
    #instead of for pos in range(len(s)):

###debugging
    #limit = 12
    #while pos < len(s):
        # 0 less than length length of hello world
    #    #print(pos)
    #    if limit > 0:
    #        limit = limit - 1
    #    else:
    #        break

        if pos % n == 0:
            #print ('the pos is '+str(pos))
            word = word + s[pos]
            #print ('the result so far is '+str(word))
            pos = pos+1
            #rint('the next pos will be '+str(pos))
        else:
            #print(str(pos)+' is not muptiple of n')
            pos = pos+1

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
    row = 0
    index = 0

    #break the tuple in to rows
    while row < len(tup):
        #print(row)
    ###debugging
    #limit = 12
    #while row < len(tup):
    #    print('the row being looked at is '+str(row))
    #    if limit > 0:
    #        limit = limit - 1
    #    else:
    #        break

        if tup[row] == index:
            print ('matched row on '+str(row)+' on index '+str(index))
            result = result +(row,)
            #print('result '+str(row))
            row = row + 1
            index = index +1

        else:
            #print ('no match row on '+str(row)+' on index '+str(index))
            row = row + 1
            index = index +1

    print (result)


#skip('hello world',4)
#returns 'hor'
fixed_points((2,1,0))
#introcs.assert_equals((0,2),result)
#fixed_points((2,1,2,1))
#    introcs.assert_equals((1,2),result)
