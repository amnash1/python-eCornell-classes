"""
A test script to test the module funcs.py

Author: Andy Nash
Date: 2022-10-11
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing


def test_has_a_vowel():
    """
    Test procedure for has_a_vowel
    """
    print('Testing has_a_vowel')

    # Test case 1
    result = funcs.has_a_vowel('aeiou')
    introcs.assert_equals(True,result)

    # Test Case 2
    result = funcs.has_a_vowel('ham')
    introcs.assert_equals(True,result)

    # Test Case 3
    result = funcs.has_a_vowel('fetch')
    introcs.assert_equals(True,result)

    # Test Case 4
    result = funcs.has_a_vowel('inch')
    introcs.assert_equals(True,result)

    # Test Case 5
    result = funcs.has_a_vowel('on')
    introcs.assert_equals(True,result)

    # Test Case 6
    result = funcs.has_a_vowel('up')
    introcs.assert_equals(True,result)

    # Test Case 7
    result = funcs.has_a_vowel('sky')
    introcs.assert_equals(False,result)

    # Test Case 8
    result = funcs.has_a_vowel('tree')
    introcs.assert_equals(True,result)

    # Test Case 9
    result = funcs.has_a_vowel('bcd')
    introcs.assert_equals(False,result)

    # Test Case 10
    result = funcs.has_a_vowel('ounce')
    introcs.assert_equals(True,result)


def test_has_y_vowel():
    """
    Test procedure for has_y_vowel
    """
    print('Testing has_y_vowel')

    # Test case 1
    result = funcs.has_y_vowel('sky')
    introcs.assert_equals(True,result)

    # Test case 2
    result = funcs.has_y_vowel('yes')
    introcs.assert_equals(False,result)

    # Test case 3
    result = funcs.has_y_vowel('es')
    introcs.assert_equals(False,result)

    # Test case 4
    result = funcs.has_y_vowel('andyyyy')
    introcs.assert_equals(True,result)

test_has_a_vowel()
test_has_y_vowel()

print('Module funcs is working correctly')
