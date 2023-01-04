"""
Functions for simple reading to and writing from a file.

Author: Andy Nash
Date:   2022-12-29
"""


def count_lines(filepath):
    """
    Returns the number of lines in the given file.

    Lines are separated by the '\n' character, which is standard for Unix files.

    Parameter filepath: The file to be read
    Precondition: filepath is a string with the FULL PATH to a text file
    """
    # HINT: Remember, you can use a file in a for-loop
           # Implement me
    #use an accumulator to count the number of times the body of the loop was executed.
    cnt = 0
    file = open(filepath)
    #The easiest way to do this function is to put the file in a for-loop
    for line in file:
        cnt = cnt + 1
    file.close()
    return cnt


def write_numbers(filepath,n):
    """
    Writes the numbers 0..n-1 to a file.

    Each number is on a line by itself.  So the first line of the file is 0,
    the second line is 1, and so on. Lines are separated by the '\n' character,
    which is standard for Unix files.  The last line (the one with the number
    n-1) should NOT end in '\n'

    Parameter filepath: The file to be written
    Precondition: filepath is a string with the FULL PATH to a text file

    Parameter n: The number of lines to write
    Precondition: n is an int > 0.
    """
                # Implement me
    #the file should not end in a blank line (e.g. there should be no '\n' after the last number).
    line = ''
    #open filepath and enable writing
    file = open(filepath,'w')

    #work = file.write(str(line)+'/n')

    #needs to stop short of end of lines for n-1
    for line in range(n-1):
        #print(range(n))
        # HINT: You can only write strings to a file, so convert the numbers first
        work = file.write(str(line)+'\n')
    file.write(str(n-1))
    file.close()


#write_numbers('files/writefle1.txt',5)
#count_lines('files/readfile1.txt')
