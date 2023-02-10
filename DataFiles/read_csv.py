"""
Module with a function to read CSV files (converting them into a 2D list)

This function will be used in the main project.  You should hold on to it.

Author: Andy Nash
Date: 2022-12-29
"""
import csv


def read_csv(filename):
    """
    Returns the contents read from the CSV file filename.

    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the
    programmer to interpret this data, since CSV files contain no type information.

    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file
    is a valid CSV file
    """
    #combine with accum pattern to create a new table
    result = []

    #make each row a list
    #open file
    file = open(filename)
    #wrapper creates a new object
    wrapper = csv.reader(file)
    #use wrapper in a for loop
    for row in wrapper:
        #print(row)
        #put full row in a list
        result.append(row)

    file.close()
    #print(result)
    return result


read_csv('files/readcsv1.csv')
