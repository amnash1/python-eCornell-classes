"""
Module demonstrating immutable functions on dictionaries

All of these functions make use of accumulators.

Author: Andy Nash
Date: 2022-12-18
"""


def average_grade(adict):
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This function
    averages those grades and returns a value.

    Examples:
        average_grade({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns (55+90+86)/3 = 77
        average_grade({'wmw2' : 55}) returns 55
        average_grade({}) returns 0

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    thesum = 0
    thecount = 0
    result = 0

    for id in adict:
        #print (id)
        thesum = thesum + adict[id]
        #print(thesum)
        thecount = thecount+1
        #print(thecount)

        if thecount !=0:
            result = thesum / thecount
    return result



def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.

    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function returns a
    new dictionary with netids for keys and letter grades (strings) for values.

    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60
    is an F.

    Examples:
        letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns
            {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        letter_grades({}) returns {}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    result = {}

    for id, score in adict.items():
        #print (id,score)
        if score >= 90:
            result[id] = 'A'
            #print (result[id])
        elif score >= 80:
            result[id] = 'B'
        elif score >= 70:
            result[id] = 'C'
        elif score >= 60:
            result[id] = 'D'
        elif score < 60:
            result[id] = 'F'
    return result


letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86})
