"""
A function to test for floats in European format

Author: YOUR NAME HERE
Date: THE DATE HERE
"""
import introcs


def iseurofloat(s):
    """
    Returns True if s is a float in European format.  Returns False otherwise.

    In European format, a comma is used in place of a decimal point.  So '12,5' stands
    for 12.5, '0,12' stands for 0.12 and so.  Formally, a string is in European format
    if it is of the form <d1>,<d2> where d1 and d2 are ints (and d2 >= 0).  See

        https://en.wikipedia.org/wiki/Decimal_separator

    for more information.

    This function does not recognize floats in scientific notation (e.g. '1e-2').

    Examples:
        iseurofloat('12,5') returns True
        iseurofloat('-12,5') returns True
        iseurofloat('12') returns False
        iseurofloat('12,-5') returns False
        iseurofloat(',5') returns False
        iseurofloat('apple') returns False
        iseurofloat('12,5.3') returns False
        iseurofloat('12,5,3') returns False
        iseurofloat('1e-2') returns False

    Parameter s: The string to check
    Precondition: s is a string
    """
    # You MAY NOT use conditionals anywhere in this function.
    try:
        #find comma position
        comma_check = introcs.index_str(s,',') >= 0
        #find position of comma
        comma_pos = introcs.index_str(s,',')
        #print(str(comma_pos))#first value is a non-empty number
        first_numcheck = int(s[:comma_pos])
        #is there only 1 character after the comma
        next_length = len(s[comma_pos+1:]) == 1
        #print(str(next_length))
        #is the character after the comma between 0 and 10
        second_numcheck = int(s[comma_pos+1:]) >= 0
        #print(str(second_numcheck))
        return second_numcheck

    except:
        return False
