"""
A function to extract names from e-mail addresses.

Author: Andy Nash
Date: 2022-11-18
"""
import introcs


def extract_name(s):
    """
    Returns the first name of the person in e-mail address s.

    We assume (see the precondition below) that the e-mail address is in one of
    three forms:

        last.first@megacorp.com
        last.first.middle@consultant.biz
        first.last@mompop.net

    where first, last, and middle correspond to the person's first, middle, and
    last name. Names are not empty, and contain only letters. Everything after the
    @ is guaranteed to be exactly as shown.

    The function preserves the capitalization of the e-mail address.

    Examples:
        extract_name('smith.john@megacorp.com') returns 'john'
        extract_name('McDougal.Raymond.Clay@consultant.biz') returns 'Raymond'
        extract_name('maggie.white@mompop.net') returns 'maggie'
        extract_name('Bob.Bird@mompop.net') returns 'Bob'

    Parameter s: The e-mail address to extract from
    Precondition: s is in one of the two address formats described above
    """
    mega = '@megacorp.com'
    mompop = '@mompop.net'
    middle = '@consultant.biz'

    # find if @megacorp
    if mega in s:
        #find pos of @
        at = introcs.find_str(s,'@')
        #return before @
        at2 = s[:at]
        #find dot
        dot = introcs.find_str(at2,'.')
        #return after the doct
        return at2[dot+1:]

    #elif first name with middle name included
    elif middle in s:
        #find pos of @
        at = introcs.find_str(s,'@')
        #return before @
        r_at = s[:at]
        #find dot
        dot = introcs.find_str(r_at,'.')
        #return after the dot
        dot2 = r_at[dot+1:]
        #find dot of remainder
        f = introcs.find_str(dot2,'.')
        #return before the dot
        return dot2[:f]

    #else first name first
    else:
        #find pos of @
        at = introcs.find_str(s,'@')
        #return before @
        at2 = s[:at]
        #find dot
        dot = introcs.find_str(at2,'.')
        #return before the dot
        return at2[:dot]
