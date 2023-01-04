"""
Module to show off tuple methods.

Neither this module nor the function should import the introcs module.  In addition,
the function should not use a loop or recursion.

Author: Andy Nash
Date: 2022-12-10
"""


def replace_first(tup,a,b):
    """
    Returns a copy of tup with the first value of a replaced by b

    Examples:
        replace_first((1,2,1),1,3) returns (3,2,1)
        replace_first((1,2,1),4,3) returns (1,2,1)

    Parameter tup: The tuple to copy
    Precondition: tup is a tuple of integers

    Parameter a: The value to replace
    Precondition: a is an int

    Parameter b: The value to replace with
    Precondition: b is an int
    """
    result = ()

    if a in tup:
        find_pos = tup.index(a)
        # 0
        #break out tuple to a different parts
        lst = list(tup)
        #returns [1, 2, 1]
        #s[i] = x       item i of s is replaced by x
        lst[find_pos] = b
        #print(lst[find_pos])
        return (tuple(lst))

    else:
        return (tup)


replace_first((1, 2, 1),4,3)
