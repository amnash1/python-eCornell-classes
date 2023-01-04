"""
The test script for the course project.

Author: Andy Nash
Date: 2022-10-17
"""

import introcs
import funcs

def test_matching_parens():
    """
    Test procedure for matching_parens
    """
    print('Testing matching_parens')

    #test case 1
    #Example: matching_parens('A (B) C') returns True
    result = funcs.matching_parens('A (B) C')
    introcs.assert_equals(True,result)

    #test case 2
    #matching_parens('A )B( C') returns False
    result = funcs.matching_parens('A )B( C')
    introcs.assert_equals(False,result)

    #test case 3
    result = funcs.matching_parens('A (B) (C)')
    introcs.assert_equals(True,result)

    #test case 4
    result = funcs.matching_parens('A ((B) (C))')
    introcs.assert_equals(True,result)

    #test case 5
    result = funcs.matching_parens('A B C')
    introcs.assert_equals(False,result)

    #test case 6
    result = funcs.matching_parens('(A B( (C')
    introcs.assert_equals(False,result)

    #test case 7
    result = funcs.matching_parens('')
    introcs.assert_equals(False,result)



def test_first_in_parens():
    """
    Test procedure for first_in_parens
    """
    print ('Testing first_in_parens')

    #test case 1
    #Example: first_in_parens('A (B) C') returns 'B'
    result = funcs.first_in_parens('A (B) C')
    introcs.assert_equals('B',result)

    #test case 2
    #Example: first_in_parens('A (B) (C)') returns 'B'
    result = funcs.first_in_parens('A (B) (C)')
    introcs.assert_equals('B',result)

    #test case 3
    #Example: first_in_parens('A ((B) (C))') returns '(B'
    result = funcs.first_in_parens('A ((B) (C))')
    introcs.assert_equals('(B',result)

    #test case 4
    #Example: first_in_parens('(A B C)') returns 'A B C'
    result = funcs.first_in_parens('(A B C)')
    introcs.assert_equals('A B C',result)

    #test case 5
    #Example: first_in_parens('(A B( (C)') returns 'A B( (C'
    result = funcs.first_in_parens('(A B( (C)')
    introcs.assert_equals('A B( (C',result)

# Script Code
test_matching_parens()
test_first_in_parens()

print('Module funcs is working correctly')
