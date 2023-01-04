"""
A completed test script for the Pig Latin module.

Author: Andy Nash
Date: 2022-11-20
"""
import funcs
import introcs


def test_first_vowel():
    """
    Test procedure for the function first_vowel()
    """
    print('Testing first_vowel()')
    # No vowels
    result = funcs.first_vowel('grrm')
    introcs.assert_equals(-1,result)

    # Letter a
    result = funcs.first_vowel('pat')
    introcs.assert_equals(1,result)

    # Letter e
    result = funcs.first_vowel('step')
    introcs.assert_equals(2,result)

    # Letter i
    result = funcs.first_vowel('strip')
    introcs.assert_equals(3,result)

    # Letter o
    result = funcs.first_vowel('stop')
    introcs.assert_equals(2,result)

    # Letter u
    result = funcs.first_vowel('truck')
    introcs.assert_equals(2,result)

    # Letter y, not a vowel
    result = funcs.first_vowel('ygglx')
    introcs.assert_equals(-1,result)

    # Letter y as vowel
    result = funcs.first_vowel('sky')
    introcs.assert_equals(2,result)

    # Various multi-vowel combinations
    result = funcs.first_vowel('apple')
    introcs.assert_equals(0,result)

    result = funcs.first_vowel('sleep')
    introcs.assert_equals(2,result)

    result = funcs.first_vowel('year')
    introcs.assert_equals(1,result)

    # Feel free to add more


def test_pigify():
    """
    Test procedure for the function pigify()
    """
    print('Testing pigify()')

    # begins with vowel, append hay to the end of the workd
    result = funcs.pigify('ask')
    introcs.assert_equals('askhay',result)

    result = funcs.pigify('use')
    introcs.assert_equals('usehay',result)

    result = funcs.pigify('easy')
    introcs.assert_equals('easyhay',result)

    result = funcs.pigify('over')
    introcs.assert_equals('overhay',result)

    result = funcs.pigify('issac')
    introcs.assert_equals('issachay',result)



    #begins with 'q' move 'qu' to the end and append hay
    result = funcs.pigify('quiet')
    introcs.assert_equals('ietquay',result)

    result = funcs.pigify('quay')
    introcs.assert_equals('ayquay',result)

    #begins with a consonant, move all the consonants up to the first vowel
    # to the end and add ay
    result = funcs.pigify('tomato')
    introcs.assert_equals('omatotay',result)

    result = funcs.pigify('school')
    introcs.assert_equals('oolschay',result)

    result = funcs.pigify('you')
    introcs.assert_equals('ouyay',result)

    result = funcs.pigify('sssh')
    introcs.assert_equals('ssshay',result)

    result = funcs.pigify('tquela')
    introcs.assert_equals('uelatqay',result)

    result = funcs.pigify('try')
    introcs.assert_equals('ytray',result)


test_first_vowel()
test_pigify()
print('Module funcs passed all tests.')
