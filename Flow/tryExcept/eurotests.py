"""
A completed test script for the eurofloattion iseurofloat.

Author: Walker M. White
Date: July 30, 2019
"""
import eurofloat
import introcs


def test_iseurofloat():
    """
    Test procedure for the eurofloattion iseurofloat()
    """
    print('Testing iseurofloat()')

    result = eurofloat.iseurofloat('12,5')
    introcs.assert_equals(True,result)

    result = eurofloat.iseurofloat('12,0')
    introcs.assert_equals(True,result)

    result = eurofloat.iseurofloat('0,5')
    introcs.assert_equals(True,result)

    result = eurofloat.iseurofloat('00,5')       # This is consistent with traditional float
    introcs.assert_equals(True,result)

    result = eurofloat.iseurofloat('-12,5')
    introcs.assert_equals(True,result)

    result = eurofloat.iseurofloat('12')
    introcs.assert_equals(False,result)

    result = eurofloat.iseurofloat('12,-5')
    introcs.assert_equals(False,result)

    result = eurofloat.iseurofloat(',5')
    introcs.assert_equals(False,result)

    result = eurofloat.iseurofloat('12,')
    introcs.assert_equals(False,result)

    result = eurofloat.iseurofloat('apple')
    introcs.assert_equals(False,result)

    result = eurofloat.iseurofloat('12,5.3')
    introcs.assert_equals(False,result)

    result = eurofloat.iseurofloat('12.5,3')
    introcs.assert_equals(False,result)

    result = eurofloat.iseurofloat('12,5,3')
    introcs.assert_equals(False,result)


if __name__ == '__main__':
    test_iseurofloat()
    print('Module eurofloat passed all tests.')
