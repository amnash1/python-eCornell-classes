"""
A function to check the validity of a numerical string

Author: Andy Nash
Date: 2022-11-19
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.

    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.

    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).

    Examples:
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False

    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """
    length = len(s)
    # one million
    #result = False


    if s =='1,000,000':
        result = True

    # >= than 100,000 <1,000,000
    # if 6 digits and the leading is not a 0
    # and [3] place is a comma
    elif length == 7 and (s[0] != '0') and (s[3] == ','):
        # then strip the comma
        strip = introcs.replace_str(s,',','')
        #check if is numeric
        result = introcs.isnumeric(strip)

    # >= than 10,000 <100,000imp
    # if 6 digits and the leading is not a 0
    # and [2] place is a comma s[1] ==','
    elif length == 6 and (s[0] != '0') and (s[2] == ','):
        # then strip the comma
        strip = introcs.replace_str(s,',','')
        #check if is numeric
        result = introcs.isnumeric(strip)

    # between 1,000 and 9,999
    # if 5 digits and the leading is not a 0
    # and [1] place is a comma s[1] ==','
    elif length == 5 and (s[0] != '0') and (s[1] == ','):
    # and (introcs.replace_str(s,',','')) and (introcs.isnumeric(s)):
        # then strip the comma
        strip = introcs.replace_str(s,',','')
        #check if is numeric
        result = introcs.isnumeric(strip)

    # >= than 100 <1,000
    elif length == 3 and (s[0] != '0') and introcs.isnumeric(s):
        result = True

    # >= than 10 < 100
    elif length == 2 and (s[0] != '0') and introcs.isnumeric(s):
        result = True

    # < 10
    elif length == 1  and introcs.isnumeric(s):
        result = True

    else:
        result = False

    return result if result == True else False
