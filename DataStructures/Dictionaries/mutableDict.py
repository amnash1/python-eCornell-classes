"""
Module demonstrating mutable functions on dictionaries.

All of these functions modify their dictionary arguments.

Author: Andy Nash
Date: 2022-12-19
"""


def letter_grades(adict):
    """
    Modifies the new dictionary to replace numerical grades with letter grades.

    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function replaces
    all of the numerical grades with letter grades (strings) for values.

    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60
    is an F.

    Examples:
        If a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}, letter_grades(a) changes
            a to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        If a = {} letter_grades(a) changes a to {}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    #no accumulators needed
    #relacing value in adict rather than creating new result

    for id, score in adict.items():
        #print (id,score)
        if score >= 90:
            adict[id] = 'A'
            #print (adict[id])
        elif score >= 80:
            adict[id] = 'B'
        elif score >= 70:
            adict[id] = 'C'
        elif score >= 60:
            adict[id] = 'D'
        elif score < 60:
            adict[id] = 'F'



def drop_below(adict,limit):
    """
    Deletes all students in the dictionary with grades below limit.

    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam.

    Examples: Suppose a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}
        drop_below(a,60) changes a to {'abc3' : 90, 'jms45': 86}
        drop_below(a,90) changes a to {'abc3' : 90}
        drop_below(a,95) changes a to {}
        drop_below(a,50) leaves a unchanged as {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints

    Paramater limit: the cut-off boundary
    Precondition: limit is a number (int or float)
    """
    # Hint: Create a list of netids to drop, and THEN drop them
    dropped = []
    for ids, scores in adict.items():
        #print(ids,scores)
        if scores < limit:
            dropped.append(ids)
        #    print ('id was dropped: '+str(ids))

    #delete the dropped idds
    for ids in dropped:
        del adict[ids]
        #print ('id was dropped: '+str(ids))





#a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}
#letter_grades(a)
drop_below(a,60)
