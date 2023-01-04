"""
The functions for the course project.

Author: Andy Nash
Date: 2022-10-17
"""

import introcs

def matching_parens(s):
    """
    Returns True if the string s has a matching pair of parentheses.

    A matching pair of parentheses is an open parens '(' followed by a closing
    parens ')'.  Any thing can be between the two pair (including other parens).

    Example: matching_parens('A (B) C') returns True
    Example: matching_parens('A )B( C') returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """
    assert type(s) == str, repr(s)+' is not a string.'

    # Search for the first open parens '('
    open = introcs.find_str(s,'(')
    # Search for the first close parens ')' AFTER the open parens
    close = introcs.find_str(s,')',open)
    # Compare both searches to -1 and return True if BOTH are not -1

    return open != -1 and close != -1


def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Example: first_in_parens('A (B) C') returns 'B'
    Example: first_in_parens('A (B) (C)') returns 'B'
    Example: first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    assert matching_parens(s), repr(s)+ ' does not have a matching pair of parens.'

    # Search for the first open parens '('
    open = introcs.find_str(s,'(')
    # Returns of next character
    first = open+1
    # Search for the first close parens ')'
    close = introcs.find_str(s,')',open)
    return s[first:close]
