"""
A function with several helpers.

The primary function in this module is str_to_seconds.  The functions get_hours,
get_minutes, and get_seconds are all helper functions that are used to implement
this function.  They should implemented in the order listed.

Author: Andy Nash
Date: 2022-10-15
"""
import introcs


def iso_8601(s):
    """
    Returns True if s is a string in ISO 8601 format, False otherwise

    Parameter time: The string to check
    Precondition: s is a string of length 8
    """

    assert type(s) == str, repr(s)+' is not a string.'
    assert len(s) == 8, repr(s)+ ' is not a string of length 8.'

    # '12:35:15'
    #This is a hint to get you started
    # Create variable to check if the first two characters are digits
    check1 = introcs.isdigit(s[:2])
    # Create variable to check if third character is a colon
    check2 = s[2] == ':'

    # FINISH THIS FUNCTION
    #check if middle charar are digits
    check3 = introcs.isdigit(s[3:5])
    # check if 5th character is a colon
    check4 = s[5] == ':'
    # check if last characters are digits
    check5 = introcs.isdigit(s[6:8])
    # Return True if all checks pass
    return check1 and check2 and check3 and check4 and check5



def get_seconds(time):
    """
    Returns the number of seconds in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: get_seconds('12:35:15') returns 15
    Example: get_seconds('03:02:05') returns 5
    Example: get_seconds('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str, repr(time)+' is not a string.'
    assert len(time) == 8, repr(time)+ ' is not a string of length 8.'
    assert iso_8601(time), repr(time)+ ' is not ISO8601 format.'

    sec = time[6:8]
    result = int(sec)
    return result



def get_minutes(time):
    """
    Returns the number of minutes in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: get_minutes('12:35:15') returns 35
    Example: get_minutes('03:02:05') returns 2
    Example: get_minutes('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str, repr(time)+' is not a string.'
    assert len(time) == 8, repr(time)+ ' is not a string of length 8.'
    assert iso_8601(time), repr(time)+ ' is not ISO8601 format.'

    size = len(time)
    start = size//3
    end = 2*size//3
    result = int(time[start +1 :end])

    return result

def get_hours(time):
    """
    Returns the number of hours in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: get_hours('12:35:15') returns 12
    Example: get_hours('03:02:05') returns 3
    Example: get_hours('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str, repr(time)+' is not a string.'
    assert len(time) == 8, repr(time)+ ' is not a string of length 8.'
    assert iso_8601(time), repr(time)+ ' is not ISO8601 format.'

    hr = time[:2]
    result = int(hr)
    return result

def str_to_seconds(time):
    """
    Returns the number of seconds since midnight in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.  So
    seconds, minutes, and hours may have leading 0s if they are only one digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: str_to_seconds('12:35:15') returns 45315
    Example: str_to_seconds('03:02:05') returns 10925
    Example: str_to_seconds('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str, repr(time)+' is not a string.'
    assert len(time) == 8, repr(time)+ ' is not a string of length 8.'
    assert iso_8601(time), repr(time)+ ' is not ISO8601 format.'


    seconds = get_seconds(time)
    minutes = get_minutes(time)*60
    hours = get_hours(time)*60*60
    result = hours+minutes+seconds
    return result
