"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: Andy Nash
Date: 2022-11-30
"""
import introcs


def findall(text,sub):
    """
    Returns the tuple of all positions of substring sub in text.

    If sub does not appears anywhere in text, this function returns the empty tuple ().

    Examples:
        c('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)

    Parameter text: The text to search
    Precondition: text is a string

    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    result = ()
    pos = 0
    next = 0
    length = len(text)

    while pos <=len(text) and pos != -1:
    #for pos in range(len(text)):
        pos = introcs.find_str(text,sub,next,length)

        if pos != -1:
            #print(pos)
            next = pos + 1
            result = result + (pos,)

        elif pos == -1:
            result = result

    return result


#If sub does not appears anywhere in text, this function returns the empty tuple ().

#findall('how now brown cow','ow')



    #Returns the tuple of all positions of substring sub in text.
