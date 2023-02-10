"""
Module that validates the flight school's records.

This is the primary module that does all of the work. It loads the files, loops through
the lessons, and searches for any takeoffs that violate insurance requirements.

Technically, we could have put many of these functions in __main__.py.  That is the
main module of this application anyway.  However, for testing purposes we want all
functions in modules and we only want script code in the file __main__.py

Author: YOUR NAME HERE
Date: THE DATE HERE
"""
import utils
import tests
import os.path
import violations

# Uncomment for the extra credit
#import endorsements
#import inspections


def discover_violations(directory,output):
    """
    Searches the dataset directory for any flight lessons the violation regulations.
    
    This function will call list_weather_violations() to get the list of weather violations.
    If list_endorsment_violations (optional) is completed, it will call that too, as
    well as list_inspection_violations.  It will concatenate all of these 2d lists
    into a single 2d list of violations (so a flight may be listed more than once for
    each of the three types of violations).
    
    If the parameter output is not None, it will create the CSV file with name output
    and write the 2d list of violations to this file.  This CSV file should have the
    following header:
    
        STUDENT,AIRPLANE,INSTRUCTOR,TAKEOFF,LANDING,FILED,AREA,REASON
    
    Regardless of whether output is None, this function will print out the number of
    violations, as follows:
    
        '23 violations found.'
    
    If no violations are found, it will say
    
        'No violations found.'
    
    Parameter directory: The directory of files to audit
    Precondition: directory is the name of a directory containing the files 'daycycle.json',
    'weather.json', 'minimums.csv', 'students.csv', 'teachers.csv', 'lessons.csv',
    'fleet.csv', and 'repairs.csv'.
    
    Parameter output: The CSV file to store the results
    Precondition: output is None or a string that is a valid file name
    """
    header = [['STUDENT', 'AIRPLANE', 'INSTRUCTOR', 'TAKEOFF', 'LANDING', 'FILED', 'AREA', 'REASON']]

    #call list_weather_violations() to get the list of weather violations
    #method to get from other file get_takeoff = utils.str_to_time(lesson[3])
    get_violations = violations.list_weather_violations(directory)
    #Example: ['S01155', '133CZ', 'I061', '2017-12-30T09:00:00-05:00', '2017-12-30T11:00:00-05:00', 'VFR', 'Pattern', 'Visibility']
   
    #add header to violations data
    output_format = header + get_violations
    
    #concatenate all of these 2d lists into a single 2d list of violations



    #If the parameter output is not None, it will create the CSV file with name "output"
    #and write the 2d list of violations to this file. 

    #solves for app.discover_violations('tests','scratch.csv') 
    if output == None:
        filename = 'output.csv'
    else:
        filename = output
        

   
    #Regardless of whether output is None, this function will print out the number of violations
    #Example : 23 'violations found.'
    #find number of violations
    violation_count = len(get_violations)
    if violation_count > 1: 
        print_violation_count = (str(repr(violation_count)+ ' violations found.'))
    
    # this line removes the pluarlizaton for "violations" if there is only 1 violation
    elif violation_count ==1:
        print_violation_count = (str(repr(violation_count)+ ' violation found.'))

    #if none 'No violations found.'
    else:
        print_violation_count = 'No violations found.'

    utils.write_csv(output_format,filename)
 
    print(print_violation_count)


def execute(args):
    """
    Executes the application or prints an error message if executed incorrectly.
    
    The arguments to the application (EXCLUDING the application name) are provided to
    the list args. This list should contain either 1 or 2 elements.  If there is one
    element, it should be the name of the data set folder or the value '--test'.  If
    there are two elements, the first should be the data set folder and the second
    should be the name of a CSV file (for output of the results).
    
    If the user calls this script incorrectly (with the wrong number of arguments), this
    function prints:
    
        Usage: python auditor dataset [output.csv]
    
    This function does not do much error checking beyond counting the number of arguments.
    
    Parameter args: The command line arguments for the application (minus the application name)
    Precondition: args is a list of strings
    """

    """
    The main application function is execute. It takes the command line arguments and decides whether 
    to call discover_violations or tests.test_all(). 
    If the user provides a data file, the function runs discover_violations.
    If the user provides the argument --test it runs the main test function.

    You have already seen an example of something similar in the course videos. 
    The application to_celsius contains a function execute that can either be used to test the function 
    or run the temperature application. This code is available in the samples folder under unit3.
    Take a look at this sample code now and use it to complete your execute function.
    """

    #Executes the application or prints an error message if executed incorrectly.

    user_input = len(args)
    if user_input == 0:
        print('Usage: python auditor dataset [output.csv]')

    #input is arguments to application (a list of 1 or 2 elements) 
    #app.execute(['KITH-2017', '--test'])
    elif user_input == 2 and args[1] =='--test':
        print('Usage: python auditor dataset [output.csv]')
     
    #app.execute(['--test', 'KITH-2017']) did not print out an error message  
    elif user_input == 2 and args[0] == '--test':
        #tests.test_all()
        print('Usage: python auditor dataset [output.csv]')
    
    #app.execute(['KITH-2017', 'output.csv', '--test']) did not print out an error message
    elif user_input > 2:
        print('Usage: python auditor dataset [output.csv]')

    #app.execute(['--test']) did not call a test procedure
    elif args[0] =='--test':
        tests.test_all()
    
    #app.execute(['KITH-2017', None]) did not call 'discover_violations'
    #else:
    #discover violations scenario
           
    #       if 1 element it should be the name of the data set folder or value '--test'
    elif user_input ==1 and args[0] != '--test':
            discover_violations(args)
            #if there are 2 elements the first should be should be the data set folder, second the name of CSV file('ouptut.csv')
    elif user_input == 2 and args[0] != '--test':
           discover_violations(args[0],args[1])
            


    
   



