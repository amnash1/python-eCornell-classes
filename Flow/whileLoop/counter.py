"""
Module demonstrating an input-driven while loop

There is no test script for this module.  Run this module as a script to test it.

Author: Andy Nash
Date: 2022-11-27
"""


def count_inputs():
    """
    Returns the number of times the user chose to continue.

    This function repeated asks the user

        Keep going [y/n]?

    If the user answers 'y', the function adds one to a counter and keeps going.
    If the user answers 'n', the function quits and returns the number of times
    that the user answered
        Answer unclear. Use 'y' or 'n'.

    It will not quit in this case, but it will not add to the counter either.
    """
    # Create a counter accumulator
    result = 0
    # Create a variable 'going' to control the loop
    #start with true
    going = True

    # While the user has not told us to stop
    while going:
        # Get the input from the user
        user_input = input('Keep going [y/n]? ')
        # Respond with error message if input is bad
        if user_input != 'y' and user_input!= 'n':
            print ('Answer unclear. Use \'y\' or \'n\'.')
        # Update counter if input is 'y'
        elif user_input == 'y':
            going = True
            result = result +1
            #print ('gave y')
        # input of n kills the flow
        elif user_input == 'n':
            going = False

    return result


# Script code to test the function
# DO NOT MODIFY BELOW THIS LINE
if __name__ == '__main__':
    result = count_inputs()
    plural = ' time.' if result == 1 else ' times.'
    print("You answered 'y' "+str(result)+plural)
