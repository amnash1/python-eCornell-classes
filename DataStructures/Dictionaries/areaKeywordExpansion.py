"""
Module to demonstrate keyword expansion.

Author: Andy Nash
Date: 2022-12-19
"""
import math


def circ_area(**kwd):
    """
    Returns the area of the specified circle, defined by the keywords in kwd

    The area of a circle is PI r*r where r is the radius

    The circle may be specified by 'radius' or 'diameter', but not both.  This function
    should intentionally crash (with an AssertionError) if neither 'radius' nor 'diameter'
    are specified, or if they both are.

    Any keyword arguments other than 'radius' or 'diameter' are ignored.

    Examples:
        circ_area(radius=3) returns approx 28.27433
        circ_area(diameter=4) returns approx 12.56637
        circ_area(radius=3,foo=20) returns approx 28.27433
        circ_area() crashes with AssertionError
        circ_area(radius=2,diameter=4) crashes with AssertionError

    Parameter kwd: the function keyword arguments
    Precondition: the arguments are all numbers (int or float)
    """
    #crash (with an AssertionError) if neither 'radius' nor 'diameter'
    assert 'radius' not in kwd or 'diameter' not in kwd
    #or if they both are.
    #double negative
    assert 'radius' in kwd or 'diameter' in kwd
    #base calculations
    #area = math.pi*(kwd['radius']*kwd['radius'])
    #area = math.pi*(kwd['diameter']/2)*(kwd['diameter']/2

    if 'radius' in kwd:
        area = math.pi*(kwd['radius']*kwd['radius'])
        #print(area)
    elif 'diameter' in kwd:
        area = math.pi*(kwd['diameter']/2)*(kwd['diameter']/2)
        #print(area)

    return area


#circ_area(something=3)
circ_area(radius=4)
