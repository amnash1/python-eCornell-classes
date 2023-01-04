"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Andy Nash
Date:   '2022-10-26'
"""
import introcs

APIKEY = '7Dw3IJRnzoapxpZsK9Vwux9gWxDLRKWVFyLTPRCak64e'

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, repr(s)+' is not a string.'
    assert introcs.find_str(s,' ') != -1 , repr(s)+ ' does not have at least one space.'

    #find index of space
    first = introcs.index_str(s,' ')
    #return everything before the space
    return s[:first]


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, repr(s)+' is not a string.'
    assert introcs.find_str(s,' ') != -1 , repr(s)+ ' does not have at least one space.'

    #find index of space
    after = introcs.index_str(s,' ')
    #return everthing after the space
    return s[after+1:]


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert type(s) == str, repr(s)+' is not a string.'
    assert introcs.count_str(s,'"') >=2, repr(s)+' does not have at least two" ".'

    # Search for the double quote character
    open = introcs.find_str(s,'"')
    # Returns of next character
    first = open+1
    # Search for the second double quote character after the first
    close = introcs.find_str(s,'"',open+1)
    #return characters between first and close
    return s[first:close]


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str, repr(json)+' is not a string.'

    #find the src
    src = introcs.find_str(json,'"src":')
    #return first_inside_quotes at the src
    first = json[src+6:]
    result = first_inside_quotes(first)
    return result


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str, repr(json)+' is not a string.'

    #find the dst
    dst = introcs.find_str(json,'"dst":')
    #return first_inside_quotes at the dst
    first = json[dst+6:]
    result = first_inside_quotes(first)
    return result


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str, repr(json)+' is not a string.'

    #look for error message
    err = introcs.find_str(json,'"error":')
    #get the index where error starts
    first = json[err+8:]
    #get string length of error message
    length = len(first_inside_quotes(first))
    #if it is greater than 0 then it is an error[TRUE]
    check = length>0
    return check


def service_response(src,dst,amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert type(src) == str, repr(src)+' is not a string.'
    assert type(dst) == str, repr(dst)+' is not a string.'
    #assert type(amt) in (float,int) , repr(amt)+' is not an int or float.'

    #build query
    q = ('https://ecpyfac.ecornell.com/python/currency/fixed?src='+(src)+
    '&dst='+(dst)+'&amt='+str(amt)+'&key='+APIKEY)

    #call query
    return introcs.urlread(q)


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert introcs.isalpha(currency), repr(currency)+ ' must contain only letters.'


    call = service_response(currency,currency,2.5)
    #get the index where error starts
    err = introcs.find_str(call,'error')
    #get error message
    message = call[err+8:]
    #check if error of "The rate for currency ABC is not present."
    check = introcs.find_str(message,'rate')
    return check<0


def exchange(src,dst,amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert iscurrency(src), repr(src)+' is not a string for a valid currency code.'
    assert iscurrency(dst), repr(dst)+' is not a string for a valid currency code.'
    #assert type(amt) in (float,int) , repr(amt)+' is not an int or float.'

    #call the service
    call = service_response(src,dst,amt)
    #get_dst
    destination = get_dst(call)
    #The value returned represents the amount in currency currency_to.
    currency_to = before_space(destination)
    return float(currency_to)
